import time
import threading
from threading import Thread

# Code to compare the performance of a single main thread vs multiple threads
# in performing simple addition for threads with shared memory

# global variable that is updated by our threads
globalSum = 0
lock1 = threading.Lock()

#Code to add to a global variable nTimes
def addToGlobalNTimes(nTimes):
    global globalSum

    lock1.acquire()
    for _ in range(nTimes):
        globalSum += 1
    lock1.release()

def runInMainThread(nTimes):
    'Update global variable in the  main thread'

    global globalSum
    globalSum = 0

    #main thread does the work
    addToGlobalNTimes(nTimes)


def runMultiThreads(nThreads, nTimes):
    'Divide the problem across nThreads'
    global globalSum
    globalSum = 0      #reset globalSum

    #divide work among threads
    workPerThread = int(nTimes/nThreads)

    #List to hold references to thread objects
    threadWorker = []

    # Create thread objects - add to list
    for i in range(nThreads):
        threadWorker.append(Thread(target=addToGlobalNTimes, args=(workPerThread,)))

    # Asynchronous calls to launch all threads
    for i in range(nThreads):
        threadWorker[i].start()

    # Wait until all threads have completed their work
    for i in range(nThreads):
        threadWorker[i].join()


#main computes the time it takes to perform calculations
if __name__ == "__main__":

    #Total Number of additions
    nTimes = 10000000

    #Execute code in main thread    --------------------------
    start = time.time()
    runInMainThread(nTimes)
    end   = time.time()
    timeMainThread = end - start
    print("Main Thread:  time=%.3f globalSum=%d" % (timeMainThread, globalSum))

    #Partition work across multiple threads  ----------------
    nThreads = 10
    start = time.time()
    runMultiThreads(nThreads, nTimes)
    end = time.time()
    timeMultiThreads = end - start
    print ("Num Threads:%d  time=%.3f globalSum=%d" %
              (nThreads, timeMultiThreads, globalSum)  )

    #Speedup?   ----------------------------------------------
    if (timeMultiThreads  <   timeMainThread):
        print ("SPEEDUP: %.2f " %
               ((timeMainThread / float(timeMultiThreads )*100 ))  )
    else:
        print  ("SLOWDOWN: %.2f Percent" %
                  ((float(timeMultiThreads )/ timeMainThread) *100)  )







