class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if not nums:
            return None
        else:
            left = 0 
            right = len(nums) - 1
            
            if target > nums[-1]:
                return len(nums)
            elif target <= nums[0]:
                return 0
            else:
                while left < right:
                    mid = left + (right - left) //2 

                    if target == nums[mid]:
                        return mid
                    if target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid]:
                        right = mid

                return right 

