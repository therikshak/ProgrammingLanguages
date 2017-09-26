// Generated from bankWithExpr.g4 by ANTLR 4.7

  import java.util.*; 

import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class bankWithExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, MOD=3, MUL=4, DIV=5, ADD=6, SUB=7, DEPOSIT=8, WITHDRAW=9, 
		NUM=10, DIGIT=11, ID=12, WS=13;
	public static final int
		RULE_transaction = 0, RULE_deposit = 1, RULE_withdraw = 2, RULE_expr = 3;
	public static final String[] ruleNames = {
		"transaction", "deposit", "withdraw", "expr"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'('", "')'", "'%'", "'*'", "'/'", "'+'", "'-'", "'dep'", "'withdraw'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, "MOD", "MUL", "DIV", "ADD", "SUB", "DEPOSIT", "WITHDRAW", 
		"NUM", "DIGIT", "ID", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "bankWithExpr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }



	  // member data  ---
	  Map<String, Integer> customers = new HashMap<String, Integer>() ;
	  
	  // member functions ---  
	  void makeDeposit(String user,  int amt) {
	   	if (customers.containsKey(user) ) {
	   	   System.out.println("Welcome back " + user);
	   	   customers.put(user, (customers.get(user) + amt));   	   
	   	}
	   	else {
	   	   System.out.println("Welcome new customer " + user); 
	   	   customers.put(user,amt);
	   	}
	   	
	   	System.out.println("Your deposit of " + amt + " has been processed");
	   	  	
	  }
	  
	  void makeWithdrawal(String user,  int amt) {
	   	if (customers.containsKey(user) ) {
	   	   System.out.println("Welcome back " + user);   	   
	   	}
	   	else {
	   	   System.out.println("Welcome new customer " + user);
	   	   customers.put(user,0); 
	   	}
	   	
	   	if(customers.get(user) < amt){
	   		System.out.println("Your withdrawal of " + amt + 
	   		" cannot be processed due to a balance of " + customers.get(user));
	   	}
	   	else{
	   		customers.put(user, (customers.get(user)-amt));
	   		System.out.println("Your withdrawal of " + amt + " has been processed");
	   	}
	   	  	
	  } 
	  
	  int doMath(int v1, int v2, int op) {
	     int retval = -1;
	     switch(op) {
	       case MOD : retval = v1 % v2;
	       		  break;
	       case MUL : retval = v1 * v2;
	              break;
	       case DIV : retval = v1 / v2;
	       		  break;
	       case ADD : retval = v1 + v2;
	       		  break;
	       case SUB : retval = v1 - v2;
	              break;
	     }
	     return retval;
	  
	  }

	public bankWithExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class TransactionContext extends ParserRuleContext {
		public List<DepositContext> deposit() {
			return getRuleContexts(DepositContext.class);
		}
		public DepositContext deposit(int i) {
			return getRuleContext(DepositContext.class,i);
		}
		public List<WithdrawContext> withdraw() {
			return getRuleContexts(WithdrawContext.class);
		}
		public WithdrawContext withdraw(int i) {
			return getRuleContext(WithdrawContext.class,i);
		}
		public TransactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_transaction; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).enterTransaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).exitTransaction(this);
		}
	}

	public final TransactionContext transaction() throws RecognitionException {
		TransactionContext _localctx = new TransactionContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_transaction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(10); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(10);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(8);
					deposit();
					}
					break;
				case 2:
					{
					setState(9);
					withdraw();
					}
					break;
				}
				}
				setState(12); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DepositContext extends ParserRuleContext {
		public Token ID;
		public ExprContext expr;
		public TerminalNode ID() { return getToken(bankWithExprParser.ID, 0); }
		public TerminalNode DEPOSIT() { return getToken(bankWithExprParser.DEPOSIT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public DepositContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_deposit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).enterDeposit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).exitDeposit(this);
		}
	}

	public final DepositContext deposit() throws RecognitionException {
		DepositContext _localctx = new DepositContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_deposit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			((DepositContext)_localctx).ID = match(ID);
			setState(15);
			match(DEPOSIT);
			setState(16);
			((DepositContext)_localctx).expr = expr(0);
			 makeDeposit   ((((DepositContext)_localctx).ID!=null?((DepositContext)_localctx).ID.getText():null), ((DepositContext)_localctx).expr.v); 
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class WithdrawContext extends ParserRuleContext {
		public Token ID;
		public ExprContext expr;
		public TerminalNode ID() { return getToken(bankWithExprParser.ID, 0); }
		public TerminalNode WITHDRAW() { return getToken(bankWithExprParser.WITHDRAW, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public WithdrawContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_withdraw; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).enterWithdraw(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).exitWithdraw(this);
		}
	}

	public final WithdrawContext withdraw() throws RecognitionException {
		WithdrawContext _localctx = new WithdrawContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_withdraw);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			((WithdrawContext)_localctx).ID = match(ID);
			setState(20);
			match(WITHDRAW);
			setState(21);
			((WithdrawContext)_localctx).expr = expr(0);
			 makeWithdrawal((((WithdrawContext)_localctx).ID!=null?((WithdrawContext)_localctx).ID.getText():null), ((WithdrawContext)_localctx).expr.v); 
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public int v;
		public ExprContext a;
		public Token NUM;
		public Token ID;
		public ExprContext e;
		public Token op;
		public ExprContext b;
		public TerminalNode NUM() { return getToken(bankWithExprParser.NUM, 0); }
		public TerminalNode ID() { return getToken(bankWithExprParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MOD() { return getToken(bankWithExprParser.MOD, 0); }
		public TerminalNode MUL() { return getToken(bankWithExprParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(bankWithExprParser.DIV, 0); }
		public TerminalNode ADD() { return getToken(bankWithExprParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(bankWithExprParser.SUB, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof bankWithExprListener ) ((bankWithExprListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 6;
		enterRecursionRule(_localctx, 6, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUM:
				{
				setState(25);
				((ExprContext)_localctx).NUM = match(NUM);
				((ExprContext)_localctx).v =  Integer.valueOf(((ExprContext)_localctx).NUM.getText());
				}
				break;
			case ID:
				{
				setState(27);
				((ExprContext)_localctx).ID = match(ID);

				                                   String id = ((ExprContext)_localctx).ID.getText();
				                                   if ( customers.containsKey(id) ) {
				                                       ((ExprContext)_localctx).v =  customers.get(id);
				                                   }
				                                   else {
				                                   	((ExprContext)_localctx).v =  0;
				                                   }
				                                   
				}
				break;
			case T__0:
				{
				setState(29);
				match(T__0);
				setState(30);
				((ExprContext)_localctx).e = expr(0);
				setState(31);
				match(T__1);
				((ExprContext)_localctx).v =  ((ExprContext)_localctx).e.v;
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(53);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(51);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.a = _prevctx;
						_localctx.a = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(36);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(37);
						((ExprContext)_localctx).op = match(MOD);
						setState(38);
						((ExprContext)_localctx).b = expr(7);
						 ((ExprContext)_localctx).v =  doMath(((ExprContext)_localctx).a.v, ((ExprContext)_localctx).b.v, ((ExprContext)_localctx).op.getType() ); 
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.a = _prevctx;
						_localctx.a = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(41);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(42);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(43);
						((ExprContext)_localctx).b = expr(6);
						 ((ExprContext)_localctx).v =  doMath(((ExprContext)_localctx).a.v, ((ExprContext)_localctx).b.v, ((ExprContext)_localctx).op.getType() ); 
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						_localctx.a = _prevctx;
						_localctx.a = _prevctx;
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(46);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(47);
						((ExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((ExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(48);
						((ExprContext)_localctx).b = expr(5);
						 ((ExprContext)_localctx).v =  doMath(((ExprContext)_localctx).a.v, ((ExprContext)_localctx).b.v, ((ExprContext)_localctx).op.getType() ); 
						}
						break;
					}
					} 
				}
				setState(55);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 3:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		case 2:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17;\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\3\2\6\2\r\n\2\r\2\16\2\16\3\3\3\3\3\3\3\3\3\3\3"+
		"\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5%\n\5\3"+
		"\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\66\n\5"+
		"\f\5\16\59\13\5\3\5\2\3\b\6\2\4\6\b\2\4\3\2\6\7\3\2\b\t\2=\2\f\3\2\2\2"+
		"\4\20\3\2\2\2\6\25\3\2\2\2\b$\3\2\2\2\n\r\5\4\3\2\13\r\5\6\4\2\f\n\3\2"+
		"\2\2\f\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2\2\17\3\3\2\2\2"+
		"\20\21\7\16\2\2\21\22\7\n\2\2\22\23\5\b\5\2\23\24\b\3\1\2\24\5\3\2\2\2"+
		"\25\26\7\16\2\2\26\27\7\13\2\2\27\30\5\b\5\2\30\31\b\4\1\2\31\7\3\2\2"+
		"\2\32\33\b\5\1\2\33\34\7\f\2\2\34%\b\5\1\2\35\36\7\16\2\2\36%\b\5\1\2"+
		"\37 \7\3\2\2 !\5\b\5\2!\"\7\4\2\2\"#\b\5\1\2#%\3\2\2\2$\32\3\2\2\2$\35"+
		"\3\2\2\2$\37\3\2\2\2%\67\3\2\2\2&\'\f\b\2\2\'(\7\5\2\2()\5\b\5\t)*\b\5"+
		"\1\2*\66\3\2\2\2+,\f\7\2\2,-\t\2\2\2-.\5\b\5\b./\b\5\1\2/\66\3\2\2\2\60"+
		"\61\f\6\2\2\61\62\t\3\2\2\62\63\5\b\5\7\63\64\b\5\1\2\64\66\3\2\2\2\65"+
		"&\3\2\2\2\65+\3\2\2\2\65\60\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\678\3\2"+
		"\2\28\t\3\2\2\29\67\3\2\2\2\7\f\16$\65\67";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}