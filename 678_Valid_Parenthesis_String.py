class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for index, item in enumerate(s):
            if item == "(":
                stack.append(index)
            elif item == "*":
                star.append(index)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    if len(star) > 0:
                        star.pop()
                    else:
                        return False
        
        if len(stack) > len(star):
            return False
    
        while stack:
            if  stack.pop() > star.pop():
                return False
        return True
