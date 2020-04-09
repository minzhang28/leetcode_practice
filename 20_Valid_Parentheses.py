class Solution:
    def isValid(self, s: str) -> bool:
        
        
        opening = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []
        
        if s:
            if s == "":
                return true
            else:
                for c in s:
                    if c in opening.keys():
                        stack.append(c)
                    else:
                        if len(stack) == 0:
                            return False
                        if opening[stack.pop()] == c:
                            pass
                        else:
                            return False
            return not stack
        else:
            return True
