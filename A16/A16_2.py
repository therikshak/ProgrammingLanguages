import time
import threading
from threading import Thread
from urllib.request import urlopen
import re, sys

#our global var
globalSum = 0

#Lock variable if needed
lock = threading.Lock()

def readUrlFindNums(url):
    global globalSum

    response = urlopen(url)
    content = response.readline().decode('utf-8')
    #extract all numbers in the text
    numList = re.findall('\d+', content)

    #lock.acquire()
    for num in numList:
        globalSum += int(num)
    #lock.release()

def read100UrlsInMainThread(baseurl):
    global globalSum

    for i in range(0, 99, 1):
        url = baseurl + str(i)
        readUrlFindNums(url)

def read100UrlsWithMUltipleThreads(baseurl):
    #List to hold references to thread objects
    threadWorker = []

    # Create thread objects - add to list
    for i in range(0, 99, 1):
        url = baseurl + str(i)
        threadWorker.append(Thread(target=readUrlFindNums, args=(url,)))

    # Asynchronous calls to launch all threads
    for i in range(0, 99, 1):
        threadWorker[i].start()

    # Wait until all threads have completed their work
    for i in range(0, 99, 1):
        threadWorker[i].join()

#main computes the time it takes to perform calculations
if __name__ == "__main__":
    baseUrl = "http://s2.smu.edu/~coyle/cse3342/testfiles/twestf"

    # Timing on main thread doing 100 IOs
    globalSum = 0
    start = time.time()
    read100UrlsInMainThread(baseUrl)
    end = time.time()
    timeMainThread = end - start
    print("Main Thread 100 reads: time=%.3f globalSum=%d" % (timeMainThread,
    globalSum))

    # do with threads No Locks
    globalSum = 0
    nThreads = 100
    start = time.time()
    read100UrlsWithMUltipleThreads(baseUrl)
    end = time.time()
    timeMultiThreads = end - start
    print("Multiple Threads Threads:%d time=%.3f globalSum=%d" %
        (nThreads, timeMultiThreads, globalSum))