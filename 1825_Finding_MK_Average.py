from sortedcontainers import SortedList
class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.queue = []
        self.small, self.middle, self.large = SortedList(),SortedList(),SortedList()

    def addElement(self, num: int) -> None:  
        self.queue.append(num)
        if len(self.queue) == self.m:
            if len(self.small) == 0:
                self.initialize()
        elif len(self.queue) > self.m:
            num_to_remove = self.queue.pop(0)  
            if num < self.small[-1]:
                self.small.add(num)   
                self.middle.add(self.small[-1])
                self.small.remove(self.small[-1])        
            elif num > self.large[0]:
                self.large.add(num)     
                self.middle.add(self.large[0])
                self.large.remove(self.large[0])                
            else:
                self.middle.add(num)
            
            if num_to_remove <= self.small[-1]:
                self.small.remove(num_to_remove)
                self.small.add(self.middle[0])
                self.middle.remove(self.middle[0])
            elif num_to_remove >= self.large[0]:
                self.large.remove(num_to_remove)
                self.large.add(self.middle[-1])
                self.middle.remove(self.middle[-1])
            else:
                self.middle.remove(num_to_remove)
            
    def initialize(self):
        sorted_queue = sorted(self.queue)
        for index, item in enumerate(sorted_queue):
            if index < self.k:
                self.small.add(item)
            elif index >= self.m - self.k:
                self.large.add(item)
            else:
                self.middle.add(item)
              
    def calculateMKAverage(self) -> int:
        if len(self.queue) < self.m:
            return -1      
        return int(sum(self.middle)/len(self.middle))

# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
