// Generated from tarzan.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link tarzanParser}.
 */
public interface tarzanListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link tarzanParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(tarzanParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link tarzanParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(tarzanParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link tarzanParser#noun}.
	 * @param ctx the parse tree
	 */
	void enterNoun(tarzanParser.NounContext ctx);
	/**
	 * Exit a parse tree produced by {@link tarzanParser#noun}.
	 * @param ctx the parse tree
	 */
	void exitNoun(tarzanParser.NounContext ctx);
	/**
	 * Enter a parse tree produced by {@link tarzanParser#verb}.
	 * @param ctx the parse tree
	 */
	void enterVerb(tarzanParser.VerbContext ctx);
	/**
	 * Exit a parse tree produced by {@link tarzanParser#verb}.
	 * @param ctx the parse tree
	 */
	void exitVerb(tarzanParser.VerbContext ctx);
	/**
	 * Enter a parse tree produced by {@link tarzanParser#mod}.
	 * @param ctx the parse tree
	 */
	void enterMod(tarzanParser.ModContext ctx);
	/**
	 * Exit a parse tree produced by {@link tarzanParser#mod}.
	 * @param ctx the parse tree
	 */
	void exitMod(tarzanParser.ModContext ctx);
}