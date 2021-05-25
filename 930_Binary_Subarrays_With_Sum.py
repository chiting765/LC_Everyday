class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = 0
        cur_sum = 0
        sums = {0:1}
        for n in nums:
            print(sums)
            cur_sum += n
            if cur_sum >= goal:
                count += sums[cur_sum - goal]
            sums[cur_sum] = sums.get(cur_sum,0) + 1
        return count
