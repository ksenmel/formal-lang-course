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


class LazyNFA:
    def __init__(self, ctx, name):
        self.ctx = ctx
        self.name = name
        self._value = None
        self._computing = False

    def get_value(self, visitor):
        if self._value is not None:
            return self._value

        if self._computing:
            return nfa_from_var(self.name)

        self._computing = True
        self._value = visitor.visitExpr(self.ctx)
        self._computing = False
        return self._value


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
        expr_ctx = ctx.expr()

        if expr_ctx.regexp():
            lazy_nfa = LazyNFA(expr_ctx, name)
            self.env.add(name, lazy_nfa)
        else:
            value = self.visitExpr(expr_ctx)
            if isinstance(value, str) and len(value) == 1:
                value = nfa_from_char(value)
            self.env.add(name, value)

        if self._query_done:
            self._query_done = False
            stored_value = self.env.find(name)
            if isinstance(stored_value, LazyNFA):
                self.query[name] = stored_value.get_value(self)
            else:
                self.query[name] = stored_value

    def visitRegexp(self, ctx: GQLParser.RegexpContext):
        regexp_and_list = ctx.regexp_and()
        result = self.visitRegexp_and(regexp_and_list[0])

        for i in range(1, len(regexp_and_list)):
            right = self.visitRegexp_and(regexp_and_list[i])
            result = union(result, right)

        return result

    def visitRegexp_and(self, ctx: GQLParser.Regexp_andContext):
        regexp_concat_list = ctx.regexp_concat()
        result = self.visitRegexp_concat(regexp_concat_list[0])

        for i in range(1, len(regexp_concat_list)):
            right = self.visitRegexp_concat(regexp_concat_list[i])
            result = intersect(result, right)

        return result

    def visitRegexp_concat(self, ctx: GQLParser.Regexp_concatContext):
        regexp_power_list = ctx.regexp_power()
        result = self.visitRegexp_power(regexp_power_list[0])

        for i in range(1, len(regexp_power_list)):
            right = self.visitRegexp_power(regexp_power_list[i])
            result = concatenate(result, right)

        return result

    def visitRegexp_power(self, ctx: GQLParser.Regexp_powerContext):
        result = self.visitRegexp_primary(ctx.regexp_primary())

        if ctx.CIRCUMFLEX():
            range_ctx = ctx.range_()
            range_ = self.visitRange(range_ctx)
            result = repeat_range(
                result, self.visitNum(range_[0]), self.visitNum(range_[1])
            )

        return result

    def visitRegexp_primary(self, ctx: GQLParser.Regexp_primaryContext):
        if ctx.char():
            return nfa_from_char(self.visitChar(ctx.char()))

        if ctx.var():
            var_name = ctx.var().getText()
            value = self.env.find(var_name)
            if isinstance(value, LazyNFA):
                return value.get_value(self)
            elif isinstance(value, EpsilonNFA):
                return value
            return nfa_from_var(var_name)

        if ctx.L_BR() and ctx.R_BR():
            return group(self.visitRegexp(ctx.regexp()))

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
        # Process all v_filter (0 or more)
        filters = []
        for i in range(len(ctx.v_filter())):
            filters.append(self.visitV_filter(ctx.v_filter(i)))

        # Parse: v_filter* RETURN var (COMMA var)? WHERE var REACHABLE FROM var IN var BY expr
        var_list = ctx.var()

        # Get return variables (1 or 2)
        return_vars = []
        return_vars.append(get_varname(var_list[0]))
        if len(var_list) > 4:  # Has second return variable
            return_vars.append(get_varname(var_list[1]))
            var_offset = 2
        else:
            var_offset = 1

        # Get WHERE/FROM/IN variables
        final_var = get_varname(var_list[var_offset])  # WHERE var
        start_var = get_varname(var_list[var_offset + 1])  # FROM var
        graph_var = var_list[var_offset + 2]  # IN var
        graph = self.visitVar(graph_var)

        # Build NFA dictionary for RSM
        nfa_dict = {}
        for k, v in self.env.env[0].items():
            if isinstance(v, LazyNFA):
                nfa_dict[k] = v.get_value(self)
            elif isinstance(v, EpsilonNFA):
                nfa_dict[k] = v

        # Match filters to start/final variables
        start_nodes = None
        final_nodes = None

        filter_dict = {f[0]: f[1] for f in filters}

        if start_var in filter_dict:
            start_nodes = filter_dict[start_var]
        if final_var in filter_dict:
            final_nodes = filter_dict[final_var]

        # Execute query
        query = build_rsm(self._nfa_from_expr(ctx.expr()), nfa_dict)
        result = tensor_based_cfpq(query, graph, start_nodes, final_nodes)

        # Format output based on return variables
        ret_var1 = return_vars[0]
        ret_var2 = return_vars[1] if len(return_vars) > 1 else None

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
        if isinstance(val, LazyNFA):
            return val.get_value(self)
        if isinstance(val, EpsilonNFA):
            return val
        if isinstance(val, str):
            return nfa_from_char(val)
        raise Exception(f"Cannot convert '{val}' to EpsilonNFA")
