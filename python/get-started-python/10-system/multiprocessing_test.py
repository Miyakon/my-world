import multiprocessing
import os
import time

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        time.sleep(1)
        p = multiprocessing.Process(target=do_this,
            args=("I'm function %s" % n,))
        p.start()
