class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = 0
        r = position[-1] - position[0]
        answer = 0

        while l <= r:
            mid = (l+r)//2
            if self.canFitAllBalls(position,mid,m):
                answer = mid
                l = mid + 1 
            else:
                r = mid - 1
        
        return answer
        
    def canFitAllBalls(self,position,max_gap,m):
        if len(position) < 1:
            return False
        
        cur_position = position[0]
        m -= 1
        for p in position:
            if p-cur_position >= max_gap:
                cur_position = p
                m -= 1
                if m == 0:
                    return True
        
        return False
            
