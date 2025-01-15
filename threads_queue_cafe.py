import time
import threading
from random import randint
import queue

lock = threading.Lock()

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        time.sleep(randint(3, 9))
        print(f'{self.name} поел(-а)')



class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.q = queue.Queue()

        self.is_open = True
        threading.Thread(target=self.work_time).start()

    def work_time(self):
        print('We open!')
        time.sleep(30)
        print('Closing...')
        self.is_open = False

    def guest_arrival(self, guest):

        self.q.put(guest)
        print(f"{guest.name} в очереди. (перед ним {self.q.qsize()-1} человек.)")


    def serve_guests(self):

        while self.is_open or not self.q.empty() or len(list(filter(lambda table: table.guest is not None, self.tables))) >0:
            for table in self.tables:
                if table.guest is None:
                    # with lock:
                    if self.q.empty():
                        continue
                    table.guest = self.q.get()
                    print(f"{table.guest.name} Сел(-а) за стол номер {table.number}")
                    table.guest.start()

                elif not table.guest.is_alive():
                    print(f"{table.guest.name} уходит")
                    # with lock:
                    table.guest = None
                    print(f"Стол номер {table.number} свободен")
                # else:
                #     if not self.is_open and  self.q.empty():
                #         for table in list(filter(lambda table: table.guest is not None, self.tables)):
                #             print(table.guest.name)




def arrival(cafe):
    # Имена гостей
    guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
    for name in guests_names:
        g= Guest(name)
        cafe.guest_arrival(g)
    i=0
    j=0
    while cafe.is_open:
        i+=1
        j=(j+1)%len(guests_names)
        time.sleep(randint(1,4))
        # Создание гостей
        guest = Guest(guests_names[j]+'_'+str(i))

        # Приём гостей
        cafe.guest_arrival(guest)




# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Заполнение кафе столами
cafe = Cafe(*tables)


t1 = threading.Thread(target=arrival, args=(cafe,))
t2 = threading.Thread(target=cafe.serve_guests)


t1.start()
t2.start()


t1.join()
t2.join()

print('the end')
