class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.buckets = [[] for i in range(self.keyRange)]

    def add(self, key: int) -> None:
        index = key % self.keyRange
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.keyRange
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = key % self.keyRange
        if key in self.buckets[index]:
            return True
        else:
            return False
