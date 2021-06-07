class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l = min(sweetness)
        r = sum(sweetness)
        answer = 0
        
        while l <= r:
            mid = l + (r-l) //2
            if self.isValid(sweetness,K+1,mid):
                l = mid + 1
                answer = mid
            else:
                r = mid - 1
            #print(l,r)
        return answer
    
    def isValid(self,sweetness, piece_count, max_for_me):
        cur_sum = 0
        for s in sweetness:
            cur_sum += s
            if cur_sum >= max_for_me:
                piece_count -= 1
                cur_sum = 0
                if piece_count == 0:
                    return True

        return False
        
