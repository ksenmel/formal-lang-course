from antlr4 import *

from project.parser.GQLParser import GQLParser
from project.parser.GQLVisitor import GQLVisitor

from project.parser.task11_parser import program_to_tree


class Environment:
    def __init__(self):
        self.env = [{}]

    def add(self, var: str, val):
        self.env[-1][var] = val

    def next_scope(self):
        new_env = Environment()
        new_env.env = self.env.copy()
        new_env.env.append({})
        return new_env

    def remove_last(self):
        new_env = Environment()
        new_env.env = self.env.copy()
        new_env.env = new_env.env[:-1]
        return new_env

    def find(self, name: str):
        scope_level = len(self.env) - 1
        while scope_level >= 0:
            value = self.env[scope_level].get(name)
            if value is not None:
                return value
            scope_level -= 1
        raise Exception(f"Unknown variable: {name}")


class MyVisitor(GQLVisitor):
    def __init__(self):
        self.env = Environment()

    def visitProg(self, ctx: ParserRuleContext):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx: GQLParser.StmtContext):
        return self.visitChildren(ctx)

    def visitExpr(self, ctx: GQLParser.ExprContext):
        return self.visitChildren(ctx)

    def visitBind(self, ctx: GQLParser.BindContext):
        var_name = ctx.var().getText()
        value = self.visit(ctx.expr())
        # value = self.visitExpr(ctx.expr())
        self.env.add(var_name, value)

    def visitNum(self, ctx: GQLParser.NumContext):
        return int(ctx.NUM().getText())

    def visitChar(self, ctx: GQLParser.CharContext):
        return str(ctx.CHAR().getText()[1])

    def visitVar(self, ctx: GQLParser.VarContext):
        var_name = ctx.VAR().getText()
        return self.env.find(var_name)

    def visitSet_expr(self, ctx: GQLParser.Set_exprContext):
        values = set()
        for expr_ctx in ctx.expr():
            value = self.visit(expr_ctx)
            values.add(value)

        return values

    def visitRange(self, ctx: GQLParser.RangeContext):
        # Начальное число (обязательно)
        start = int(ctx.num(0))

        if ctx.num(1):
            end = int(ctx.num(1))
            return range(start, end)
            # return range(start, end + 1)???
        else:
            return range(start, float('inf'))


def interpret(code: str):
    tree = program_to_tree(code)

    visitor = MyVisitor()
    visitor.visit(tree[0])

    return 0


if __name__ == '__main__':
    interp = interpret('let b = 1 let a = b let c = [1,2]')
    print(interp)
