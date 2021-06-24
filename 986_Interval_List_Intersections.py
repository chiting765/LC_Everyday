class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):        
            f = firstList[i]
            s = secondList[j]
            intersection_start = max(f[0],s[0])
            intersection_end = min(f[1],s[1])
            if intersection_start <= intersection_end:
                output.append([intersection_start,intersection_end])
                if f[1] < s[1]:
                    i += 1
                else:
                    j += 1
            elif f[1] < s[0]:
                i += 1
            else:
                j += 1
        
        return output
