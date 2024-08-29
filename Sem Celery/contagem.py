import threading
import time

#Thread 1
def thread1():
    for i in range(1,6):
        print(f"Thread 1: {i}")
        time.sleep(1)

#Thread 2
def thread2():
    for i in range(1,6):
        print(f"Thread 2: {i}")
        time.sleep(2)

thread1 = threading.Thread(target=thread1)
thread2 = threading.Thread(target=thread2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Cabo (;-;)")
