class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        b = 0
        result = 0
        for i in s:
            if i == "R":
                b += 1
            else:
                b -= 1
            if b == 0:
                result += 1
                
        return result
