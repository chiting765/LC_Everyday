class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            binary = str(bin(i))
            output.append(binary.count('1'))
        return output
            
