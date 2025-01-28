from project.parser.GQLVisitor import GQLVisitor
from project.interpreter.visitor import get_varname
from project.typeinference.exceptions import (
    InvalidType,
    TypeMismatch,
    VariableNotFoundException,
    UnsupportedOperation,
    VariableAlreadyExists,
    UnsupportedConstruction,
)


class Types:
    EDGE = "edge"
    GRAPH = "graph"
    FA = "FA"
    RSM = "RSM"
    RANGE = "RANGE"
    NUM = "num"
    CHAR = "char"
    SET = "SET<a>"
    PAIR_SET = "SET<a * a>"
    INVALID = "ERROR"


class Env:
    def __init__(self):
        self.var_types = {}

    def add(self, name: str, typ: Types):
        if typ == Types.INVALID:
            raise InvalidType
        self.var_types[name] = typ

    def get(self, name: str):
        return self.var_types[name]

    def contain_variable(self, name: str):
        return name in self.var_types.keys()


def check_type(expected, actual):
    if expected != actual:
        raise TypeMismatch(expected, actual)


class GQLInfer(GQLVisitor):
    def __init__(self):
        self.env = Env()

    def visitProg(self, ctx):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx):
        return self.visitChildren(ctx)

    def visitDeclare(self, ctx):
        name = get_varname(ctx.var())
        self.env.add(name, Types.GRAPH)

    def visitExpr(self, ctx):
        return self.visitChildren(ctx)

    def visitBind(self, ctx):
        var_name = get_varname(ctx.var())
        expr_type = self.visitExpr(ctx.expr())
        self.env.add(var_name, expr_type)

    def visitRegexp(self, ctx):
        if ctx.char():
            return Types.FA
        if ctx.var():
            return self._handle_var(ctx)
        if ctx.L_BR() and ctx.R_BR():
            return self._handle_brackets(ctx)
        if ctx.CIRCUMFLEX():
            return self._handle_circumflex(ctx)
        if ctx.PIPE() or ctx.DOT() or ctx.AMPERSAND():
            return self._handle_binop(ctx)

        return Types.INVALID

    def _handle_var(self, ctx):
        var_name = get_varname(ctx.var())
        if not self.env.contain_variable(var_name):
            return Types.RSM

        var_type = self.visitVar(ctx.var())

        if var_type == Types.FA or var_type == Types.CHAR:
            return Types.FA
        if var_type == Types.RSM:
            return Types.RSM
        raise Exception(f"Invalid type {var_type} for variable {var_name} in regexp")

    def _handle_brackets(self, ctx):
        return self.visitRegexp(ctx.regexp(0))

    def _handle_circumflex(self, ctx):
        left_type = self.visitRegexp(ctx.regexp(0))
        range_type = self.visitRange(ctx.range_())
        check_type(Types.RANGE, range_type)

        if left_type not in [Types.FA, Types.RSM]:
            raise Exception(f"Invalid type {left_type} for repeat operation")
        return left_type

    def _handle_binop(self, ctx):
        left_type = self.visitRegexp(ctx.regexp(0))
        right_type = self.visitRegexp(ctx.regexp(1))
        if ctx.PIPE() or ctx.DOT():
            return Types.RSM if Types.RSM in [left_type, right_type] else Types.FA
        if ctx.AMPERSAND():
            if left_type == Types.RSM and right_type == Types.RSM:
                raise Exception("Cannot intersect two RSMs")
            return Types.RSM if Types.RSM in [left_type, right_type] else Types.FA

        raise UnsupportedOperation

    def visitSelect(self, ctx):
        self.visitV_filter(ctx.v_filter(0))
        self.visitV_filter(ctx.v_filter(1))

        vars = ctx.var()
        in_var = vars[-1].getText()

        check_type(Types.GRAPH, self.env.get(in_var))

        result_var2 = vars[1].getText() if ctx.COMMA() else None

        expr_type = self.visitExpr(ctx.expr())
        if expr_type not in [Types.FA, Types.RSM, Types.CHAR]:
            raise Exception(f"Invalid expression type {expr_type} in SELECT")

        return Types.PAIR_SET if result_var2 else Types.SET

    def visitAdd(self, ctx):
        var_type = self.visitVar(ctx.var())
        check_type(Types.GRAPH, var_type)

        entity_type = self.visitExpr(ctx.expr())

        if ctx.EDGE():
            check_type(Types.EDGE, entity_type)
        elif ctx.VERTEX():
            check_type(Types.NUM, entity_type)

    def visitRemove(self, ctx):
        var_type = self.visitVar(ctx.var())
        check_type(Types.GRAPH, var_type)

        entity_type = self.visitExpr(ctx.expr())

        if ctx.EDGE():
            check_type(Types.EDGE, entity_type)
        elif ctx.VERTEX():
            check_type(Types.NUM, entity_type)
        elif ctx.VERTICES():
            check_type(Types.SET, entity_type)

    def visitV_filter(self, ctx):
        if not ctx:
            return None

        var_name = get_varname(ctx.var())
        if self.env.contain_variable(var_name):
            raise VariableAlreadyExists

        expr_type = self.visitExpr(ctx.expr())
        check_type(Types.SET, expr_type)

        return var_name

    def visitSet_expr(self, ctx):
        for expr in ctx.expr():
            check_type(Types.NUM, self.visitExpr(expr))
        return Types.SET

    def visitEdge_expr(self, ctx):
        exprs = ctx.expr()
        types = [self.visitExpr(e) for e in exprs]

        if types[0] == Types.NUM and types[1] == Types.CHAR and types[2] == Types.NUM:
            return Types.EDGE

        raise UnsupportedConstruction(ctx.getText())

    def visitRange(self, ctx):
        return Types.RANGE

    def visitNum(self, ctx):
        return Types.NUM

    def visitChar(self, ctx):
        return Types.CHAR

    def visitVar(self, ctx):
        var_name = ctx.VAR().getText()
        if not self.env.contain_variable(var_name):
            raise VariableNotFoundException
        return self.env.get(var_name)
