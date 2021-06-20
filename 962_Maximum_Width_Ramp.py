class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        num_index = [(item, index) for index, item in enumerate(nums)]
        num_index.sort()
        
        result = 0
        min_index = len(nums)
        for item, i in num_index:
            result = max(result, i - min_index)
            min_index = min(min_index, i)
    
        return result
