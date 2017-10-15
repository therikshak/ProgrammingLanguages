# Generated from triplegen.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\20\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\3\3\3\3")
        buf.write("\3\3\3\3\3\2\2\4\2\4\2\2\2\16\2\7\3\2\2\2\4\13\3\2\2\2")
        buf.write("\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3\2\2\2\t\n\3")
        buf.write("\2\2\2\n\3\3\2\2\2\13\f\7\3\2\2\f\r\7\4\2\2\r\16\7\5\2")
        buf.write("\2\16\5\3\2\2\2\3\t")
        return buf.getvalue()


class triplegenParser ( Parser ):

    grammarFileName = "triplegen.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "L1", "L2", "L3", "WS" ]

    RULE_phrase = 0
    RULE_word = 1

    ruleNames =  [ "phrase", "word" ]

    EOF = Token.EOF
    L1=1
    L2=2
    L3=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class PhraseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(triplegenParser.WordContext)
            else:
                return self.getTypedRuleContext(triplegenParser.WordContext,i)


        def getRuleIndex(self):
            return triplegenParser.RULE_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhrase" ):
                listener.enterPhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhrase" ):
                listener.exitPhrase(self)




    def phrase(self):

        localctx = triplegenParser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_phrase)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.word()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==triplegenParser.L1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WordContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L1(self):
            return self.getToken(triplegenParser.L1, 0)

        def L2(self):
            return self.getToken(triplegenParser.L2, 0)

        def L3(self):
            return self.getToken(triplegenParser.L3, 0)

        def getRuleIndex(self):
            return triplegenParser.RULE_word

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWord" ):
                listener.enterWord(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWord" ):
                listener.exitWord(self)




    def word(self):

        localctx = triplegenParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_word)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(triplegenParser.L1)
            self.state = 10
            self.match(triplegenParser.L2)
            self.state = 11
            self.match(triplegenParser.L3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





