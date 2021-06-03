class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for index, n in enumerate(nums):
            greater_count = len(nums) - index
            if greater_count <= n and (index == 0 or greater_count > nums[index-1]):
                return greater_count
        
        return -1
