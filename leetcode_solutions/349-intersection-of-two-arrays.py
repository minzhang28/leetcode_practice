class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return None
        else:
            result = []
            def findTarget(nums: List[int], target: int) -> bool:
                left = 0 
                right = len(nums) - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    print("target to find is {}, mid number is {}".format(target, nums[mid]))
                    if target == nums[mid]:
                        return True
                    elif target > nums[mid]:
                        left = mid + 1
                    elif target < nums[mid]:
                        right = mid - 1
                
                return False
        
            nums1.sort()
            nums2.sort()
            for i in nums2:
                print("i is {}".format(i))
                if findTarget(nums1, i) and i not in result:
                    result.append(i)
            
            return result 
