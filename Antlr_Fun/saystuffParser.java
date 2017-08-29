// Generated from saystuff.g4 by ANTLR 4.7
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class saystuffParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		HELLOTOK=1, TITLE=2, BYETOK=3, ENDTOK=4, VERB=5, DESCR=6, ID=7, WS=8;
	public static final int
		RULE_stmt = 0, RULE_infostmt = 1, RULE_hellostmt = 2, RULE_byestmt = 3;
	public static final String[] ruleNames = {
		"stmt", "infostmt", "hellostmt", "byestmt"
	};

	private static final String[] _LITERAL_NAMES = {
		null, null, null, null, "'later'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, "HELLOTOK", "TITLE", "BYETOK", "ENDTOK", "VERB", "DESCR", "ID", 
		"WS"
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
	public String getGrammarFileName() { return "saystuff.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public saystuffParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class StmtContext extends ParserRuleContext {
		public HellostmtContext hellostmt() {
			return getRuleContext(HellostmtContext.class,0);
		}
		public ByestmtContext byestmt() {
			return getRuleContext(ByestmtContext.class,0);
		}
		public InfostmtContext infostmt() {
			return getRuleContext(InfostmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).enterStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).exitStmt(this);
		}
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_stmt);
		try {
			setState(11);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(8);
				hellostmt();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(9);
				byestmt();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(10);
				infostmt();
				}
				break;
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

	public static class InfostmtContext extends ParserRuleContext {
		public TerminalNode HELLOTOK() { return getToken(saystuffParser.HELLOTOK, 0); }
		public TerminalNode TITLE() { return getToken(saystuffParser.TITLE, 0); }
		public TerminalNode ID() { return getToken(saystuffParser.ID, 0); }
		public TerminalNode VERB() { return getToken(saystuffParser.VERB, 0); }
		public TerminalNode DESCR() { return getToken(saystuffParser.DESCR, 0); }
		public InfostmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_infostmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).enterInfostmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).exitInfostmt(this);
		}
	}

	public final InfostmtContext infostmt() throws RecognitionException {
		InfostmtContext _localctx = new InfostmtContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_infostmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			match(HELLOTOK);
			setState(14);
			match(TITLE);
			setState(15);
			match(ID);
			setState(16);
			match(VERB);
			setState(17);
			match(DESCR);
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

	public static class HellostmtContext extends ParserRuleContext {
		public TerminalNode HELLOTOK() { return getToken(saystuffParser.HELLOTOK, 0); }
		public TerminalNode TITLE() { return getToken(saystuffParser.TITLE, 0); }
		public TerminalNode ID() { return getToken(saystuffParser.ID, 0); }
		public HellostmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hellostmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).enterHellostmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).exitHellostmt(this);
		}
	}

	public final HellostmtContext hellostmt() throws RecognitionException {
		HellostmtContext _localctx = new HellostmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_hellostmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(HELLOTOK);
			setState(20);
			match(TITLE);
			setState(21);
			match(ID);
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

	public static class ByestmtContext extends ParserRuleContext {
		public TerminalNode BYETOK() { return getToken(saystuffParser.BYETOK, 0); }
		public TerminalNode TITLE() { return getToken(saystuffParser.TITLE, 0); }
		public TerminalNode ID() { return getToken(saystuffParser.ID, 0); }
		public List<TerminalNode> ENDTOK() { return getTokens(saystuffParser.ENDTOK); }
		public TerminalNode ENDTOK(int i) {
			return getToken(saystuffParser.ENDTOK, i);
		}
		public ByestmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_byestmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).enterByestmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof saystuffListener ) ((saystuffListener)listener).exitByestmt(this);
		}
	}

	public final ByestmtContext byestmt() throws RecognitionException {
		ByestmtContext _localctx = new ByestmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_byestmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			match(BYETOK);
			setState(24);
			match(TITLE);
			setState(25);
			match(ID);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ENDTOK) {
				{
				{
				setState(26);
				match(ENDTOK);
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n#\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\5\2\16\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4"+
		"\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\36\n\5\f\5\16\5!\13\5\3\5\2\2\6\2\4\6"+
		"\b\2\2\2!\2\r\3\2\2\2\4\17\3\2\2\2\6\25\3\2\2\2\b\31\3\2\2\2\n\16\5\6"+
		"\4\2\13\16\5\b\5\2\f\16\5\4\3\2\r\n\3\2\2\2\r\13\3\2\2\2\r\f\3\2\2\2\16"+
		"\3\3\2\2\2\17\20\7\3\2\2\20\21\7\4\2\2\21\22\7\t\2\2\22\23\7\7\2\2\23"+
		"\24\7\b\2\2\24\5\3\2\2\2\25\26\7\3\2\2\26\27\7\4\2\2\27\30\7\t\2\2\30"+
		"\7\3\2\2\2\31\32\7\5\2\2\32\33\7\4\2\2\33\37\7\t\2\2\34\36\7\6\2\2\35"+
		"\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \t\3\2\2\2!\37\3\2\2"+
		"\2\4\r\37";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}