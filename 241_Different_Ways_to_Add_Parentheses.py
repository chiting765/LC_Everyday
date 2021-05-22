class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calculate(left, op, right):
            if op == "+":
                result = int(left) + int(right)
            elif op == "-":
                result = int(left) - int(right)
            else:
                result = int(left) * int(right)
                
            #print(left,op,right,result)
            return result
    
        def dfs(numbers, ops):
            result = []
            if len(numbers) == 1:
                return numbers
            for i, op in enumerate(ops):
                if i == 0:
                    left = [numbers[0]]
                else:
                    left = dfs(numbers[:i+1], ops[:i])

                if i == len(ops) - 1:
                    right = [numbers[-1]]
                else:
                    right = dfs(numbers[i+1:], ops[i+1:])

                #print(numbers, ops, left,right)
                for l in left:
                    for r in right:
                        result.append(calculate(l,op,r))

            return result
    
        numbers = []
        operations = []
        cur_number = ""
        for char in expression:
            if char.isdigit():
                cur_number += char
            else:
                operations.append(char)
                numbers.append(cur_number)
                cur_number = ""
        
        numbers.append(cur_number)
        #print(numbers,operations)
        return dfs(numbers, operations)
