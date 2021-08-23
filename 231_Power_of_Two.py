class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 1:
            remain = n % 2
            if remain > 0:
                return False
            else:
                n = n / 2
        
        return True
