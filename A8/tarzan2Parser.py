# Generated from tarzan2.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\36\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13")
        buf.write("\3\3\3\3\3\3\5\3\21\n\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\31")
        buf.write("\n\3\3\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2\2\37\2\t\3\2\2\2")
        buf.write("\4\30\3\2\2\2\6\32\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13")
        buf.write("\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\16\7")
        buf.write("\3\2\2\16\20\7\4\2\2\17\21\5\6\4\2\20\17\3\2\2\2\20\21")
        buf.write("\3\2\2\2\21\31\3\2\2\2\22\23\7\5\2\2\23\31\7\b\2\2\24")
        buf.write("\25\7\7\2\2\25\31\7\3\2\2\26\27\7\7\2\2\27\31\7\5\2\2")
        buf.write("\30\r\3\2\2\2\30\22\3\2\2\2\30\24\3\2\2\2\30\26\3\2\2")
        buf.write("\2\31\5\3\2\2\2\32\33\7\6\2\2\33\34\7\5\2\2\34\7\3\2\2")
        buf.write("\2\5\13\20\30")
        return buf.getvalue()


class tarzan2Parser ( Parser ):

    grammarFileName = "tarzan2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'what about'" ]

    symbolicNames = [ "<INVALID>", "PERSON", "VERB", "PLACE", "CONJ", "QUERY", 
                      "ADJECTIVE", "WS" ]

    RULE_sentence = 0
    RULE_statement = 1
    RULE_phrase = 2

    ruleNames =  [ "sentence", "statement", "phrase" ]

    EOF = Token.EOF
    PERSON=1
    VERB=2
    PLACE=3
    CONJ=4
    QUERY=5
    ADJECTIVE=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SentenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(tarzan2Parser.StatementContext)
            else:
                return self.getTypedRuleContext(tarzan2Parser.StatementContext,i)


        def getRuleIndex(self):
            return tarzan2Parser.RULE_sentence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentence" ):
                listener.enterSentence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentence" ):
                listener.exitSentence(self)




    def sentence(self):

        localctx = tarzan2Parser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.statement()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << tarzan2Parser.PERSON) | (1 << tarzan2Parser.PLACE) | (1 << tarzan2Parser.QUERY))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return tarzan2Parser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PERSONQUERYContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tarzan2Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUERY(self):
            return self.getToken(tarzan2Parser.QUERY, 0)
        def PERSON(self):
            return self.getToken(tarzan2Parser.PERSON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPERSONQUERY" ):
                listener.enterPERSONQUERY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPERSONQUERY" ):
                listener.exitPERSONQUERY(self)


    class PLACEFACTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tarzan2Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PLACE(self):
            return self.getToken(tarzan2Parser.PLACE, 0)
        def ADJECTIVE(self):
            return self.getToken(tarzan2Parser.ADJECTIVE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPLACEFACT" ):
                listener.enterPLACEFACT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPLACEFACT" ):
                listener.exitPLACEFACT(self)


    class PEOPLEFACTContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tarzan2Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PERSON(self):
            return self.getToken(tarzan2Parser.PERSON, 0)
        def VERB(self):
            return self.getToken(tarzan2Parser.VERB, 0)
        def phrase(self):
            return self.getTypedRuleContext(tarzan2Parser.PhraseContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPEOPLEFACT" ):
                listener.enterPEOPLEFACT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPEOPLEFACT" ):
                listener.exitPEOPLEFACT(self)


    class PLACEQUERYContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a tarzan2Parser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def QUERY(self):
            return self.getToken(tarzan2Parser.QUERY, 0)
        def PLACE(self):
            return self.getToken(tarzan2Parser.PLACE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPLACEQUERY" ):
                listener.enterPLACEQUERY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPLACEQUERY" ):
                listener.exitPLACEQUERY(self)



    def statement(self):

        localctx = tarzan2Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = tarzan2Parser.PEOPLEFACTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.match(tarzan2Parser.PERSON)
                self.state = 12
                self.match(tarzan2Parser.VERB)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==tarzan2Parser.CONJ:
                    self.state = 13
                    self.phrase()


                pass

            elif la_ == 2:
                localctx = tarzan2Parser.PLACEFACTContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.match(tarzan2Parser.PLACE)
                self.state = 17
                self.match(tarzan2Parser.ADJECTIVE)
                pass

            elif la_ == 3:
                localctx = tarzan2Parser.PERSONQUERYContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(tarzan2Parser.QUERY)
                self.state = 19
                self.match(tarzan2Parser.PERSON)
                pass

            elif la_ == 4:
                localctx = tarzan2Parser.PLACEQUERYContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 20
                self.match(tarzan2Parser.QUERY)
                self.state = 21
                self.match(tarzan2Parser.PLACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PhraseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONJ(self):
            return self.getToken(tarzan2Parser.CONJ, 0)

        def PLACE(self):
            return self.getToken(tarzan2Parser.PLACE, 0)

        def getRuleIndex(self):
            return tarzan2Parser.RULE_phrase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPhrase" ):
                listener.enterPhrase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPhrase" ):
                listener.exitPhrase(self)




    def phrase(self):

        localctx = tarzan2Parser.PhraseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_phrase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(tarzan2Parser.CONJ)
            self.state = 25
            self.match(tarzan2Parser.PLACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





