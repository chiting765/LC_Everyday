class Solution:
    def longestValidParentheses(self, s: str) -> int:
        extra_right_index = []
        stack = []
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                if stack:
                    stack.pop()
                else:
                    extra_right_index.append(index)
        
        #print(stack, extra_right_index)
        not_valid_index = [-1, len(s)] + stack + extra_right_index
        not_valid_index.sort()
        
        max_length = 0
        for i in range(1,len(not_valid_index)):
            max_length = max(max_length, not_valid_index[i] - not_valid_index[i-1] - 1)
        
        return max_length
