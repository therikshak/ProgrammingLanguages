#  Code to use a Listener to count number of words from TripleGen 
from antlr4 import *

from triplegenLexer    import triplegenLexer
from triplegenParser   import triplegenParser
from triplegenListener import triplegenListener
from triplegenListenerSubclass import triplegenListenerSubclass
from TripleGen  import TripleGen

def main():
        # instantiate our Listener to react to input in the REPL	
        myListener = triplegenListenerSubclass() 

        tgen = TripleGen("[bcdfgmnpr][aeiou][stwxyz]", 285)
	  	
        wordList = tgen.getList()
   	
   	#TODO: create wordsBigString from wordList
        wordsBigString = ' '.join(wordList)      
   
	#setup input string in a stream for Antlr
        inStream = InputStream(wordsBigString)	

	#build a new lexer and a stream for the tokens found
        lexer = triplegenLexer(inStream )
        stream = CommonTokenStream(lexer)

	#create a Parser based on the token stream 
        myParser = triplegenParser(stream)

	#ask the Parser for a parse tree that we can navigate
        tree   = myParser.phrase()

	#get a generic tree walker 
        walker     = ParseTreeWalker()

	#feed the tree walker our Listener code and the parse tree
        walker.walk(myListener, tree)

	# what happens now depends on the code in the Listener



if __name__ == '__main__':
    main()

