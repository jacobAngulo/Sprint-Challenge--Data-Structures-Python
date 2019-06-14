class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if self.capacity:
            self.storage[self.current] = item
            self.current = (self.current + 1) % self.capacity 

    def get(self):
        temp = []
        for i in self.storage:
            if i is not None:
                temp.append(i)
        return temp
