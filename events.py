import time
from threading import Thread, Event, Lock
from random import randint
import queue

data_recived = Event()
data_stored = Event()
end = Event()
lock = Lock()


def recive_data():
    global data
    while not end.is_set():
        data_stored.wait()
        inp = input('введите данные(0 -для выхода):')
        if inp == '0':
            end.set()
        with lock:
            data = inp
        data_stored.clear()
        data_recived.set()


def store_data():
    global data
    while not end.is_set():
        data_recived.wait()
        time.sleep(3)
        print('данные: ',data)
        data_stored.set()
        data_recived.clear()


data=''
data_stored.set()
t1 = Thread(target=recive_data)
t2 = Thread(target=store_data)


t1.start()
t2.start()


t1.join()
t2.join()

print('the end')
