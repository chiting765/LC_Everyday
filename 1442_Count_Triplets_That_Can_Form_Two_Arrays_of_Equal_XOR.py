class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        xors = [0]
        for item in arr:
            xors.append(xors[-1] ^ item)
        
        #print(xors)
        count = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                for k in range(j,len(arr)):
                    a = xors[i] ^ xors[j]
                    b = xors[j] ^ xors[k+1]
                    #print(i,j,k,a,b)
                    if a == b:
                        count += 1
        return count
