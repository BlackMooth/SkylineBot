# Generated from testSkyline.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("R\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16=\n\16\r\16\16\16")
        buf.write(">\3\16\7\16B\n\16\f\16\16\16E\13\16\3\17\6\17H\n\17\r")
        buf.write("\17\16\17I\3\20\6\20M\n\20\r\20\16\20N\3\20\3\20\2\2\21")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21\3\2\6\4\2C\\c|\5\2\62;C\\c|\3\2")
        buf.write("\62;\4\2\13\13\"\"\2U\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3!")
        buf.write("\3\2\2\2\5$\3\2\2\2\7&\3\2\2\2\t(\3\2\2\2\13*\3\2\2\2")
        buf.write("\r,\3\2\2\2\17.\3\2\2\2\21\60\3\2\2\2\23\62\3\2\2\2\25")
        buf.write("\64\3\2\2\2\27\67\3\2\2\2\319\3\2\2\2\33<\3\2\2\2\35G")
        buf.write("\3\2\2\2\37L\3\2\2\2!\"\7<\2\2\"#\7?\2\2#\4\3\2\2\2$%")
        buf.write("\7*\2\2%\6\3\2\2\2&\'\7+\2\2\'\b\3\2\2\2()\7/\2\2)\n\3")
        buf.write("\2\2\2*+\7.\2\2+\f\3\2\2\2,-\7]\2\2-\16\3\2\2\2./\7_\2")
        buf.write("\2/\20\3\2\2\2\60\61\7}\2\2\61\22\3\2\2\2\62\63\7\177")
        buf.write("\2\2\63\24\3\2\2\2\64\65\7+\2\2\65\66\7.\2\2\66\26\3\2")
        buf.write("\2\2\678\7-\2\28\30\3\2\2\29:\7,\2\2:\32\3\2\2\2;=\t\2")
        buf.write("\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?\3\2\2\2?C\3\2\2\2")
        buf.write("@B\t\3\2\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2\2\2D\34")
        buf.write("\3\2\2\2EC\3\2\2\2FH\t\4\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2")
        buf.write("\2\2IJ\3\2\2\2J\36\3\2\2\2KM\t\5\2\2LK\3\2\2\2MN\3\2\2")
        buf.write("\2NL\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\b\20\2\2Q \3\2\2\2")
        buf.write("\7\2>CIN\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    PLUS = 11
    ESTRELLA = 12
    ID = 13
    INT = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "':='", "'('", "')'", "'-'", "','", "'['", "']'", "'{'", "'}'", 
            "'),'", "'+'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "ESTRELLA", "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "PLUS", "ESTRELLA", "ID", "INT", 
                  "WS" ]

    grammarFileName = "testSkyline.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


