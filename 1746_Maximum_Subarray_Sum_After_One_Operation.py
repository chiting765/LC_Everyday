class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        dp = [[0,0] for i in range(len(nums))]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0] ** 2
        
        result = max(dp[0][0], dp[0][1])
        
        for i in range(1,len(nums)):
            dp[i][0] = max(nums[i], nums[i] + dp[i-1][0])
            dp[i][1] = max(nums[i] ** 2, nums[i] ** 2 + dp[i-1][0], nums[i] + dp[i-1][1])
            result = max(result, dp[i][0],dp[i][1])
        
        return result
