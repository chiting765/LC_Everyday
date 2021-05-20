class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        index_to_remove = []
        output_s = s
        for index, item in enumerate(s):
            if item == "(":
                stack.append(index)
            elif item == ")":
                if stack:
                    stack.pop()
                else:
                    index_to_remove.append(index)
        
        index_to_remove += stack
        if len(index_to_remove) > 0:
            output_s = "".join([s[i] for i in range(len(s)) if i not in index_to_remove])
            
        return output_s
        
