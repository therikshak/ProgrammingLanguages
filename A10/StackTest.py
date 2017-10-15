import unittest
from Stack import Stack

class StackTest(unittest.TestCase):
	def testSize(self):
		stack = Stack()
		self.assertEqual(stack.size(),0)
	def testPush(self):
		stack = Stack()
		stack.push(2)
		self.assertEqual(stack.size(), 1)
	def testPop(self):
		stack = Stack()
		stack.push(2)
		v = stack.pop()
		self.assertEqual(v,2)
	def testPeek(self):
		stack = Stack()
		stack.push(3)
		stack.push(2)
		v = stack.peek()
		self.assertEqual(v, 2)
	def testPeek2(self):
		stack = Stack()
		stack.push(3)
		stack.push(2)
		v = stack.peek()
		self.assertEqual(v, 2)
	def testPeek3(self):
		stack = Stack()
		stack.push(3)
		stack.push(2)
		v = stack.peek()
		self.assertEqual(stack.size(),2)
	def testIsEmpty(self):
	 	stack = Stack()
	 	stack.push(3)
	 	stack.push(2)
	 	stack.pop()
	 	stack.pop()
	 	self.assertTrue(stack.isEmpty())
	 
	def testStackAsList(self):
		stack = Stack()
		stack.push(3)
		stack.push(2)
		list1 = stack.stackAsList()
		list2 = [3,2]
		self.assertEqual(list1,list2)

if __name__ == '__main__':
	unittest.main()