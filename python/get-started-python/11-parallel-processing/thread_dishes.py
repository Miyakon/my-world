import threading, queue
import time

def washer(dishes, dish_queue):
    for dish in dishes:
        print("Washing", dish)
        time.sleep(1)
        dish_queue.put(dish)

def dryer(dish_queue: queue.Queue):
    while True:
        print("roop start")
        try:
            dish = dish_queue.get(timeout=10)
        except queue.Empty as e:
            print("EOB")
            break
        print("Drying", dish)
        time.sleep(3)
        dish_queue.task_done()
        print("roop end")

if __name__ == "__main__":
    dish_queue = queue.Queue()
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes = ['salada', 'bread', 'entree', 'desert']
    washer(dishes, dish_queue)
    dish_queue.join()
