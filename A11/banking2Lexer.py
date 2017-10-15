# Generated from banking2.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\6\n\66")
        buf.write("\n\n\r\n\16\n\67\3\13\3\13\3\f\6\f=\n\f\r\f\16\f>\3\r")
        buf.write("\6\rB\n\r\r\r\16\rC\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\5\3\2\62;\3")
        buf.write("\2c|\5\2\13\f\17\17\"\"\2I\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2")
        buf.write("\t!\3\2\2\2\13#\3\2\2\2\r%\3\2\2\2\17\'\3\2\2\2\21+\3")
        buf.write("\2\2\2\23\65\3\2\2\2\259\3\2\2\2\27<\3\2\2\2\31A\3\2\2")
        buf.write("\2\33\34\7*\2\2\34\4\3\2\2\2\35\36\7+\2\2\36\6\3\2\2\2")
        buf.write("\37 \7,\2\2 \b\3\2\2\2!\"\7\61\2\2\"\n\3\2\2\2#$\7-\2")
        buf.write("\2$\f\3\2\2\2%&\7/\2\2&\16\3\2\2\2\'(\7f\2\2()\7g\2\2")
        buf.write(")*\7r\2\2*\20\3\2\2\2+,\7y\2\2,-\7k\2\2-.\7v\2\2./\7j")
        buf.write("\2\2/\60\7f\2\2\60\61\7t\2\2\61\62\7c\2\2\62\63\7y\2\2")
        buf.write("\63\22\3\2\2\2\64\66\5\25\13\2\65\64\3\2\2\2\66\67\3\2")
        buf.write("\2\2\67\65\3\2\2\2\678\3\2\2\28\24\3\2\2\29:\t\2\2\2:")
        buf.write("\26\3\2\2\2;=\t\3\2\2<;\3\2\2\2=>\3\2\2\2><\3\2\2\2>?")
        buf.write("\3\2\2\2?\30\3\2\2\2@B\t\4\2\2A@\3\2\2\2BC\3\2\2\2CA\3")
        buf.write("\2\2\2CD\3\2\2\2DE\3\2\2\2EF\b\r\2\2F\32\3\2\2\2\6\2\67")
        buf.write(">C\3\b\2\2")
        return buf.getvalue()


class banking2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    MUL = 3
    DIV = 4
    ADD = 5
    SUB = 6
    DEPOSIT = 7
    WITHDRAW = 8
    NUM = 9
    DIGIT = 10
    ID = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'*'", "'/'", "'+'", "'-'", "'dep'", "'withdraw'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "DEPOSIT", "WITHDRAW", "NUM", "DIGIT", 
            "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "MUL", "DIV", "ADD", "SUB", "DEPOSIT", 
                  "WITHDRAW", "NUM", "DIGIT", "ID", "WS" ]

    grammarFileName = "banking2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


