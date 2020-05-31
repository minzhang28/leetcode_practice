class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        else:
            s = str(abs(x))
            r = ""
            for c in s:
                r = c+r
            
            val = 0
            if x > 0:
                val = int(r)
            else:
                val = 0 - int(r)
            
            
            return val if -(2**31)-1 < val < 2**31 else 0
