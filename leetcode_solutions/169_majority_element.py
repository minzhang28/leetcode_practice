class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = len(nums) / 2
        
        d = {}
        return_val = None
        for i in nums:
            if i in d:
                d[i] +=1 
            else:
                d[i] = 1
                
        print("d is {}".format(d))
            
        for k, v in d.items():
            if v >= counter:
                return_val = k
                break
                
        print("return value is {}".format(return_val))
        return return_val
            
            
