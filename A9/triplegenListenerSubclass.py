from antlr4 import *
from triplegenListener import triplegenListener

# overrides do nothing methods of triplegenListener

class triplegenListenerSubclass(triplegenListener):

	# enter parse tree produced by parser
	def enterPhrase(self, ctx):
		# instantiates num_words variable
		print ('Entering Phrase...')
		self.num_words = 0

	def exitPhrase(self, ctx):
		# print out word count after finished parsing the phrase
		print ('Finished...Number of words parsed is %s' % self.num_words)

	def enterWord(self, ctx):
		# increment the word count when listener sees a word
		self.num_words += 1