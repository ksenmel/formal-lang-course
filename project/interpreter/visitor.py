from project.parser.GQLVisitor import GQLVisitor
from project.parser.GQLParser import GQLParser

from networkx import MultiDiGraph
from pyformlang.finite_automaton import EpsilonNFA

from project.interpreter.utils import (
    nfa_from_char,
    nfa_from_var,
    group,
    intersect,
    concatenate,
    union,
    repeat_range,
    build_rsm,
)
from project.task8_tensors import tensor_based_cfpq

from project.interpreter.exceptions import (
    VariableNotFoundException,
    RemoveGlobalScopeException,
)


class Env:
    def __init__(self):
        self.env = [{}]

    def add(self, var: str, val):
        self.env[-1][var] = val

    def next_scope(self):
        self.env.append({})

    def remove_last(self):
        if len(self.env) > 1:
            self.env.pop()
        else:
            raise RemoveGlobalScopeException

    def find(self, name: str):
        for scope in reversed(self.env):
            if name in scope:
                return scope[name]
        raise VariableNotFoundException


def add_edge(graph, expr_val):
    graph.add_edge(expr_val[0], expr_val[2], label=expr_val[1])


def add_node(graph, expr_val):
    graph.add_node(expr_val)


def get_varname(ctx: GQLParser.VarContext):
    return str(ctx.VAR().getText())


class MyVisitor(GQLVisitor):
    def __init__(self):
        self.env = Env()
        self.query = {}
        self._query_done = False

    def last_query_results(self):
        return dict(self.query)

    def visitProg(self, ctx: GQLParser.ProgContext):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx: GQLParser.StmtContext):
        return self.visitChildren(ctx)

    def visitDeclare(self, ctx: GQLParser.DeclareContext):
        name = get_varname(ctx.var())
        self.env.add(name, MultiDiGraph())

    def visitExpr(self, ctx: GQLParser.ExprContext):
        return self.visitChildren(ctx)

    def visitBind(self, ctx: GQLParser.BindContext):
        name = get_varname(ctx.var())
        value = self.visitExpr(ctx.expr())

        if isinstance(value, str) and len(value) == 1:
            value = nfa_from_char(value)

        self.env.add(name, value)

        if self._query_done:
            self._query_done = False
            self.query[name] = value

    def visitRegexp(self, ctx: GQLParser.RegexpContext):
        if ctx.char():
            return self._handle_char(ctx)
        if ctx.var():
            return self._handle_var(ctx)
        if ctx.L_BR() and ctx.R_BR():
            return self._handle_brackets(ctx)
        if ctx.CIRCUMFLEX():
            return self._handle_circumflex(ctx)
        return self._handle_binop(ctx)

    def _handle_char(self, ctx):
        return nfa_from_char(self.visitChar(ctx.char()))

    def _handle_var(self, ctx):
        return nfa_from_var(ctx.var().getText())

    def _handle_brackets(self, ctx):
        return group(self.visitRegexp(ctx.regexp(0)))

    def _handle_circumflex(self, ctx):
        left = self.visitRegexp(ctx.regexp(0))
        range_ = self.visitRange(ctx.range_())
        return repeat_range(left, self.visitNum(range_[0]), self.visitNum(range_[1]))

    def _handle_binop(self, ctx):
        left = self.visitRegexp(ctx.regexp(0))
        right = self.visitRegexp(ctx.regexp(1))
        if ctx.PIPE():
            return union(left, right)
        if ctx.DOT():
            return concatenate(left, right)
        if ctx.AMPERSAND():
            return intersect(left, right)

    def visitV_filter(self, ctx: GQLParser.V_filterContext):
        return ctx.var().getText(), self.visitExpr(ctx.expr())

    def visitAdd(self, ctx):
        graph = self.visitVar(ctx.var())
        expr_val = self.visitExpr(ctx.expr())

        if ctx.EDGE():
            add_edge(graph, expr_val)
        else:
            add_node(graph, expr_val)

    def visitRemove(self, ctx):
        graph = self.visitVar(ctx.var())
        expr_val = self.visitExpr(ctx.expr())

        if ctx.EDGE():
            graph.remove_edge(expr_val[0], expr_val[2])
        else:
            graph.remove_node(expr_val)

    def visitSet_expr(self, ctx: GQLParser.Set_exprContext):
        values = set()
        for expr in ctx.expr():
            value = self.visit(expr)
            values.add(value)

        return values

    def visitEdge_expr(self, ctx):
        exprs = ctx.expr()
        return (
            self.visitExpr(exprs[0]),
            self.visitExpr(exprs[1]),
            self.visitExpr(exprs[2]),
        )

    def visitRange(self, ctx: GQLParser.RangeContext):
        start = ctx.num(0)
        end = ctx.num(1)
        return start, end

    def visitVar(self, ctx: GQLParser.VarContext):
        name = get_varname(ctx)
        return self.env.find(name)

    def visitChar(self, ctx: GQLParser.CharContext):
        return str(ctx.CHAR().getText()[1])

    def visitNum(self, ctx: GQLParser.NumContext):
        return int(ctx.NUM().getText())

    def visitSelect(self, ctx: GQLParser.SelectContext):
        filter1 = self.visitV_filter(ctx.v_filter(0))
        filter2 = self.visitV_filter(ctx.v_filter(1))

        if not filter1 or not filter2:
            raise Exception("Both filters must be defined for a SELECT operation")

        var_list = ctx.var()
        graph = self.visitVar(var_list[-1])
        nfa_dict = {
            k: v for k, v in self.env.env[0].items() if isinstance(v, EpsilonNFA)
        }

        start_var = get_varname(var_list[-2])
        final_var = get_varname(var_list[-3])
        start_nodes = filter1[1] if start_var == filter1[0] else filter2[1]
        final_nodes = filter2[1] if final_var == filter2[0] else filter1[1]

        query = build_rsm(self._nfa_from_expr(ctx.expr()), nfa_dict)
        result = tensor_based_cfpq(query, graph, start_nodes, final_nodes)

        ret_var1 = var_list[0].getText()
        ret_var2 = var_list[1].getText()
        if ret_var1 == start_var and not ret_var2:
            output = {res[0] for res in result}
        elif ret_var1 == final_var and not ret_var2:
            output = {res[1] for res in result}
        else:
            output = result

        self._query_done = True
        return output

    def _nfa_from_expr(self, ctx):
        val = self.visitExpr(ctx)
        if isinstance(val, EpsilonNFA):
            return val
        if isinstance(val, str):
            return nfa_from_char(val)
        raise Exception(f"Cannot convert '{val}' to EpsilonNFA")
