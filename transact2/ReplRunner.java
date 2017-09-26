import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;

public class ReplRunner {
	
	public static void main(String[] args) throws Exception {
		InputStream is = System.in;

		BufferedReader br = new BufferedReader(new InputStreamReader(is));
		String expr       = br.readLine();

		// CHANGE BELOW
		transact2Parser parser = new transact2Parser(null);

		parser.setBuildParseTree(false);

		while(expr!=null) {
			ANTLRInputStream input = new ANTLRInputStream(expr+"\n");

			//CHANGE BELOW
			transact2Lexer lexer = new transact2Lexer(input);

			CommonTokenStream tokens = new CommonTokenStream(lexer);

			parser.setInputStream(tokens);

			//CHANGE BELOW
			parser.transaction();

			expr = br.readLine();
		}
	}
}