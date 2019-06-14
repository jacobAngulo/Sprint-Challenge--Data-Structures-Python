class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        if None in self.storage:
            for i in range(len(self.storage)):
                if self.storage[i] == None:
                    self.storage[i] = item
                    return
        else:
            self.storage[self.current] = item
            self.current += 1
            self.current % (self.capacity - 1)

    def get(self):
        temp = []
        for i in self.storage:
            if i is not None:
                temp.append(i)
        return temp
