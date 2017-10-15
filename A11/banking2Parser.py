# Generated from banking2.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\6\2\r\n\2")
        buf.write("\r\2\16\2\16\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\5 \n\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5\3\5\2")
        buf.write("\3\b\6\2\4\6\b\2\2\2\66\2\f\3\2\2\2\4\20\3\2\2\2\6\24")
        buf.write("\3\2\2\2\b\37\3\2\2\2\n\r\5\4\3\2\13\r\5\6\4\2\f\n\3\2")
        buf.write("\2\2\f\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2")
        buf.write("\2\2\17\3\3\2\2\2\20\21\7\r\2\2\21\22\7\t\2\2\22\23\5")
        buf.write("\b\5\2\23\5\3\2\2\2\24\25\7\r\2\2\25\26\7\n\2\2\26\27")
        buf.write("\5\b\5\2\27\7\3\2\2\2\30\31\b\5\1\2\31 \7\13\2\2\32 \7")
        buf.write("\r\2\2\33\34\7\3\2\2\34\35\5\b\5\2\35\36\7\4\2\2\36 \3")
        buf.write("\2\2\2\37\30\3\2\2\2\37\32\3\2\2\2\37\33\3\2\2\2 /\3\2")
        buf.write("\2\2!\"\f\t\2\2\"#\7\5\2\2#.\5\b\5\n$%\f\b\2\2%&\7\6\2")
        buf.write("\2&.\5\b\5\t\'(\f\7\2\2()\7\7\2\2).\5\b\5\b*+\f\6\2\2")
        buf.write("+,\7\b\2\2,.\5\b\5\7-!\3\2\2\2-$\3\2\2\2-\'\3\2\2\2-*")
        buf.write("\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\t\3\2\2")
        buf.write("\2\61/\3\2\2\2\7\f\16\37-/")
        return buf.getvalue()


class banking2Parser ( Parser ):

    grammarFileName = "banking2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'*'", "'/'", "'+'", "'-'", 
                     "'dep'", "'withdraw'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "DEPOSIT", "WITHDRAW", "NUM", "DIGIT", 
                      "ID", "WS" ]

    RULE_transaction = 0
    RULE_deposit = 1
    RULE_withdraw = 2
    RULE_expr = 3

    ruleNames =  [ "transaction", "deposit", "withdraw", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    MUL=3
    DIV=4
    ADD=5
    SUB=6
    DEPOSIT=7
    WITHDRAW=8
    NUM=9
    DIGIT=10
    ID=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class TransactionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def deposit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(banking2Parser.DepositContext)
            else:
                return self.getTypedRuleContext(banking2Parser.DepositContext,i)


        def withdraw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(banking2Parser.WithdrawContext)
            else:
                return self.getTypedRuleContext(banking2Parser.WithdrawContext,i)


        def getRuleIndex(self):
            return banking2Parser.RULE_transaction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransaction" ):
                listener.enterTransaction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransaction" ):
                listener.exitTransaction(self)




    def transaction(self):

        localctx = banking2Parser.TransactionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_transaction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 8
                    self.deposit()
                    pass

                elif la_ == 2:
                    self.state = 9
                    self.withdraw()
                    pass


                self.state = 12 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==banking2Parser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DepositContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(banking2Parser.ID, 0)

        def DEPOSIT(self):
            return self.getToken(banking2Parser.DEPOSIT, 0)

        def expr(self):
            return self.getTypedRuleContext(banking2Parser.ExprContext,0)


        def getRuleIndex(self):
            return banking2Parser.RULE_deposit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeposit" ):
                listener.enterDeposit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeposit" ):
                listener.exitDeposit(self)




    def deposit(self):

        localctx = banking2Parser.DepositContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_deposit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(banking2Parser.ID)
            self.state = 15
            self.match(banking2Parser.DEPOSIT)
            self.state = 16
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class WithdrawContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(banking2Parser.ID, 0)

        def WITHDRAW(self):
            return self.getToken(banking2Parser.WITHDRAW, 0)

        def expr(self):
            return self.getTypedRuleContext(banking2Parser.ExprContext,0)


        def getRuleIndex(self):
            return banking2Parser.RULE_withdraw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWithdraw" ):
                listener.enterWithdraw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWithdraw" ):
                listener.exitWithdraw(self)




    def withdraw(self):

        localctx = banking2Parser.WithdrawContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_withdraw)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(banking2Parser.ID)
            self.state = 19
            self.match(banking2Parser.WITHDRAW)
            self.state = 20
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return banking2Parser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DIVContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a banking2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(banking2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(banking2Parser.ExprContext,i)

        def DIV(self):
            return self.getToken(banking2Parser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDIV" ):
                listener.enterDIV(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDIV" ):
                listener.exitDIV(self)


    class ADDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a banking2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(banking2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(banking2Parser.ExprContext,i)

        def ADD(self):
            return self.getToken(banking2Parser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterADD" ):
                listener.enterADD(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitADD" ):
                listener.exitADD(self)


    class SUBContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a banking2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(banking2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(banking2Parser.ExprContext,i)

        def SUB(self):
            return self.getToken(banking2Parser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSUB" ):
                listener.enterSUB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSUB" ):
                listener.exitSUB(self)


    class PARENSContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a banking2Parser.ExprContext
            super().__init__(parser)
            self.e = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(banking2Parser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPARENS" ):
                listener.enterPARENS(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPARENS" ):
                listener.exitPARENS(self)


    class MULContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a banking2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(banking2Parser.ExprContext)
            else:
                return self.getTypedRuleContext(banking2Parser.ExprContext,i)

        def MUL(self):
            return self.getToken(banking2Parser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMUL" ):
                listener.enterMUL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMUL" ):
                listener.exitMUL(self)


    class NUMContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a banking2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUM(self):
            return self.getToken(banking2Parser.NUM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNUM" ):
                listener.enterNUM(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNUM" ):
                listener.exitNUM(self)


    class IDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a banking2Parser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(banking2Parser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterID" ):
                listener.enterID(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitID" ):
                listener.exitID(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = banking2Parser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [banking2Parser.NUM]:
                localctx = banking2Parser.NUMContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(banking2Parser.NUM)
                pass
            elif token in [banking2Parser.ID]:
                localctx = banking2Parser.IDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(banking2Parser.ID)
                pass
            elif token in [banking2Parser.T__0]:
                localctx = banking2Parser.PARENSContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(banking2Parser.T__0)
                self.state = 26
                localctx.e = self.expr(0)
                self.state = 27
                self.match(banking2Parser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 43
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = banking2Parser.MULContext(self, banking2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 32
                        self.match(banking2Parser.MUL)
                        self.state = 33
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = banking2Parser.DIVContext(self, banking2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 35
                        self.match(banking2Parser.DIV)
                        self.state = 36
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = banking2Parser.ADDContext(self, banking2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 38
                        self.match(banking2Parser.ADD)
                        self.state = 39
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = banking2Parser.SUBContext(self, banking2Parser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 41
                        self.match(banking2Parser.SUB)
                        self.state = 42
                        self.expr(5)
                        pass

             
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         




