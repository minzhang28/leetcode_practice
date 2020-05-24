class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return None
        else:
            d = {
                "I" : 1,
                "V" : 5,
                "X" :10,
                "L" : 50,
                "C" :100,
                "D" :500,
                "M" :1000
            }
            
            temp = []
            temp.append(d[s[0]])
            
            result = 0
            for i in range(1,len(s)):
                val = d[s[i]]
                if val <= temp[-1]:
                    temp.append(val)
                else:
                    t = temp.pop()
                    temp.append(0-t)
                    temp.append(val)

            return sum(temp)
