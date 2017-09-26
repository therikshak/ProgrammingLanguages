import org.antlr.v4.runtime.ANTLRInputStream;
import org.antlr.v4.runtime.CommonTokenStream;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;

/** To adapt this ReplRunner for your grammar change all occurrences of:
 *  bankWithExprParser TO <YourGrammarName>Parser
 *  bankWithExprLexer  TO <YourGrammarName>Lexer
 *  parser.prog()    TO parser.<YourTopLevelrule>()
 *
 *  Note: Enter 'bye' or 'quit' to terminate ReplRunner
 *        see code at end of loop
 */

public class ReplRunnerBankWithExpr {

    public static void main(String[] args) throws Exception {


	 // Use System.in to get input from the command line
     InputStream is = System.in;

     // BufferedReader let's us read one line at a time using readline()
     BufferedReader br = new BufferedReader(new InputStreamReader(is));

     // Prompt User
     System.out.println("ReplRunner : type 'bye' or 'quit' to terminate");
     System.out.print(">>>");
     String expr       = br.readLine() + '\n';          // get first line of input


	// STRATEGY: create ONE Parser that we will reuse for each line of input
	//           then we will instantiate a new LEXER for each input string
	//           This will give a REPL that responds to each line of input

	//  ** The parser name should vary depending on your grammar name
	bankWithExprParser parser = new bankWithExprParser(null); // share single parser

  	parser.setBuildParseTree(false);          		 // don't need to see tree

    // LOOP: keep looking for input - create a new LEXER in each loop iteration
    while ( expr!=null ) {             // while more input
       // create ANTLR input from the string we got from the user
       ANTLRInputStream input = new ANTLRInputStream(expr);

       //  ** The lexer name should vary depending on your grammar name
       bankWithExprLexer lexer = new bankWithExprLexer(input);

       // Lexer creates a token stream based on the input string
       CommonTokenStream tokens = new CommonTokenStream(lexer);

       // Feed the TOKENS to the parser
       parser.setInputStream(tokens); // notify parser of new token stream

       // ** Tell the parser your top level rule
       parser.transaction();              // start the parser to match top level rule

       //One REPL line now done. Get more text from our user
       System.out.print(">>>");
       expr = br.readLine() + '\n';             // see if there's another line

       // Does user want to quit?
       if (expr.startsWith("quit") || expr.startsWith("bye") ) break;

    }
  }
}



