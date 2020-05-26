class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return None
        else:
            mx = len(nums)+1
            for i in range(mx):
                if i not in nums:
                    return i
                
