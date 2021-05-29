class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        index_dict = {0:-1}
        state = 0
        vowels = 'aeiou'
        max_length = 0
        
        for index, char in enumerate(s):
            vowel_pos = vowels.find(char)
            if vowel_pos >= 0:
                state ^= 1 << vowel_pos
            
            if state in index_dict.keys():
                max_length = max(max_length, index - index_dict[state])
            else:
                index_dict[state] = index
        
        return max_length
