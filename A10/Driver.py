# Driver for A10
# @author Erik Stryshak
# @sid 41069864

from Publisher import *
from People import *

def main():
	# create instances
	cy_news = CyberNews()
	rep = Reporter("Mr. Reporter Sir")
	n_fan = NewsFan("Young NewsFan")
	boz = Bozo("The Bozo")

	# add subscribers
	cy_news.addSubscriber(rep)
	cy_news.addSubscriber(n_fan)
	cy_news.addSubscriber(boz)

	# add news messages
	cy_news.putNews("Simula is cool")
	cy_news.putNews("PyTHon is cool")

	# pull the two news messages
	cy_news.pullRecent()
	cy_news.pullRecent()

if __name__ == "__main__":
    main()