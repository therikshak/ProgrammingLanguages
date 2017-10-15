import unittest
from Publisher import Publisher

class Dummy(object):
	def notify(info):
		print("Notified with %s" % info)

class BigDummy(object):
	pass

class PublisherTest(unittest.TestCase):

	def testAddSubscriber1(self):
		# tests that a valid object is added
		pub = Publisher()
		dum = Dummy()
		pub.addSubscriber(dum)
		self.assertEqual(len(pub.getSubscriberList()), 1)

	def testAddSubscriber2(self):
		# tests to make sure invalid object not added
		pub = Publisher()
		dum = BigDummy()
		pub.addSubscriber(dum)
		self.assertEqual(len(pub.getSubscriberList()), 0)

	def testRemoveSubscriber1(self):
		# tests to see if subscriber in list is removed
		pub = Publisher()
		dum1 = Dummy()
		dum2 = Dummy()
		pub.addSubscriber(dum1)
		pub.addSubscriber(dum2)
		pub.removeSubscriber(dum2)
		self.assertEqual(len(pub.getSubscriberList()), 1)

	def testRemoveSubscriber2(self):
		# tests to make sure nothing is removed since not in list
		pub = Publisher()
		dum1 = Dummy()
		dum2 = Dummy()
		notAdded = BigDummy()
		pub.addSubscriber(dum1)
		pub.addSubscriber(dum2)
		pub.removeSubscriber(notAdded)
		self.assertEqual(len(pub.getSubscriberList()), 2)

	def testGetSubscriberList(self):
		pub = Publisher()
		dum1 = Dummy()
		dum2 = Dummy()
		pub.addSubscriber(dum1)
		pub.addSubscriber(dum2)
		list1 = pub.getSubscriberList()
		list2 = [dum1, dum2]
		self.assertCountEqual(list1, list2)

if __name__ == '__main__':
	unittest.main()