class Solution:
    def longestAwesome(self, s: str) -> int:
        digits = "0123456789"
        state = 0
        state_dict = {0:-1}
        length = 1
        for index, char in enumerate(s):
            digit_index = digits.find(char)
            state ^= 1 << digit_index
            if state not in state_dict.keys():
                state_dict[state] = index
            else:
                length = max(length, index-state_dict[state]+1)
                
            state_copy = state
            
            # just vary the state by 1 digit and see whether there is a match
            for i in range(10):
                if str(i) != char:
                    state_copy ^= 1 << i
                    if state_copy in state_dict.keys():
                        length = max(length, index-state_dict[state_copy])
                    state_copy = state
 
        return min(length,len(s))
