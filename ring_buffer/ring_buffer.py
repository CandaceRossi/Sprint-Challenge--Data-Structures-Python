from collections import OrderedDict


class RingBuffer:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, item):
        self.item = item
        if item not in self.cache:
            return -1
        else:
            self.cache.move_to_end(item)
            return self.cache[item]

    def append(self, item, value):
        self.item = item
        self.value = value
        self.cache[item] = value
        self.cache.move_to_end(item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


cache = RingBuffer(2)
