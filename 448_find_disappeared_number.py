class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        
        size = len(nums)
        
        d = set(range(1,size+1))
        for i in nums:
            if i in d:
                d.discard(i)
        return list(d)
    
