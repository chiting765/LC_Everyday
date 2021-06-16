class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0]
        for n in nums:
            presum.append(presum[-1] + n)
        
        right_min_index = [len(nums)] * len(nums)
        left_min_index = [-1]*len(nums)
        stack = []        
        i = 0
        
        while i < len(nums):     
            if not stack or nums[i] >= nums[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                right_min_index[stack.pop()] = i
                
        stack = []
        i = len(nums) - 1
        while i > -1:    
            if not stack:
                stack.append(i)
                i -= 1       
            elif nums[i] >= nums[stack[-1]]:
                stack.append(i)
                i -= 1      
            else:
                left_min_index[stack.pop()] = i
        
        max_product = 0
        for i in range(len(nums)):    
            max_product = max(max_product, (presum[right_min_index[i]] - presum[left_min_index[i]+1]) * nums[i])
        
        return max_product % (10**9 + 7)
