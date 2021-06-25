class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        i,j = 0,0
        slots1.sort()
        slots2.sort()
        while i < len(slots1) and j < len(slots2):
            m_start = max(slots1[i][0],slots2[j][0])
            m_end = min(slots1[i][1],slots2[j][1])
            if m_start + duration <= m_end:
                return [m_start, m_start+duration]
            elif m_start < m_end:
                if slots2[j][1] < slots1[i][1]:
                    j += 1
                else:
                    i += 1
            else:
                if slots1[i][1] < slots2[j][0]:
                    i += 1
                else:
                    j += 1
        
        return []
