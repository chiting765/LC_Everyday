class Bucket:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        found = False
        for index, [k,v] in enumerate(self.bucket):
            if k == key:
                self.bucket[index] = [k,value]
                found = True
        
        if not found:
            self.bucket.append([key,value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        for k, v in self.bucket:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for index, [k,v] in enumerate(self.bucket):
            if k == key:
                self.bucket.remove([k,v])
        
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyrange = 769
        self.buckets = [Bucket() for i in range(self.keyrange)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_index = key % self.keyrange
        self.buckets[hash_index].put(key,value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_index = key % self.keyrange
        return self.buckets[hash_index].get(key)

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """ 
        hash_index = key % self.keyrange
        self.buckets[hash_index].remove(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
