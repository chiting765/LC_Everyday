class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        i = 0
        sum_1_time = 0
        sum_total = 0
        max_satisfaction = float('-inf')
        
        while i < len(satisfaction):  
            sum_total += satisfaction[i] + sum_1_time
            sum_1_time += satisfaction[i]
            max_satisfaction = max(max_satisfaction,sum_total)
            i += 1
        return max(0,max_satisfaction)
            
