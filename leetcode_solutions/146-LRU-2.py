class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.cache = {}
        

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            self.list.remove(key)
            self.list.append(key)
            return value
        except KeyError:
            return -1

    def put(self, key, value):
        try:
            self.cache.pop(key)
            self.list.remove(key)
        except KeyError:
            if len(self.list) >= self.capacity:
                key_to_remove = self.list[0]
                self.list.remove(key_to_remove)
                self.cache.pop(key_to_remove)
        self.cache[key] = value
        self.list.append(key)
