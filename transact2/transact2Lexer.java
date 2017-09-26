// Generated from transact2.g4 by ANTLR 4.7
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class transact2Lexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DEPOSIT=1, WITHDRAW=2, BYE=3, NUM=4, DIGIT=5, ID=6, WS=7;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"DEPOSIT", "WITHDRAW", "BYE", "NUM", "DIGIT", "ID", "WS"
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


	public transact2Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "transact2.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\tR\b\1\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\3\2\3\2\3\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3"+
		"\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\67\n\4\3\5"+
		"\6\5:\n\5\r\5\16\5;\3\6\3\6\3\7\6\7A\n\7\r\7\16\7B\3\7\3\7\3\7\3\7\3\7"+
		"\5\7J\n\7\3\b\6\bM\n\b\r\b\16\bN\3\b\3\b\2\2\t\3\3\5\4\7\5\t\6\13\7\r"+
		"\b\17\t\3\2\6\3\2\62;\3\2c|\3\2C\\\5\2\13\f\17\17\"\"\2Y\2\3\3\2\2\2\2"+
		"\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2"+
		"\2\3\21\3\2\2\2\5\25\3\2\2\2\7\66\3\2\2\2\t9\3\2\2\2\13=\3\2\2\2\rI\3"+
		"\2\2\2\17L\3\2\2\2\21\22\7f\2\2\22\23\7g\2\2\23\24\7r\2\2\24\4\3\2\2\2"+
		"\25\26\7y\2\2\26\27\7k\2\2\27\30\7v\2\2\30\31\7j\2\2\31\32\7f\2\2\32\33"+
		"\7t\2\2\33\34\7c\2\2\34\35\7y\2\2\35\6\3\2\2\2\36\37\7d\2\2\37 \7{\2\2"+
		" \67\7g\2\2!\"\7u\2\2\"#\7q\2\2#$\7n\2\2$%\7q\2\2%&\7p\2\2&\67\7i\2\2"+
		"\'(\7u\2\2()\7g\2\2)*\7g\2\2*+\7{\2\2+\67\7c\2\2,-\7n\2\2-.\7c\2\2./\7"+
		"v\2\2/\60\7g\2\2\60\67\7t\2\2\61\62\7c\2\2\62\63\7f\2\2\63\64\7k\2\2\64"+
		"\65\7q\2\2\65\67\7u\2\2\66\36\3\2\2\2\66!\3\2\2\2\66\'\3\2\2\2\66,\3\2"+
		"\2\2\66\61\3\2\2\2\67\b\3\2\2\28:\5\13\6\298\3\2\2\2:;\3\2\2\2;9\3\2\2"+
		"\2;<\3\2\2\2<\n\3\2\2\2=>\t\2\2\2>\f\3\2\2\2?A\t\3\2\2@?\3\2\2\2AB\3\2"+
		"\2\2B@\3\2\2\2BC\3\2\2\2CJ\3\2\2\2DE\t\4\2\2EF\5\13\6\2FG\5\13\6\2GH\5"+
		"\13\6\2HJ\3\2\2\2I@\3\2\2\2ID\3\2\2\2J\16\3\2\2\2KM\t\5\2\2LK\3\2\2\2"+
		"MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\b\b\2\2Q\20\3\2\2\2\b\2\66"+
		";BIN\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}