class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        cur_product = 1
        count = 0
        max_length = 0
        first_negative_index = None
        
        for n in nums:
            if n == 0:
                cur_product = 1
                count = 0
                first_negative_index = None
            else:
                cur_product *= n
                count += 1
                if cur_product > 0:
                    max_length = max(max_length,count)
                else:
                    if first_negative_index == None:
                        first_negative_index = count
                    else:
                        max_length = max(max_length,count-first_negative_index)        
        return max_length
