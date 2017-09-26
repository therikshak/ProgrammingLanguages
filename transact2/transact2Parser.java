// Generated from transact2.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class transact2Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DEPOSIT=1, WITHDRAW=2, BYE=3, NUM=4, DIGIT=5, ID=6, WS=7;
	public static final int
		RULE_transaction = 0, RULE_deposit = 1, RULE_withdraw = 2;
	public static final String[] ruleNames = {
		"transaction", "deposit", "withdraw"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'dep'", "'withdraw'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "DEPOSIT", "WITHDRAW", "BYE", "NUM", "DIGIT", "ID", "WS"
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
	public String getGrammarFileName() { return "transact2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public transact2Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class TransactionContext extends ParserRuleContext {
		public TerminalNode BYE() { return getToken(transact2Parser.BYE, 0); }
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
			if ( listener instanceof transact2Listener ) ((transact2Listener)listener).enterTransaction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof transact2Listener ) ((transact2Listener)listener).exitTransaction(this);
		}
	}

	public final TransactionContext transaction() throws RecognitionException {
		TransactionContext _localctx = new TransactionContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_transaction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(8);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(6);
					deposit();
					}
					break;
				case 2:
					{
					setState(7);
					withdraw();
					}
					break;
				}
				}
				setState(10); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
			setState(12);
			match(BYE);
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
		public TerminalNode ID() { return getToken(transact2Parser.ID, 0); }
		public TerminalNode DEPOSIT() { return getToken(transact2Parser.DEPOSIT, 0); }
		public TerminalNode NUM() { return getToken(transact2Parser.NUM, 0); }
		public DepositContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_deposit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof transact2Listener ) ((transact2Listener)listener).enterDeposit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof transact2Listener ) ((transact2Listener)listener).exitDeposit(this);
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
			match(NUM);
			System.out.println("Hey " +((DepositContext)_localctx).ID.getText() + ", saving money eh?"); 
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
		public TerminalNode ID() { return getToken(transact2Parser.ID, 0); }
		public TerminalNode WITHDRAW() { return getToken(transact2Parser.WITHDRAW, 0); }
		public TerminalNode NUM() { return getToken(transact2Parser.NUM, 0); }
		public WithdrawContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_withdraw; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof transact2Listener ) ((transact2Listener)listener).enterWithdraw(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof transact2Listener ) ((transact2Listener)listener).exitWithdraw(this);
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
			match(NUM);
			System.out.println(((WithdrawContext)_localctx).ID.getText() + " need some cash?"); 
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

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t\33\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\3\2\3\2\6\2\13\n\2\r\2\16\2\f\3\2\3\2\3\3\3\3\3\3\3\3\3\3"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\2\2\5\2\4\6\2\2\2\31\2\n\3\2\2\2\4\20\3\2\2\2"+
		"\6\25\3\2\2\2\b\13\5\4\3\2\t\13\5\6\4\2\n\b\3\2\2\2\n\t\3\2\2\2\13\f\3"+
		"\2\2\2\f\n\3\2\2\2\f\r\3\2\2\2\r\16\3\2\2\2\16\17\7\5\2\2\17\3\3\2\2\2"+
		"\20\21\7\b\2\2\21\22\7\3\2\2\22\23\7\6\2\2\23\24\b\3\1\2\24\5\3\2\2\2"+
		"\25\26\7\b\2\2\26\27\7\4\2\2\27\30\7\6\2\2\30\31\b\4\1\2\31\7\3\2\2\2"+
		"\4\n\f";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}