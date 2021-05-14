class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        letter_start_position = {}
        letter_end_position = {}
        output = []
        
        for index, char in enumerate(s):
            letter_start_position[char] = min(letter_start_position.get(char,len(s)),index)
            letter_end_position[char] = max(letter_end_position.get(char,0),index)
            
        for char in letter_start_position.keys():
            start_index = letter_start_position[char]
            end_index = letter_end_position[char]
            cur_string = s[start_index:end_index+1]
            if len(cur_string) > 1:
                i = 0
                while i < len(cur_string):
                    cur_char = cur_string[i]       
                    cur_start_index = letter_start_position[cur_char]
                    cur_end_index = letter_end_position[cur_char]
                    if cur_start_index < start_index:
                        cur_string = ""                    
                    else:
                        end_index = max(cur_end_index,end_index)
                        cur_string = s[start_index:end_index+1]
                    i += 1
                    
            if len(cur_string) > 0:
                output.append(cur_string)
                for item in output:
                    if cur_string in item and cur_string != item:
                        output.remove(item)
                    if item in cur_string and cur_string != item:
                        output.remove(cur_string)                     
        
        return output
