// Generated from saystuff.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link saystuffParser}.
 */
public interface saystuffListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link saystuffParser#stmt}.
	 * @param ctx the parse tree
	 */
	void enterStmt(saystuffParser.StmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link saystuffParser#stmt}.
	 * @param ctx the parse tree
	 */
	void exitStmt(saystuffParser.StmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link saystuffParser#infostmt}.
	 * @param ctx the parse tree
	 */
	void enterInfostmt(saystuffParser.InfostmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link saystuffParser#infostmt}.
	 * @param ctx the parse tree
	 */
	void exitInfostmt(saystuffParser.InfostmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link saystuffParser#hellostmt}.
	 * @param ctx the parse tree
	 */
	void enterHellostmt(saystuffParser.HellostmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link saystuffParser#hellostmt}.
	 * @param ctx the parse tree
	 */
	void exitHellostmt(saystuffParser.HellostmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link saystuffParser#byestmt}.
	 * @param ctx the parse tree
	 */
	void enterByestmt(saystuffParser.ByestmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link saystuffParser#byestmt}.
	 * @param ctx the parse tree
	 */
	void exitByestmt(saystuffParser.ByestmtContext ctx);
}