class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        result = []
        if len(nums) != len(index):
            return None
        else:
            for i in range(len(nums)):   
                result.insert(index[i], nums[i])
        return result
