from antlr4 import *
from banking2Listener import banking2Listener
from Stack import Stack

class banking2ListenerSubClass(banking2Listener):

	def __init__(self):
		# initialize class with a stack a dictionary
		self.stack = Stack()
		self.dict = {}

	def enterDeposit(self, ctx):
		# initialize amount if user not in dictionary
		print("enter deposit")
		if(ctx.ID().getText() not in self.dict):
			self.dict[ctx.ID().getText()] = 0

	def exitDeposit(self, ctx):
		val = self.stack.pop()
		self.dict[ctx.ID().getText()] += val
		print("exit deposit", self.dict)

	def enterWithdraw(self, ctx):
		# initialize amount if user not in dictionary
		print("enter withdraw")
		if(ctx.ID().getText() not in self.dict):
			self.dict[ctx.ID().getText()] = 0

	def exitWithdraw(self, ctx):
		val = self.stack.pop()
		bal = int(self.dict[ctx.ID().getText()])
		if(val<=bal):
			self.dict[ctx.ID().getText()] -= val
		else:
			print("withdraw of {} larger than balance of {}".format(val, 
        		self.dict[ctx.ID().getText()]))
		print("exit deposit", self.dict)

	def enterDIV(self, ctx):
		print("enter div")

	def exitDIV(self, ctx):
		v1 = self.stack.pop()
		v2 = self.stack.pop()
		r = v1/v2
		self.stack.push(r)
		print("exit div")

	def enterADD(self, ctx):
		print("enter add")

	def exitADD(self, ctx):
		v1 = self.stack.pop()
		v2 = self.stack.pop()
		r = v1+v2
		self.stack.push(r)
		print("exit add")

	def enterSUB(self, ctx):
		print("enter sub")

	def exitSUB(self, ctx):
		v1 = self.stack.pop()
		v2 = self.stack.pop()
		r = v1-v2
		self.stack.push(r)
		print("exit sub")

	def enterPARENS(self, ctx):
		print("enter parens")

	def exitPARENS(self, ctx):
		print("exit parens")

	def enterMUL(self, ctx):
		print("enter mult")

	def exitMUL(self, ctx):
		v1 = self.stack.pop()
		v2 = self.stack.pop()
		r = v1*v2
		self.stack.push(r)
		print("exit mult")

	def enterNUM(self, ctx):
		print("enter num")

	def exitNUM(self, ctx):
		self.stack.push(int(ctx.NUM().getText()))
		print("exit num")

	def enterID(self, ctx):
		print("enter id")

	def exitID(self, ctx):
		if(ctx.ID().getText() in self.dict):
			self.stack.push(self.dict[ctx.ID().getText()])
		else:
			self.stack.push(0)
		print("exit id")
