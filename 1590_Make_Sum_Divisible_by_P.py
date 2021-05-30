class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0:
            return 0

        sum_rmd_dict = {0:-1}
        sum_rmd = 0
        length = len(nums)

        for index, num in enumerate(nums):
            sum_rmd = (sum_rmd + num) % p
            diff_sum_rmd_and_rmd = (sum_rmd - remainder) % p
            if diff_sum_rmd_and_rmd in sum_rmd_dict:
                length = min(length, index - sum_rmd_dict[diff_sum_rmd_and_rmd])
            sum_rmd_dict[sum_rmd] = index

        if length == len(nums):
            length = -1
        
        return length
