class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:
            return None
        else:
            
            S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            d = {}
            
            for i in range(len(S)):
                d[S[i]] = i+1                
            
            
            result = 0
            for i in range(len(s)):
                pwr = len(s) - i - 1
                result += d[s[i]]*(26**pwr)
                
            return result
