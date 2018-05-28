import time
from threading import Thread

class Manager:
    elevators = []

    def __init__(self,top_floor,bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor

    def add_elevators(self,*els):
        for i in els:
            self.elevators.append(i)

    def update_qs(self):
        qs = {}
        for e in self.elevators:
            qs[e.name] = e.queue
        with open("qs","w") as f1:
            f1.write(str(qs))

    def ping(self,cur_floor,floor):
        for e in self.elevators:
            if e.ping(cur_floor,floor):
                self.update_qs()
                return True
        return False

    def print_queues(self):
        for e in self.elevators:
            print(str(e.name),e.queue)

    def run_ele(self):
        with open("qs","r") as f1:
            qs = eval(f1.read())
        trds = []
        for e in self.elevators:
            e.queue = qs[e.name]
            if e.queue:
                trds.append(Thread(target=e.run))
        for t in trds:
            t.start()
        for t in trds:
            t.join()
        self.update_qs()

class Elevator():
    def __init__(self,name,e_floor,direction):
        self.name = name
        self.e_floor = e_floor
        self.direction = direction
        self.queue = []

    def rp(self,x):
        if x == 0: return 0
        return 1 if x > 0 else -1

    def add_queue(self,cur_floor,floor):
        if cur_floor not in self.queue: self.queue.append(cur_floor)
        if floor not in self.queue: self.queue.append(floor)
        rev = False
        if self.direction == -1:
            rev = True
        self.queue.sort(reverse=rev)

    def ping(self, cur_floor,floor):
        if self.direction == 0 or len(self.queue) == 0:
            self.direction = self.rp(floor - cur_floor)
            self.add_queue(cur_floor,floor)
            return True
        elif self.rp(floor - cur_floor) == self.direction == self.rp(cur_floor - self.e_floor):
                self.add_queue(cur_floor,floor)
                return True
        return False

    def move(self):
        if self.queue[0] == self.e_floor:
            self.queue = self.queue[1:]
            print("lift " + str(self.name) + " at floor " + str(self.e_floor))
            time.sleep(2)
        else:
            tow = self.queue[0] - self.e_floor
            self.direction = self.rp(tow)
            self.e_floor += self.direction

    def run(self):
        while self.queue:
            self.move()
        self.direction = 0


b = Manager(12,-2)
e1 = Elevator("E1",0,0)
e2 = Elevator("E2",10,-1)
b.add_elevators(e1,e2)
