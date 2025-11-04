# Generated from project/parser/GQL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,31,162,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,1,1,1,1,1,
        1,1,3,1,43,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,3,6,74,8,6,1,7,1,7,1,7,1,7,5,7,80,8,7,10,7,12,7,83,9,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,
        102,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,116,
        8,9,10,9,12,9,119,9,9,1,10,1,10,1,10,1,10,3,10,125,8,10,1,10,1,10,
        1,11,3,11,130,8,11,1,11,3,11,133,8,11,1,11,1,11,1,11,1,11,3,11,139,
        8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,0,1,18,16,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,1,0,9,11,1,0,9,10,166,
        0,35,1,0,0,0,2,42,1,0,0,0,4,44,1,0,0,0,6,49,1,0,0,0,8,54,1,0,0,0,
        10,60,1,0,0,0,12,73,1,0,0,0,14,75,1,0,0,0,16,86,1,0,0,0,18,101,1,
        0,0,0,20,120,1,0,0,0,22,129,1,0,0,0,24,150,1,0,0,0,26,155,1,0,0,
        0,28,157,1,0,0,0,30,159,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,37,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,1,1,0,0,0,37,35,1,0,0,0,38,
        43,3,4,2,0,39,43,3,6,3,0,40,43,3,10,5,0,41,43,3,8,4,0,42,38,1,0,
        0,0,42,39,1,0,0,0,42,40,1,0,0,0,42,41,1,0,0,0,43,3,1,0,0,0,44,45,
        5,1,0,0,45,46,3,30,15,0,46,47,5,2,0,0,47,48,5,3,0,0,48,5,1,0,0,0,
        49,50,5,1,0,0,50,51,3,30,15,0,51,52,5,17,0,0,52,53,3,12,6,0,53,7,
        1,0,0,0,54,55,5,4,0,0,55,56,7,0,0,0,56,57,3,12,6,0,57,58,5,12,0,
        0,58,59,3,30,15,0,59,9,1,0,0,0,60,61,5,13,0,0,61,62,7,1,0,0,62,63,
        3,12,6,0,63,64,5,14,0,0,64,65,3,30,15,0,65,11,1,0,0,0,66,74,3,26,
        13,0,67,74,3,28,14,0,68,74,3,30,15,0,69,74,3,16,8,0,70,74,3,14,7,
        0,71,74,3,18,9,0,72,74,3,22,11,0,73,66,1,0,0,0,73,67,1,0,0,0,73,
        68,1,0,0,0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,
        0,74,13,1,0,0,0,75,76,5,18,0,0,76,81,3,12,6,0,77,78,5,22,0,0,78,
        80,3,12,6,0,79,77,1,0,0,0,80,83,1,0,0,0,81,79,1,0,0,0,81,82,1,0,
        0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,20,0,0,85,15,1,0,0,0,86,
        87,5,19,0,0,87,88,3,12,6,0,88,89,5,22,0,0,89,90,3,12,6,0,90,91,5,
        22,0,0,91,92,3,12,6,0,92,93,5,21,0,0,93,17,1,0,0,0,94,95,6,9,-1,
        0,95,102,3,28,14,0,96,102,3,30,15,0,97,98,5,19,0,0,98,99,3,18,9,
        0,99,100,5,21,0,0,100,102,1,0,0,0,101,94,1,0,0,0,101,96,1,0,0,0,
        101,97,1,0,0,0,102,117,1,0,0,0,103,104,10,3,0,0,104,105,5,24,0,0,
        105,116,3,18,9,4,106,107,10,2,0,0,107,108,5,27,0,0,108,116,3,18,
        9,3,109,110,10,1,0,0,110,111,5,25,0,0,111,116,3,18,9,2,112,113,10,
        4,0,0,113,114,5,23,0,0,114,116,3,20,10,0,115,103,1,0,0,0,115,106,
        1,0,0,0,115,109,1,0,0,0,115,112,1,0,0,0,116,119,1,0,0,0,117,115,
        1,0,0,0,117,118,1,0,0,0,118,19,1,0,0,0,119,117,1,0,0,0,120,121,5,
        18,0,0,121,122,3,26,13,0,122,124,5,26,0,0,123,125,3,26,13,0,124,
        123,1,0,0,0,124,125,1,0,0,0,125,126,1,0,0,0,126,127,5,20,0,0,127,
        21,1,0,0,0,128,130,3,24,12,0,129,128,1,0,0,0,129,130,1,0,0,0,130,
        132,1,0,0,0,131,133,3,24,12,0,132,131,1,0,0,0,132,133,1,0,0,0,133,
        134,1,0,0,0,134,135,5,7,0,0,135,138,3,30,15,0,136,137,5,22,0,0,137,
        139,3,30,15,0,138,136,1,0,0,0,138,139,1,0,0,0,139,140,1,0,0,0,140,
        141,5,5,0,0,141,142,3,30,15,0,142,143,5,6,0,0,143,144,5,12,0,0,144,
        145,3,30,15,0,145,146,5,16,0,0,146,147,3,30,15,0,147,148,5,8,0,0,
        148,149,3,12,6,0,149,23,1,0,0,0,150,151,5,15,0,0,151,152,3,30,15,
        0,152,153,5,16,0,0,153,154,3,12,6,0,154,25,1,0,0,0,155,156,5,29,
        0,0,156,27,1,0,0,0,157,158,5,30,0,0,158,29,1,0,0,0,159,160,5,28,
        0,0,160,31,1,0,0,0,11,35,42,73,81,101,115,117,124,129,132,138
    ]

