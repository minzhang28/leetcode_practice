class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums and not target:
            return False
        else:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left)//2    
                
                if nums[mid] == target:
                    return True
                if nums[mid] == nums[right]:
                    right -= 1
                elif nums[left] <= nums[mid]:
                    if nums[left] <= target and target <= nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if nums[mid] <= target and target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
            return False
