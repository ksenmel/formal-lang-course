from antlr4 import *

from project.parser.GQLParser import GQLParser
from project.parser.GQLVisitor import GQLVisitor

from project.parser.task11_parser import program_to_tree


class Memory:
    def __init__(self):
        self.tables = [{}]

    def add(self, name: str, value):
        self.tables[-1][name] = value

    def next_scope(self):
        new_table = Memory()
        new_table.tables = self.tables.copy()
        new_table.tables.append({})
        return new_table

    def remove_last(self):
        new_table = Memory()
        new_table.tables = self.tables.copy()
        new_table.tables = new_table.tables[:-1]
        return new_table

    def find(self, name: str):
        scope_level = len(self.tables) - 1
        while scope_level >= 0:
            value = self.tables[scope_level].get(name)
            if value is not None:
                return value
            scope_level -= 1
        raise Exception("ti dolboeb")


class MyVisitor(GQLVisitor):
    def __init__(self):
        self.env = Memory()

    def visitProg(self, ctx: ParserRuleContext):
        return self.visitChildren(ctx)

    def visitStmt(self, ctx: GQLParser.StmtContext):
        return self.visitChildren(ctx)

    def visitBind(self, ctx: GQLParser.BindContext):
        var_name = ctx.var().getText()
        value = self.visitChildren(ctx)
        self.env.add(var_name, value)

    def visitExpr(self, ctx: GQLParser.ExprContext):
        return self.visitChildren(ctx)

    def visitNum(self, ctx: GQLParser.NumContext):
        return int(ctx.NUM().getText())


def interpret(code: str):
    tree = program_to_tree(code)

    visitor = MyVisitor()
    visitor.visit(tree[0])

    return 0


if __name__ == '__main__':
    interp = interpret('let a = 15')
    print(interp)
