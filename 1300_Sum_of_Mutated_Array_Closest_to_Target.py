class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse = True)
        print(arr)
        l = 0
        r = arr[0]
        right_val = r
        left_val = l

        while l <= r:
            mid = (l + r) // 2
            if self.calculate(arr,mid) > target:
                right_val = mid
                r = mid-1
            else:
                left_val = mid
                l = mid+1
        
        if abs(self.calculate(arr,left_val) - target) <= abs(self.calculate(arr,right_val) - target):
            return left_val
        else:
            return right_val
    
    def calculate(self,arr,val):
        total = 0
        for item in arr:
            if item > val:
                total += val
            else:
                total += item
        
        return total
