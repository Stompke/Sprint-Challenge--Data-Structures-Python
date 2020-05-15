class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.counter = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            # print('storage: ', self.storage)
            # print('counter : ',self.counter)
            if self.counter == self.capacity:
                self.counter = 0
                self.storage[self.counter] = item
                self.counter += 1
            else:
                self.storage[self.counter] = item
                self.counter += 1

        else:
            self.storage.append(item)
            self.counter += 1


    def get(self):
        return self.storage

# ring = RingBuffer(3)
# ring.append('a')
# ring.append('b')
# ring.append('c')


# print(ring.get())

# ring.append('d')

# print(ring.get())

# ring.append('e')
# ring.append('f')

# print(ring.get())




# ring.append('d')