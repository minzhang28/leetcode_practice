class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        else:
            sorted_nums = nums.copy()
            sorted_nums.sort()
            l = len(nums)
            r = 0           
            for i in range(len(nums)):
                if sorted_nums[i] != nums[i]:
                    l = min(l, i)
                    r = max(r, i)
            if r - l >=0:
                return r - l + 1
            else:
                return 0 
