class Solution:
    def trailingZeroes(self, n: int) -> int:
        
    
        zeroCnt = 0
        while n > 0:
            n = n // 5; 
            zeroCnt += n
        
        return zeroCnt
