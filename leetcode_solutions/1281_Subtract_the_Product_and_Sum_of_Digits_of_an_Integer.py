class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        
        if not n:
            return None
        
        num = str(n)
        
        p = 1
        s = 0
        
        
        
        for i in num:
            s += int(i)
            p = p * int(i)
            
        
        result = p - s 
        return  result
