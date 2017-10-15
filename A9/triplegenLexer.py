# Generated from triplegen.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\30\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\6\5\23\n\5\r\5\16\5\24\3\5\3\5\2\2\6\3")
        buf.write("\3\5\4\7\5\t\6\3\2\6\7\2dfhioprrtt\7\2ccggkkqqww\b\2f")
        buf.write("fiipprrtvy|\5\2\13\f\17\17\"\"\2\30\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2\2\5\r\3\2\2")
        buf.write("\2\7\17\3\2\2\2\t\22\3\2\2\2\13\f\t\2\2\2\f\4\3\2\2\2")
        buf.write("\r\16\t\3\2\2\16\6\3\2\2\2\17\20\t\4\2\2\20\b\3\2\2\2")
        buf.write("\21\23\t\5\2\2\22\21\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2")
        buf.write("\2\24\25\3\2\2\2\25\26\3\2\2\2\26\27\b\5\2\2\27\n\3\2")
        buf.write("\2\2\4\2\24\3\b\2\2")
        return buf.getvalue()


class triplegenLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    L1 = 1
    L2 = 2
    L3 = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "L1", "L2", "L3", "WS" ]

    ruleNames = [ "L1", "L2", "L3", "WS" ]

    grammarFileName = "triplegen.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


