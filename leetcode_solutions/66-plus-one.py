class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        if not digits:
            return None
        else:
            
            result = ""
            for i in digits:
                result += str(i)
            
            result2 = int(result) + 1
            
            return_val = []
            for j in str(result2):
                return_val.append(j)
                
            return return_val
