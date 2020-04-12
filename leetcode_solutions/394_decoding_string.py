class Solution:
    def decodeString(self, s: str) -> str:
        stack, multi, res = [], 0, ''
        for c in s:
            if c == '[':
                
                stack.append((res, multi))
                res, multi = '', 0
            elif c == ']':
                
                last_res, multi = stack.pop()
                res = last_res + multi * res
                multi = 0
            elif c.isdigit():
                
                multi = multi * 10 + int(c)
            else:
                
                res += c
        return res

