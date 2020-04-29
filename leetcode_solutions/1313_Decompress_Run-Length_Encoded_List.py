class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        if not nums:
            return None
        else:
            i = 0
            while i < len(nums):
                feq = nums[i]
                val = nums[i+1]
                temp = [val] * feq     
                result += temp
                i+=2
                
        return result
