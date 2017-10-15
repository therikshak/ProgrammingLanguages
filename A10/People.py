# People Classes
# @author Erik Stryshak
# @sid 41069864

class Manager(object):

	def __init__(self):
		pass

class Reporter(Manager):
	
	def __init__(self, name):
		self.name = name

	def notify(self, info):
		if("python" in info.lower()):
			print("{} reports: {}".format(self.name, info))

class NewsFan(Manager):
	
	def __init__(self, name):
		self.name = name

	def notify(self, info):
		print("{} tweets new news: {}".format(self.name, info))

class Bozo(Manager):
	
	def __init__(self, name):
		self.name = name
