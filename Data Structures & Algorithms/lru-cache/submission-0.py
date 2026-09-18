from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.k = 0
        self.capacity = capacity
        self.lru = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.lru:
            self.lru.move_to_end(key, last=False)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = value
            self.lru.move_to_end(key, last=False)
        elif self.k >= self.capacity:
            self.lru.popitem(last=True)
            self.lru[key] = value
            self.lru.move_to_end(key, last=False)
        else:
            self.k += 1
            self.lru[key] = value
            self.lru.move_to_end(key, last=False)