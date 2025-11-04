from project.parser.GQLVisitor import GQLVisitor
from project.interpreter.visitor import get_varname
from project.typecheck.exceptions import (
    InvalidType,
    TypeMismatch,
    VariableNotFoundException,
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
        self.current_binding = None

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
        self.current_binding = var_name

        expr_type = self.visitExpr(ctx.expr())
        self.current_binding = None
        self.env.add(var_name, expr_type)

    # New regexp hierarchy methods for updated grammar
    def visitRegexp(self, ctx):
        regexp_and_list = ctx.regexp_and()
        result_type = self.visitRegexp_and(regexp_and_list[0])

        for i in range(1, len(regexp_and_list)):
            right_type = self.visitRegexp_and(regexp_and_list[i])
            result_type = (
                Types.RSM if Types.RSM in [result_type, right_type] else Types.FA
            )

        return result_type

    def visitRegexp_and(self, ctx):
        regexp_concat_list = ctx.regexp_concat()
        result_type = self.visitRegexp_concat(regexp_concat_list[0])

        for i in range(1, len(regexp_concat_list)):
            right_type = self.visitRegexp_concat(regexp_concat_list[i])
            if result_type == Types.RSM and right_type == Types.RSM:
                raise Exception("Cannot intersect two RSMs")
            result_type = (
                Types.RSM if Types.RSM in [result_type, right_type] else Types.FA
            )

        return result_type

    def visitRegexp_concat(self, ctx):
        regexp_power_list = ctx.regexp_power()
        result_type = self.visitRegexp_power(regexp_power_list[0])

        for i in range(1, len(regexp_power_list)):
            right_type = self.visitRegexp_power(regexp_power_list[i])
            result_type = (
                Types.RSM if Types.RSM in [result_type, right_type] else Types.FA
            )

        return result_type

    def visitRegexp_power(self, ctx):
        result_type = self.visitRegexp_primary(ctx.regexp_primary())

        range_list = ctx.range_()
        for range_ctx in range_list:
            range_type = self.visitRange(range_ctx)
            check_type(Types.RANGE, range_type)

            if result_type not in [Types.FA, Types.RSM]:
                raise Exception(f"Invalid type {result_type} for repeat operation")

        return result_type

    def visitRegexp_primary(self, ctx):
        if ctx.char():
            return Types.FA

        if ctx.var():
            var_name = get_varname(ctx.var())
            if var_name == self.current_binding:
                return Types.RSM

            if not self.env.contain_variable(var_name):
                return Types.FA

            var_type = self.visitVar(ctx.var())

            if var_type == Types.FA or var_type == Types.CHAR:
                return Types.FA
            if var_type == Types.RSM:
                return Types.RSM
            raise Exception(
                f"Invalid type {var_type} for variable {var_name} in regexp"
            )

        if ctx.L_BR() and ctx.R_BR():
            return self.visitRegexp(ctx.regexp())

        return Types.INVALID

    def visitSelect(self, ctx):
        for i in range(len(ctx.v_filter())):
            self.visitV_filter(ctx.v_filter(i))

        vars = ctx.var()

        if ctx.COMMA():
            result_var2 = vars[1].getText()
            var_offset = 2
        else:
            result_var2 = None
            var_offset = 1

        in_var = vars[var_offset + 2].getText()
        check_type(Types.GRAPH, self.env.get(in_var))

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
