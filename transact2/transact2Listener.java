// Generated from transact2.g4 by ANTLR 4.7
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link transact2Parser}.
 */
public interface transact2Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link transact2Parser#transaction}.
	 * @param ctx the parse tree
	 */
	void enterTransaction(transact2Parser.TransactionContext ctx);
	/**
	 * Exit a parse tree produced by {@link transact2Parser#transaction}.
	 * @param ctx the parse tree
	 */
	void exitTransaction(transact2Parser.TransactionContext ctx);
	/**
	 * Enter a parse tree produced by {@link transact2Parser#deposit}.
	 * @param ctx the parse tree
	 */
	void enterDeposit(transact2Parser.DepositContext ctx);
	/**
	 * Exit a parse tree produced by {@link transact2Parser#deposit}.
	 * @param ctx the parse tree
	 */
	void exitDeposit(transact2Parser.DepositContext ctx);
	/**
	 * Enter a parse tree produced by {@link transact2Parser#withdraw}.
	 * @param ctx the parse tree
	 */
	void enterWithdraw(transact2Parser.WithdrawContext ctx);
	/**
	 * Exit a parse tree produced by {@link transact2Parser#withdraw}.
	 * @param ctx the parse tree
	 */
	void exitWithdraw(transact2Parser.WithdrawContext ctx);
}