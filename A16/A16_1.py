import time
import threading
from threading import Thread

# Code to compare the performance of a single main thread vs multiple threads
# in performing simple addition for threads with shared memory

# global variable that is updated by our threads
globalSum = 0
#lock1 = threading.Lock()

#Code to add to a global variable nTimes
def addToGlobalNTimes(nTimes):
    global globalSum

    #lock1.acquire()
    for _ in range(nTimes):
        globalSum += 1
    #lock1.release()

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

    data_points = 1
    #Total Number of additions
    nTimes = 10000000

    time_array1 = []
    time_array2 = []
    time_array3 = []
    time_array4 = []

    for _ in range(data_points):
        start = time.time()
        runInMainThread(nTimes)
        end = time.time()
        timeMainThread = end - start
        time_array1.append(end-start)

    timeMainThread = sum(time_array1)/len(time_array1)
    print("Main Thread:  time=%.3f globalSum=%d" % (timeMainThread, globalSum))


    nThreads = 1
    for _ in range(data_points):
        start = time.time()
        runMultiThreads(nThreads, nTimes)
        end = time.time()
        time_array2.append(end - start)

    timeMultiThreads = sum(time_array2) / len(time_array2)
    print ("Num Threads:%d  time=%.3f globalSum=%d" %
              (nThreads, timeMultiThreads, globalSum)  )

    nThreads = 4
    for _ in range(data_points):
        start = time.time()
        runMultiThreads(nThreads, nTimes)
        end = time.time()
        # print(end - start)
        time_array3.append(end - start)

    timeMultiThreads = sum(time_array3) / len(time_array3)
    print("Num Threads:%d  time=%.3f globalSum=%d" %
          (nThreads, timeMultiThreads, globalSum))

    nThreads = 16
    for _ in range(data_points):
        start = time.time()
        runMultiThreads(nThreads, nTimes)
        end = time.time()
        # print(end - start)
        time_array4.append(end - start)

    timeMultiThreads = sum(time_array4) / len(time_array4)
    print("Num Threads:%d  time=%.3f globalSum=%d" %
          (nThreads, timeMultiThreads, globalSum))
