from collections import OrderedDict


Class LRUImplementation():

    def __init__(self, capicity):
        self.capicity = capicity
        self.cache = OrderedDict()


    def get(self, key):
        if key in self.cache:
            val = self.cache[key]
            self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return None

    def set(self, key, value):
        if self.cache.has_key(key):
            value = self.cache.pop(key)
            self.cache[key] = value
        elif len(cache) <= self.capicity:
            self.cache[key] = value
        else:
            self.cache.pop(first = False)
            self.cache[key] = value
