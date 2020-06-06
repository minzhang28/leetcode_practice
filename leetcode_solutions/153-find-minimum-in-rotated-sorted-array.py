class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        if not nums:
            return None
        else:
            
            left = 0 
            right = len(nums) - 1
            
            while left < right:
                mid = left + (right - left ) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[right] > nums[mid]:
                    right = mid
            
            return nums[left]
                
