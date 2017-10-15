# Subclass of Generated tarzan2Listener

from antlr4 import *
from tarzan2Listener import tarzan2Listener

# This class overrides do-nothing methods of tarzan2Listener 
# Reacts to traversal of parse tree produced by tarzan2Parser.

class tarzan2ListenerSubclass(tarzan2Listener):
    # Enter a parse tree produced by tarzan2Parser#sentence.
    def enterSentence(self, ctx):
        print ('Beginning the walk of the parse tree')

    # Exit a parse tree produced by tarzan2Parser#PEOPLEFACT.
    def exitPEOPLEFACT(self, ctx):
        print ("hey %s" % ctx.PERSON().getText())
        if ctx.phrase() != None:
        	print ("I see you were  %s" % ctx.phrase().getText())
       

    # Exit a parse tree produced by tarzan2Parser#PLACEFACT.
    def exitPLACEFACT(self, ctx):
        print ("the %s is %s" %  (ctx.PLACE().getText(), ctx.ADJECTIVE().getText()))


    # Exit a parse tree produced by tarzan2Parser#PERSONQUERY.
    def exitPERSONQUERY(self, ctx):
        print ("Want to know about %s " % ctx.PERSON().getText())
        
        
    # Exit a parse tree produced by tarzan2Parser#PLACEQUERY.
    def exitPLACEQUERY(self, ctx):
        print ("Ah, life by the old %s " % ctx.PLACE().getText())
         
        

    # Enter a parse tree produced by tarzan2Parser#phrase.
    def enterPhrase(self, ctx):
        pass

    # Exit a parse tree produced by tarzan2Parser#phrase.
    def exitPhrase(self, ctx):
        pass


