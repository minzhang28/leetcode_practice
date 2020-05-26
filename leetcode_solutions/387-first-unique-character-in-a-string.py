class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        else:
            d = {}
            for i in s:
                if i in d:
                    d[i] =+ 1
                else:
                    d[i] = 0
            
            idx = -1
            for i in range(len(s)):
                if d[s[i]] == 0:
                    idx = i
                    break
            return idx 
