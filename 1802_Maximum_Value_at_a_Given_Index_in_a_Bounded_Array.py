class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 1
        r = maxSum
        while l <= r:
            m = (l + r) // 2
            total = self.getSum(n,index,m,index+1) + self.getSum(n,index,m,n-index) - m
            if total > maxSum:
                r = m - 1
            else:
                ans = m
                l = m + 1        
        
        return ans
    
    def getSum(self,n,index,index_val,length):
        if length <= index_val:
            return (index_val + index_val-length+1) / 2 * length
        else:
            return (index_val + 1) / 2 * index_val + (length - index_val)
            
