# Generated from project/parser/GQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GQLParser import GQLParser
else:
    from GQLParser import GQLParser

# This class defines a complete generic visitor for a parse tree produced by GQLParser.

class GQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GQLParser#prog.
    def visitProg(self, ctx:GQLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#stmt.
    def visitStmt(self, ctx:GQLParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#declare.
    def visitDeclare(self, ctx:GQLParser.DeclareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#bind.
    def visitBind(self, ctx:GQLParser.BindContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#remove.
    def visitRemove(self, ctx:GQLParser.RemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#add.
    def visitAdd(self, ctx:GQLParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#expr.
    def visitExpr(self, ctx:GQLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#set_expr.
    def visitSet_expr(self, ctx:GQLParser.Set_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#edge_expr.
    def visitEdge_expr(self, ctx:GQLParser.Edge_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#regexp.
    def visitRegexp(self, ctx:GQLParser.RegexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#range.
    def visitRange(self, ctx:GQLParser.RangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#select.
    def visitSelect(self, ctx:GQLParser.SelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#v_filter.
    def visitV_filter(self, ctx:GQLParser.V_filterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#num.
    def visitNum(self, ctx:GQLParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#char.
    def visitChar(self, ctx:GQLParser.CharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GQLParser#var.
    def visitVar(self, ctx:GQLParser.VarContext):
        return self.visitChildren(ctx)



del GQLParser