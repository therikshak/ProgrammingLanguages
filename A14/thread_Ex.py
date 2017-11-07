import time
import threading

number_of_adds = 10000000
result_list = []

global_sum = 0


def addToGlobalNTimes(n_times):
    global global_sum

    for _ in range(n_times):
        global_sum += 1


def runSimpleTiming(n_created_threads, n_adds):
    start = time.time()

    t1 = threading.Thread(target=addToGlobalNTimes, args=n_adds)
    t1.start()
    t1.join()

    end = time.time()

    total_time = end - start

    total_time = int((total_time * 1000)) / 1000.0

    result_tuple = (n_created_threads, total_time, global_sum)
    result_list.append(result_tuple)


if __name__ == "__main__":
    global_sum = 0
    n_created_threads = 0
    runSimpleTiming(n_created_threads, number_of_adds)

    print(result_list)
