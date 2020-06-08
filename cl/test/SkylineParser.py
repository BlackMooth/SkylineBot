# Generated from Skyline.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\64\n")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("B\n\4\f\4\16\4E\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5V\n\5\3\5\2\3\6\6\2\4\6")
        buf.write("\b\2\2\2_\2\13\3\2\2\2\4\23\3\2\2\2\6\63\3\2\2\2\bU\3")
        buf.write("\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2")
        buf.write("\2\r\16\3\2\2\2\16\3\3\2\2\2\17\24\5\6\4\2\20\21\7\17")
        buf.write("\2\2\21\22\7\3\2\2\22\24\5\6\4\2\23\17\3\2\2\2\23\20\3")
        buf.write("\2\2\2\24\5\3\2\2\2\25\26\b\4\1\2\26\27\7\4\2\2\27\30")
        buf.write("\5\6\4\2\30\31\7\5\2\2\31\64\3\2\2\2\32\33\7\6\2\2\33")
        buf.write("\64\5\6\4\13\34\35\7\4\2\2\35\36\7\20\2\2\36\37\7\7\2")
        buf.write("\2\37 \7\20\2\2 !\7\7\2\2!\"\7\20\2\2\"\64\7\5\2\2#$\7")
        buf.write("\b\2\2$%\5\b\5\2%&\7\t\2\2&\64\3\2\2\2\'(\7\n\2\2()\7")
        buf.write("\20\2\2)*\7\7\2\2*+\7\20\2\2+,\7\7\2\2,-\7\20\2\2-.\7")
        buf.write("\7\2\2./\7\20\2\2/\60\7\7\2\2\60\61\7\20\2\2\61\64\7\13")
        buf.write("\2\2\62\64\7\17\2\2\63\25\3\2\2\2\63\32\3\2\2\2\63\34")
        buf.write("\3\2\2\2\63#\3\2\2\2\63\'\3\2\2\2\63\62\3\2\2\2\64C\3")
        buf.write("\2\2\2\65\66\f\n\2\2\66\67\7\16\2\2\67B\5\6\4\1389\f\b")
        buf.write("\2\29:\7\r\2\2:B\5\6\4\t;<\f\t\2\2<=\7\16\2\2=B\7\20\2")
        buf.write("\2>?\f\7\2\2?@\7\r\2\2@B\7\20\2\2A\65\3\2\2\2A8\3\2\2")
        buf.write("\2A;\3\2\2\2A>\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D")
        buf.write("\7\3\2\2\2EC\3\2\2\2FG\7\4\2\2GH\7\20\2\2HI\7\7\2\2IJ")
        buf.write("\7\20\2\2JK\7\7\2\2KL\7\20\2\2LM\7\f\2\2MV\5\b\5\2NO\7")
        buf.write("\4\2\2OP\7\20\2\2PQ\7\7\2\2QR\7\20\2\2RS\7\7\2\2ST\7\20")
        buf.write("\2\2TV\7\5\2\2UF\3\2\2\2UN\3\2\2\2V\t\3\2\2\2\b\r\23\63")
        buf.write("ACU")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "'('", "')'", "'-'", "','", "'['", 
                     "']'", "'{'", "'}'", "'),'", "'+'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "PLUS", "ESTRELLA", 
                      "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_skyline = 2
    RULE_skyline_sets = 3

    ruleNames =  [ "prog", "stat", "skyline", "skyline_sets" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    PLUS=11
    ESTRELLA=12
    ID=13
    INT=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.StatContext)
            else:
                return self.getTypedRuleContext(SkylineParser.StatContext,i)


        def getRuleIndex(self):
            return SkylineParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = SkylineParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.stat()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SkylineParser.T__1) | (1 << SkylineParser.T__3) | (1 << SkylineParser.T__5) | (1 << SkylineParser.T__7) | (1 << SkylineParser.ID))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintSkylineContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintSkyline" ):
                return visitor.visitPrintSkyline(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)
        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = SkylineParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.PrintSkylineContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.skyline(0)
                pass

            elif la_ == 2:
                localctx = SkylineParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(SkylineParser.ID)
                self.state = 15
                self.match(SkylineParser.T__0)
                self.state = 16
                self.skyline(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SkylineParser.RULE_skyline

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class IntersectionContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)

        def ESTRELLA(self):
            return self.getToken(SkylineParser.ESTRELLA, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntersection" ):
                return visitor.visitIntersection(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class EdificiSimpleContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INT)
            else:
                return self.getToken(SkylineParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdificiSimple" ):
                return visitor.visitEdificiSimple(self)
            else:
                return visitor.visitChildren(self)


    class ReflectionContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReflection" ):
                return visitor.visitReflection(self)
            else:
                return visitor.visitChildren(self)


    class EdificisAleatorisContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INT)
            else:
                return self.getToken(SkylineParser.INT, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdificisAleatoris" ):
                return visitor.visitEdificisAleatoris(self)
            else:
                return visitor.visitChildren(self)


    class ReplicationContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)

        def ESTRELLA(self):
            return self.getToken(SkylineParser.ESTRELLA, 0)
        def INT(self):
            return self.getToken(SkylineParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplication" ):
                return visitor.visitReplication(self)
            else:
                return visitor.visitChildren(self)


    class EdificisCompostosContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline_sets(self):
            return self.getTypedRuleContext(SkylineParser.Skyline_setsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdificisCompostos" ):
                return visitor.visitEdificisCompostos(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class UnionContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylineContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylineContext,i)

        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnion" ):
                return visitor.visitUnion(self)
            else:
                return visitor.visitChildren(self)


    class DespContext(SkylineContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SkylineParser.SkylineContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def skyline(self):
            return self.getTypedRuleContext(SkylineParser.SkylineContext,0)

        def PLUS(self):
            return self.getToken(SkylineParser.PLUS, 0)
        def INT(self):
            return self.getToken(SkylineParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesp" ):
                return visitor.visitDesp(self)
            else:
                return visitor.visitChildren(self)



    def skyline(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.SkylineContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_skyline, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = SkylineParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(SkylineParser.T__1)
                self.state = 21
                self.skyline(0)
                self.state = 22
                self.match(SkylineParser.T__2)
                pass

            elif la_ == 2:
                localctx = SkylineParser.ReflectionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(SkylineParser.T__3)
                self.state = 25
                self.skyline(9)
                pass

            elif la_ == 3:
                localctx = SkylineParser.EdificiSimpleContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(SkylineParser.T__1)
                self.state = 27
                self.match(SkylineParser.INT)
                self.state = 28
                self.match(SkylineParser.T__4)
                self.state = 29
                self.match(SkylineParser.INT)
                self.state = 30
                self.match(SkylineParser.T__4)
                self.state = 31
                self.match(SkylineParser.INT)
                self.state = 32
                self.match(SkylineParser.T__2)
                pass

            elif la_ == 4:
                localctx = SkylineParser.EdificisCompostosContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 33
                self.match(SkylineParser.T__5)
                self.state = 34
                self.skyline_sets()
                self.state = 35
                self.match(SkylineParser.T__6)
                pass

            elif la_ == 5:
                localctx = SkylineParser.EdificisAleatorisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(SkylineParser.T__7)
                self.state = 38
                self.match(SkylineParser.INT)
                self.state = 39
                self.match(SkylineParser.T__4)
                self.state = 40
                self.match(SkylineParser.INT)
                self.state = 41
                self.match(SkylineParser.T__4)
                self.state = 42
                self.match(SkylineParser.INT)
                self.state = 43
                self.match(SkylineParser.T__4)
                self.state = 44
                self.match(SkylineParser.INT)
                self.state = 45
                self.match(SkylineParser.T__4)
                self.state = 46
                self.match(SkylineParser.INT)
                self.state = 47
                self.match(SkylineParser.T__8)
                pass

            elif la_ == 6:
                localctx = SkylineParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(SkylineParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 63
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.IntersectionContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 51
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 52
                        self.match(SkylineParser.ESTRELLA)
                        self.state = 53
                        self.skyline(9)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.UnionContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        self.match(SkylineParser.PLUS)
                        self.state = 56
                        self.skyline(7)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ReplicationContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 57
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 58
                        self.match(SkylineParser.ESTRELLA)
                        self.state = 59
                        self.match(SkylineParser.INT)
                        pass

                    elif la_ == 4:
                        localctx = SkylineParser.DespContext(self, SkylineParser.SkylineContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_skyline)
                        self.state = 60
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 61
                        self.match(SkylineParser.PLUS)
                        self.state = 62
                        self.match(SkylineParser.INT)
                        pass

             
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Skyline_setsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.INT)
            else:
                return self.getToken(SkylineParser.INT, i)

        def skyline_sets(self):
            return self.getTypedRuleContext(SkylineParser.Skyline_setsContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_skyline_sets

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline_sets" ):
                return visitor.visitSkyline_sets(self)
            else:
                return visitor.visitChildren(self)




    def skyline_sets(self):

        localctx = SkylineParser.Skyline_setsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_skyline_sets)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(SkylineParser.T__1)
                self.state = 69
                self.match(SkylineParser.INT)
                self.state = 70
                self.match(SkylineParser.T__4)
                self.state = 71
                self.match(SkylineParser.INT)
                self.state = 72
                self.match(SkylineParser.T__4)
                self.state = 73
                self.match(SkylineParser.INT)
                self.state = 74
                self.match(SkylineParser.T__9)
                self.state = 75
                self.skyline_sets()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(SkylineParser.T__1)
                self.state = 77
                self.match(SkylineParser.INT)
                self.state = 78
                self.match(SkylineParser.T__4)
                self.state = 79
                self.match(SkylineParser.INT)
                self.state = 80
                self.match(SkylineParser.T__4)
                self.state = 81
                self.match(SkylineParser.INT)
                self.state = 82
                self.match(SkylineParser.T__2)
                pass


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
        self._predicates[2] = self.skyline_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def skyline_sempred(self, localctx:SkylineContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




