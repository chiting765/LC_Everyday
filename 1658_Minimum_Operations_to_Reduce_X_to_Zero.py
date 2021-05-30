class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        left_sum_dict = {}
        left_sum = 0
        right_sum = total
        length = len(nums) + 1
        for i, num in enumerate(nums):
            left_sum += num
            right_sum -= num
            if left_sum == x:
                length = min(i+1,length)
            
            if right_sum == x:
                length = min(len(nums)-i-1, length)

            if (x - right_sum) in left_sum_dict.keys():
                length = min(length, len(nums) - i + left_sum_dict[x - right_sum])
            left_sum_dict[left_sum] = i
                 
        if length > len(nums):
            length = -1
        return length
