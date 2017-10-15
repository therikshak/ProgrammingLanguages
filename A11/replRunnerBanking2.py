# modified from 'replRunnerTarzan2.py'
# @__author__ = 'Erik Stryshak'
# @__sid__ = '41069864'
from antlr4 import *

from banking2Lexer    import banking2Lexer
from banking2Parser   import banking2Parser
from banking2Listener import banking2Listener
from banking2ListenerSubClass import banking2ListenerSubClass

def main():

    # instantiate our Listener to react to input in the REPL	
    myListener = banking2ListenerSubClass()
    
    # get the first line of input from our user
    # raw_input strips the \n AND does not eval string as python input(..) does
    print ("Welcome to this banking application")
    print ("enter q to quit ..starting REPL")
    inString = input('>>') + '\n'
    
    # set up the REPL loop
    while inString[0] != "q":
    
    	#setup input string in a stream for Antlr
        inStream = InputStream(inString)	

	#build a new lexer and a stream for the tokens found
        lexer = banking2Lexer(inStream)
        stream = CommonTokenStream(lexer)

	#create a Parser based on the token stream 
        myParser = banking2Parser(stream)
	
	#ask the Parser for a parse tree that we can navigate
        tree = myParser.transaction()

	#get a generic tree walker 
        walker = ParseTreeWalker()
	
	#feed the tree walker our Listener code and the parse tree
        walker.walk(myListener, tree)

	# what happens now depends on the code in the Listener
	
	# get another input to our REPL
        inString = input('>>') + '\n'

if __name__ == '__main__':
    main()

