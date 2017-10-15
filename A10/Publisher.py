# Publisher and CyberNews Class
# @author Erik Stryshak
# @sid 41069864

from Stack import Stack

class Publisher(object):

	def __init__(self):
		self.subscriberList = []

	def addSubscriber(self, s):
	# check if notify is implemented and add subscriber
		if(hasattr(s, 'notify')):
			self.subscriberList.append(s)

	def removeSubscriber(self, s):
	# trys to remove a subscriber, will catch a Value Error if the
	# subscriber is not in the list
		try:
			self.subscriberList.remove(s)
		except ValueError:
			pass

	def notifySubscribers(self, info):
	# call notify method for each subscriber
		for subscriber in self.subscriberList:
			subscriber.notify(info)

	def getSubscriberList(self):
		return self.subscriberList

class CyberNews(Publisher):

	def __init__(self):
		# call superclass constructor and make a news stack
		Publisher.__init__(self)
		self.news_stack = Stack()

	def putNews(self, news):
		self.news_stack.push(news)

	def pullRecent(self):
		# use superclass method to notify all subscribers
		Publisher.notifySubscribers(self, self.news_stack.pop())