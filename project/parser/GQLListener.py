# Generated from project/parser/GQL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GQLParser import GQLParser
else:
    from GQLParser import GQLParser

# This class defines a complete listener for a parse tree produced by GQLParser.
class GQLListener(ParseTreeListener):

    # Enter a parse tree produced by GQLParser#prog.
    def enterProg(self, ctx:GQLParser.ProgContext):
        pass

    # Exit a parse tree produced by GQLParser#prog.
    def exitProg(self, ctx:GQLParser.ProgContext):
        pass


    # Enter a parse tree produced by GQLParser#stmt.
    def enterStmt(self, ctx:GQLParser.StmtContext):
        pass

    # Exit a parse tree produced by GQLParser#stmt.
    def exitStmt(self, ctx:GQLParser.StmtContext):
        pass


    # Enter a parse tree produced by GQLParser#declare.
    def enterDeclare(self, ctx:GQLParser.DeclareContext):
        pass

    # Exit a parse tree produced by GQLParser#declare.
    def exitDeclare(self, ctx:GQLParser.DeclareContext):
        pass


    # Enter a parse tree produced by GQLParser#bind.
    def enterBind(self, ctx:GQLParser.BindContext):
        pass

    # Exit a parse tree produced by GQLParser#bind.
    def exitBind(self, ctx:GQLParser.BindContext):
        pass


    # Enter a parse tree produced by GQLParser#remove.
    def enterRemove(self, ctx:GQLParser.RemoveContext):
        pass

    # Exit a parse tree produced by GQLParser#remove.
    def exitRemove(self, ctx:GQLParser.RemoveContext):
        pass


    # Enter a parse tree produced by GQLParser#add.
    def enterAdd(self, ctx:GQLParser.AddContext):
        pass

    # Exit a parse tree produced by GQLParser#add.
    def exitAdd(self, ctx:GQLParser.AddContext):
        pass


    # Enter a parse tree produced by GQLParser#expr.
    def enterExpr(self, ctx:GQLParser.ExprContext):
        pass

    # Exit a parse tree produced by GQLParser#expr.
    def exitExpr(self, ctx:GQLParser.ExprContext):
        pass


    # Enter a parse tree produced by GQLParser#set_expr.
    def enterSet_expr(self, ctx:GQLParser.Set_exprContext):
        pass

    # Exit a parse tree produced by GQLParser#set_expr.
    def exitSet_expr(self, ctx:GQLParser.Set_exprContext):
        pass


    # Enter a parse tree produced by GQLParser#edge_expr.
    def enterEdge_expr(self, ctx:GQLParser.Edge_exprContext):
        pass

    # Exit a parse tree produced by GQLParser#edge_expr.
    def exitEdge_expr(self, ctx:GQLParser.Edge_exprContext):
        pass


    # Enter a parse tree produced by GQLParser#regexp.
    def enterRegexp(self, ctx:GQLParser.RegexpContext):
        pass

    # Exit a parse tree produced by GQLParser#regexp.
    def exitRegexp(self, ctx:GQLParser.RegexpContext):
        pass


    # Enter a parse tree produced by GQLParser#range.
    def enterRange(self, ctx:GQLParser.RangeContext):
        pass

    # Exit a parse tree produced by GQLParser#range.
    def exitRange(self, ctx:GQLParser.RangeContext):
        pass


    # Enter a parse tree produced by GQLParser#select.
    def enterSelect(self, ctx:GQLParser.SelectContext):
        pass

    # Exit a parse tree produced by GQLParser#select.
    def exitSelect(self, ctx:GQLParser.SelectContext):
        pass


    # Enter a parse tree produced by GQLParser#v_filter.
    def enterV_filter(self, ctx:GQLParser.V_filterContext):
        pass

    # Exit a parse tree produced by GQLParser#v_filter.
    def exitV_filter(self, ctx:GQLParser.V_filterContext):
        pass


    # Enter a parse tree produced by GQLParser#num.
    def enterNum(self, ctx:GQLParser.NumContext):
        pass

    # Exit a parse tree produced by GQLParser#num.
    def exitNum(self, ctx:GQLParser.NumContext):
        pass


    # Enter a parse tree produced by GQLParser#char.
    def enterChar(self, ctx:GQLParser.CharContext):
        pass

    # Exit a parse tree produced by GQLParser#char.
    def exitChar(self, ctx:GQLParser.CharContext):
        pass


    # Enter a parse tree produced by GQLParser#var.
    def enterVar(self, ctx:GQLParser.VarContext):
        pass

    # Exit a parse tree produced by GQLParser#var.
    def exitVar(self, ctx:GQLParser.VarContext):
        pass



del GQLParser