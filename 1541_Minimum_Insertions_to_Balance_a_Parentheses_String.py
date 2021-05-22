class Solution:
    def minInsertions(self, s: str) -> int:
        miss_left_count = 0
        miss_right_count = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "(":
                stack.append(s[i])
            else:
                if len(stack) > 0: 
                    if i < len(s) - 1 and s[i+1] == ")":
                        stack.pop()
                        i += 1
                    else:
                        stack.pop()
                        miss_right_count += 1
                else:
                    if i < len(s) - 1 and s[i+1] == ")":
                        miss_left_count += 1
                        i += 1
                    else:
                        miss_left_count += 1
                        miss_right_count += 1
            i += 1
        
        miss_right_count += len(stack) * 2      
        return int(miss_right_count +  miss_left_count)
                   
                
                    
            
