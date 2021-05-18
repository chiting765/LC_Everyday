class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for index, item in enumerate(s):
            if item == "(":
                stack.append(item)
            elif item == ")":
                if s[index-1] == "(":
                    score += 2 ** (len(stack)-1)
                stack.pop(-1)
                
        return score
