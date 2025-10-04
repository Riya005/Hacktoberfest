class HashMap:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.data = [[] for _ in range(capacity)]
    
    def _hash(self, key):
        return hash(key) % self.capacity
    
    def put(self, key, value):
        idx = self._hash(key)
        bucket = self.data[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
    
    def get(self, key):
        idx = self._hash(key)
        bucket = self.data[idx]
        for (k, v) in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key):
        idx = self._hash(key)
        bucket = self.data[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
