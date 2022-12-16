import threading
import time


def function1():
    # function to print cube of given num
    print("Vous avez attendu 2sc")
 
 
def function2():
    # function to print square of given num
    print("2sc d'attentes")
    time.sleep(2)
 
if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=function2)
    t2 = threading.Thread(target=function1)
 
    # starting thread 1
    t1.start()
    # wait until thread 1 is completely executed
    t1.join()

    # starting thread 2
    t2.start()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("Done!")