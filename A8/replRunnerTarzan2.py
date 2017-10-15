__author__ = 'frankcoyle'
#  SUCCESS in REPL framework  
from antlr4 import *

from tarzan2Lexer    import tarzan2Lexer
from tarzan2Parser   import tarzan2Parser
from tarzan2Listener import tarzan2Listener
from tarzan2ListenerSubclass import tarzan2ListenerSubclass


def main():

    # instantiate our Listener to react to input in the REPL	
    myListener = tarzan2ListenerSubclass()
    
    # get the first line of input from our user
    # raw_input strips the \n AND does not eval string as python input(..) does
    print ("enter q to quit ..starting REPL ")
    inString = input('>>') + '\n'
    
    # set up the REPL loop
    while inString[0] != "q":
    
    	#setup input string in a stream for Antlr
        inStream = InputStream(inString)	

	#build a new lexer and a stream for the tokens found
        lexer = tarzan2Lexer(inStream)
        stream = CommonTokenStream(lexer)

	#create a Parser based on the token stream 
        myParser = tarzan2Parser(stream)
	
	#ask the Parser for a parse tree that we can navigate
        tree = myParser.sentence()

	#get a generic tree walker 
        walker = ParseTreeWalker()
	
	#feed the tree walker our Listener code and the parse tree
        walker.walk(myListener, tree)

	# what happens now depends on the code in the Listener
	
	# get another input to our REPL
        inString = input('>>') + '\n'

if __name__ == '__main__':
    main()

