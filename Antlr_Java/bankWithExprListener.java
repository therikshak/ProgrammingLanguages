// Generated from bankWithExpr.g4 by ANTLR 4.7

  import java.util.*; 

import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link bankWithExprParser}.
 */
public interface bankWithExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link bankWithExprParser#transaction}.
	 * @param ctx the parse tree
	 */
	void enterTransaction(bankWithExprParser.TransactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link bankWithExprParser#transaction}.
	 * @param ctx the parse tree
	 */
	void exitTransaction(bankWithExprParser.TransactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link bankWithExprParser#deposit}.
	 * @param ctx the parse tree
	 */
	void enterDeposit(bankWithExprParser.DepositContext ctx);
	/**
	 * Exit a parse tree produced by {@link bankWithExprParser#deposit}.
	 * @param ctx the parse tree
	 */
	void exitDeposit(bankWithExprParser.DepositContext ctx);
	/**
	 * Enter a parse tree produced by {@link bankWithExprParser#withdraw}.
	 * @param ctx the parse tree
	 */
	void enterWithdraw(bankWithExprParser.WithdrawContext ctx);
	/**
	 * Exit a parse tree produced by {@link bankWithExprParser#withdraw}.
	 * @param ctx the parse tree
	 */
	void exitWithdraw(bankWithExprParser.WithdrawContext ctx);
	/**
	 * Enter a parse tree produced by {@link bankWithExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(bankWithExprParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link bankWithExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(bankWithExprParser.ExprContext ctx);
}