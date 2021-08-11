class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = ['a','e','i','o','u']
        max_length = 0
        cur_string = ''
        i = 0
        while i < len(word):
            if cur_string == '':
                if word[i] == 'a':
                    cur_string += word[i]
            else:
                if word[i] == cur_string[-1] or vowels.index(word[i]) == vowels.index(cur_string[-1]) + 1:
                    cur_string += word[i]
                else:
                    if cur_string[-1] == 'u':
                        max_length = max(max_length, len(cur_string))
                    
                    if word[i] == 'a':
                        cur_string = 'a'
                    else:
                        cur_string = ''
                                   
            i += 1
        
        if cur_string != '' and cur_string[-1] == 'u':
            max_length = max(max_length, len(cur_string))
            
        return max_length
