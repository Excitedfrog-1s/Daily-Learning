from threading import Thread
import time

def counter():
    i = 0
    for _ in range(1000000000):
        i = i + 1
        return True

def main():
    thread_array = {}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=counter)
        t.start()
        t.join()
    end_time = time.time()
    print("Total time: {}".format(end_time-start_time))

main()
