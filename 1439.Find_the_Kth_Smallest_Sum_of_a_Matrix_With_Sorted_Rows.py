from heapq import heappush, heappop, heapify
import copy

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m,n = len(mat), len(mat[0])
        init_ids = [0] * m
        init_sum = sum([row[0] for row in mat])
        queue = [[init_sum, init_ids]]
        seen_ids = [init_ids]

        x = 1
        while x < k:
            #print(x, queue)
            cur_sum, cur_ids = heappop(queue)
            for i in range(m):
                next_ids = copy.deepcopy(cur_ids)
                next_ids[i] += 1
                if next_ids[i] < n and next_ids not in seen_ids:      
                    seen_ids.append(next_ids)
                    j = next_ids[i]
                    next_sum = cur_sum + mat[i][j] - mat[i][j-1]
                    heappush(queue, [next_sum, next_ids])   
            x += 1

        result_sum, ids = heappop(queue)
        return result_sum
