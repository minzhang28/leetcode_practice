class Solution:
    def twoSum(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1

class Solution:
    def twoSum(self, numbers, target):
        
        
        if not numbers and not target:
            return None
        else:
            
            l = 0
            r = len(numbers) - 1
            
            while l < r:
                if numbers[l] + numbers[r] > target:
                    r -= 1
                elif numbers[l] + numbers[r] == target:
                    return [l+1, r+1]
                elif numbers[l] + numbers[r] < target:
                    l += 1
                                    