class GQLParser ( Parser ):

    grammarFileName = "GQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'is'", "'graph'", "'remove'", 
                     "'where'", "'reachable'", "'return'", "'by'", "'vertex'", 
                     "'edge'", "'vertices'", "'from'", "'add'", "'to'", 
                     "'for'", "'in'", "'='", "'['", "'('", "']'", "')'", 
                     "','", "'^'", "'.'", "'&'", "'..'", "'|'" ]

    symbolicNames = [ "<INVALID>", "LET", "IS", "GRAPH", "REMOVE", "WHERE", 
                      "REACHABLE", "RETURN", "BY", "VERTEX", "EDGE", "VERTICES", 
                      "FROM", "ADD", "TO", "FOR", "IN", "EQUAL", "L_SQ_BR", 
                      "L_BR", "R_SQ_BR", "R_BR", "COMMA", "CIRCUMFLEX", 
                      "DOT", "AMPERSAND", "ELLIPSIS", "PIPE", "VAR", "NUM", 
                      "CHAR", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_declare = 2
    RULE_bind = 3
    RULE_remove = 4
    RULE_add = 5
    RULE_expr = 6
    RULE_set_expr = 7
    RULE_edge_expr = 8
    RULE_regexp = 9
    RULE_range = 10
    RULE_select = 11
    RULE_v_filter = 12
    RULE_num = 13
    RULE_char = 14
    RULE_var = 15

    ruleNames =  [ "prog", "stmt", "declare", "bind", "remove", "add", "expr", 
                   "set_expr", "edge_expr", "regexp", "range", "select", 
                   "v_filter", "num", "char", "var" ]

    EOF = Token.EOF
    LET=1
    IS=2
    GRAPH=3
    REMOVE=4
    WHERE=5
    REACHABLE=6
    RETURN=7
    BY=8
    VERTEX=9
    EDGE=10
    VERTICES=11
    FROM=12
    ADD=13
    TO=14
    FOR=15
    IN=16
    EQUAL=17
    L_SQ_BR=18
    L_BR=19
    R_SQ_BR=20
    R_BR=21
    COMMA=22
    CIRCUMFLEX=23
    DOT=24
    AMPERSAND=25
    ELLIPSIS=26
    PIPE=27
    VAR=28
    NUM=29
    CHAR=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GQLParser.StmtContext)
            else:
                return self.getTypedRuleContext(GQLParser.StmtContext,i)


        def getRuleIndex(self):
            return GQLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = GQLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8210) != 0):
                self.state = 32
                self.stmt()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare(self):
            return self.getTypedRuleContext(GQLParser.DeclareContext,0)


        def bind(self):
            return self.getTypedRuleContext(GQLParser.BindContext,0)


        def add(self):
            return self.getTypedRuleContext(GQLParser.AddContext,0)


        def remove(self):
            return self.getTypedRuleContext(GQLParser.RemoveContext,0)


        def getRuleIndex(self):
            return GQLParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = GQLParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.declare()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.bind()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.add()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.remove()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(GQLParser.LET, 0)

        def var(self):
            return self.getTypedRuleContext(GQLParser.VarContext,0)


        def IS(self):
            return self.getToken(GQLParser.IS, 0)

        def GRAPH(self):
            return self.getToken(GQLParser.GRAPH, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_declare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclare" ):
                listener.enterDeclare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclare" ):
                listener.exitDeclare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare" ):
                return visitor.visitDeclare(self)
            else:
                return visitor.visitChildren(self)




    def declare(self):

        localctx = GQLParser.DeclareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(GQLParser.LET)
            self.state = 45
            self.var()
            self.state = 46
            self.match(GQLParser.IS)
            self.state = 47
            self.match(GQLParser.GRAPH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(GQLParser.LET, 0)

        def var(self):
            return self.getTypedRuleContext(GQLParser.VarContext,0)


        def EQUAL(self):
            return self.getToken(GQLParser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(GQLParser.ExprContext,0)


        def getRuleIndex(self):
            return GQLParser.RULE_bind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBind" ):
                listener.enterBind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBind" ):
                listener.exitBind(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBind" ):
                return visitor.visitBind(self)
            else:
                return visitor.visitChildren(self)




    def bind(self):

        localctx = GQLParser.BindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(GQLParser.LET)
            self.state = 50
            self.var()
            self.state = 51
            self.match(GQLParser.EQUAL)
            self.state = 52
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RemoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REMOVE(self):
            return self.getToken(GQLParser.REMOVE, 0)

        def expr(self):
            return self.getTypedRuleContext(GQLParser.ExprContext,0)


        def FROM(self):
            return self.getToken(GQLParser.FROM, 0)

        def var(self):
            return self.getTypedRuleContext(GQLParser.VarContext,0)


        def VERTEX(self):
            return self.getToken(GQLParser.VERTEX, 0)

        def EDGE(self):
            return self.getToken(GQLParser.EDGE, 0)

        def VERTICES(self):
            return self.getToken(GQLParser.VERTICES, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_remove

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove" ):
                listener.enterRemove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove" ):
                listener.exitRemove(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemove" ):
                return visitor.visitRemove(self)
            else:
                return visitor.visitChildren(self)




    def remove(self):

        localctx = GQLParser.RemoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_remove)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(GQLParser.REMOVE)
            self.state = 55
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3584) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 56
            self.expr()
            self.state = 57
            self.match(GQLParser.FROM)
            self.state = 58
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(GQLParser.ADD, 0)

        def expr(self):
            return self.getTypedRuleContext(GQLParser.ExprContext,0)


        def TO(self):
            return self.getToken(GQLParser.TO, 0)

        def var(self):
            return self.getTypedRuleContext(GQLParser.VarContext,0)


        def VERTEX(self):
            return self.getToken(GQLParser.VERTEX, 0)

        def EDGE(self):
            return self.getToken(GQLParser.EDGE, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = GQLParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_add)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(GQLParser.ADD)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self.expr()
            self.state = 63
            self.match(GQLParser.TO)
            self.state = 64
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def num(self):
            return self.getTypedRuleContext(GQLParser.NumContext,0)


        def char(self):
            return self.getTypedRuleContext(GQLParser.CharContext,0)


        def var(self):
            return self.getTypedRuleContext(GQLParser.VarContext,0)


        def edge_expr(self):
            return self.getTypedRuleContext(GQLParser.Edge_exprContext,0)


        def set_expr(self):
            return self.getTypedRuleContext(GQLParser.Set_exprContext,0)


        def regexp(self):
            return self.getTypedRuleContext(GQLParser.RegexpContext,0)


        def select(self):
            return self.getTypedRuleContext(GQLParser.SelectContext,0)


        def getRuleIndex(self):
            return GQLParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = GQLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.num()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.char()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.var()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.edge_expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.set_expr()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.regexp(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 72
                self.select()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Set_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_SQ_BR(self):
            return self.getToken(GQLParser.L_SQ_BR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(GQLParser.ExprContext,i)


        def R_SQ_BR(self):
            return self.getToken(GQLParser.R_SQ_BR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GQLParser.COMMA)
            else:
                return self.getToken(GQLParser.COMMA, i)

        def getRuleIndex(self):
            return GQLParser.RULE_set_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSet_expr" ):
                listener.enterSet_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSet_expr" ):
                listener.exitSet_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSet_expr" ):
                return visitor.visitSet_expr(self)
            else:
                return visitor.visitChildren(self)




    def set_expr(self):

        localctx = GQLParser.Set_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_set_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(GQLParser.L_SQ_BR)
            self.state = 76
            self.expr()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 77
                self.match(GQLParser.COMMA)
                self.state = 78
                self.expr()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(GQLParser.R_SQ_BR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Edge_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BR(self):
            return self.getToken(GQLParser.L_BR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GQLParser.ExprContext)
            else:
                return self.getTypedRuleContext(GQLParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GQLParser.COMMA)
            else:
                return self.getToken(GQLParser.COMMA, i)

        def R_BR(self):
            return self.getToken(GQLParser.R_BR, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_edge_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEdge_expr" ):
                listener.enterEdge_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEdge_expr" ):
                listener.exitEdge_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdge_expr" ):
                return visitor.visitEdge_expr(self)
            else:
                return visitor.visitChildren(self)




    def edge_expr(self):

        localctx = GQLParser.Edge_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_edge_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(GQLParser.L_BR)
            self.state = 87
            self.expr()
            self.state = 88
            self.match(GQLParser.COMMA)
            self.state = 89
            self.expr()
            self.state = 90
            self.match(GQLParser.COMMA)
            self.state = 91
            self.expr()
            self.state = 92
            self.match(GQLParser.R_BR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def char(self):
            return self.getTypedRuleContext(GQLParser.CharContext,0)


        def var(self):
            return self.getTypedRuleContext(GQLParser.VarContext,0)


        def L_BR(self):
            return self.getToken(GQLParser.L_BR, 0)

        def regexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GQLParser.RegexpContext)
            else:
                return self.getTypedRuleContext(GQLParser.RegexpContext,i)


        def R_BR(self):
            return self.getToken(GQLParser.R_BR, 0)

        def DOT(self):
            return self.getToken(GQLParser.DOT, 0)

        def PIPE(self):
            return self.getToken(GQLParser.PIPE, 0)

        def AMPERSAND(self):
            return self.getToken(GQLParser.AMPERSAND, 0)

        def CIRCUMFLEX(self):
            return self.getToken(GQLParser.CIRCUMFLEX, 0)

        def range_(self):
            return self.getTypedRuleContext(GQLParser.RangeContext,0)


        def getRuleIndex(self):
            return GQLParser.RULE_regexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegexp" ):
                listener.enterRegexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegexp" ):
                listener.exitRegexp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegexp" ):
                return visitor.visitRegexp(self)
            else:
                return visitor.visitChildren(self)



    def regexp(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GQLParser.RegexpContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_regexp, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30]:
                self.state = 95
                self.char()
                pass
            elif token in [28]:
                self.state = 96
                self.var()
                pass
            elif token in [19]:
                self.state = 97
                self.match(GQLParser.L_BR)
                self.state = 98
                self.regexp(0)
                self.state = 99
                self.match(GQLParser.R_BR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 115
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = GQLParser.RegexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regexp)
                        self.state = 103
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 104
                        self.match(GQLParser.DOT)
                        self.state = 105
                        self.regexp(4)
                        pass

                    elif la_ == 2:
                        localctx = GQLParser.RegexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regexp)
                        self.state = 106
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 107
                        self.match(GQLParser.PIPE)
                        self.state = 108
                        self.regexp(3)
                        pass

                    elif la_ == 3:
                        localctx = GQLParser.RegexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regexp)
                        self.state = 109
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 110
                        self.match(GQLParser.AMPERSAND)
                        self.state = 111
                        self.regexp(2)
                        pass

                    elif la_ == 4:
                        localctx = GQLParser.RegexpContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_regexp)
                        self.state = 112
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 113
                        self.match(GQLParser.CIRCUMFLEX)
                        self.state = 114
                        self.range_()
                        pass

             
                self.state = 119
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class RangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_SQ_BR(self):
            return self.getToken(GQLParser.L_SQ_BR, 0)

        def num(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GQLParser.NumContext)
            else:
                return self.getTypedRuleContext(GQLParser.NumContext,i)


        def ELLIPSIS(self):
            return self.getToken(GQLParser.ELLIPSIS, 0)

        def R_SQ_BR(self):
            return self.getToken(GQLParser.R_SQ_BR, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_range

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRange" ):
                listener.enterRange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRange" ):
                listener.exitRange(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange" ):
                return visitor.visitRange(self)
            else:
                return visitor.visitChildren(self)




    def range_(self):

        localctx = GQLParser.RangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_range)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(GQLParser.L_SQ_BR)
            self.state = 121
            self.num()
            self.state = 122
            self.match(GQLParser.ELLIPSIS)
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 123
                self.num()


            self.state = 126
            self.match(GQLParser.R_SQ_BR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(GQLParser.RETURN, 0)

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GQLParser.VarContext)
            else:
                return self.getTypedRuleContext(GQLParser.VarContext,i)


        def WHERE(self):
            return self.getToken(GQLParser.WHERE, 0)

        def REACHABLE(self):
            return self.getToken(GQLParser.REACHABLE, 0)

        def FROM(self):
            return self.getToken(GQLParser.FROM, 0)

        def IN(self):
            return self.getToken(GQLParser.IN, 0)

        def BY(self):
            return self.getToken(GQLParser.BY, 0)

        def expr(self):
            return self.getTypedRuleContext(GQLParser.ExprContext,0)


        def v_filter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GQLParser.V_filterContext)
            else:
                return self.getTypedRuleContext(GQLParser.V_filterContext,i)


        def COMMA(self):
            return self.getToken(GQLParser.COMMA, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelect" ):
                return visitor.visitSelect(self)
            else:
                return visitor.visitChildren(self)




    def select(self):

        localctx = GQLParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 128
                self.v_filter()


            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 131
                self.v_filter()


            self.state = 134
            self.match(GQLParser.RETURN)
            self.state = 135
            self.var()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 136
                self.match(GQLParser.COMMA)
                self.state = 137
                self.var()


            self.state = 140
            self.match(GQLParser.WHERE)
            self.state = 141
            self.var()
            self.state = 142
            self.match(GQLParser.REACHABLE)
            self.state = 143
            self.match(GQLParser.FROM)
            self.state = 144
            self.var()
            self.state = 145
            self.match(GQLParser.IN)
            self.state = 146
            self.var()
            self.state = 147
            self.match(GQLParser.BY)
            self.state = 148
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V_filterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GQLParser.FOR, 0)

        def var(self):
            return self.getTypedRuleContext(GQLParser.VarContext,0)


        def IN(self):
            return self.getToken(GQLParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(GQLParser.ExprContext,0)


        def getRuleIndex(self):
            return GQLParser.RULE_v_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_filter" ):
                listener.enterV_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_filter" ):
                listener.exitV_filter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitV_filter" ):
                return visitor.visitV_filter(self)
            else:
                return visitor.visitChildren(self)




    def v_filter(self):

        localctx = GQLParser.V_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_v_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(GQLParser.FOR)
            self.state = 151
            self.var()
            self.state = 152
            self.match(GQLParser.IN)
            self.state = 153
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(GQLParser.NUM, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)




    def num(self):

        localctx = GQLParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(GQLParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(GQLParser.CHAR, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_char

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChar" ):
                listener.enterChar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChar" ):
                listener.exitChar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChar" ):
                return visitor.visitChar(self)
            else:
                return visitor.visitChildren(self)




    def char(self):

        localctx = GQLParser.CharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_char)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(GQLParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(GQLParser.VAR, 0)

        def getRuleIndex(self):
            return GQLParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = GQLParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(GQLParser.VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.regexp_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def regexp_sempred(self, localctx:RegexpContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




