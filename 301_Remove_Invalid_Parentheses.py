class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        s = s.lstrip(')').rstrip('(')
        def isValid(s: str):
            count_left = 0
            for i in range(len(s)):
                if s[i] == '(':
                    count_left += 1
                elif s[i] == ')':
                    count_left -= 1
                if count_left < 0: 
                    return False
            return count_left == 0
    
        candidates = {s}
        while True:
            result = list(filter(isValid, candidates))
            if result:
                return result
            else:
                # BFS, reduce 1 length each loop
                candidates = {candidate[:i]+candidate[i+1:] for candidate in candidates for i in range(len(candidate))}
