# Stack.py - implements a Stack Class
# @author Erik Stryshak
# @sid 41069864

class Stack:
	def __init__(self):
		self.stack_container = []
		self.size_var = 0

	def isEmpty(self):
		if(self.size_var == 0):
			return True
		return False

	def push(self, item):
		self.stack_container.append(item)
		self.size_var += 1

	def pop(self):
		self.size_var -= 1
		return self.stack_container.pop()

	def peek(self):
		if(self.size_var > 0):
			return self.stack_container[self.size_var - 1]

	def size(self):
		return self.size_var

	def stackAsList(self):
		return self.stack_container
