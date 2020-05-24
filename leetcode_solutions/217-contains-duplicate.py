class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        
        if not nums:
            return None
        else:            
            nums_set = set(nums)            
            return len(nums_set) != len(nums)
