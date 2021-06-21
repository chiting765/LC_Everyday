class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [16]
        answer = 0
        for i, a in enumerate(arr):
            while a > stack[-1]:
                answer += stack[-1] * min(a,stack[-2])
                stack.pop()
            stack.append(a)

        while len(stack)>2:
            answer += stack.pop() * stack[-1]
        
        return answer
