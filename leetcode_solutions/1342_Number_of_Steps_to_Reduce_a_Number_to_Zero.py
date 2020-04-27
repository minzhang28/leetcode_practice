class Solution:
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        if not num:
            return None
        else:
            while num > 0 :
                if num % 2 == 1: 
                    num = num -1 
                    steps += 1
                else:
                    num = num / 2
                    steps += 1
        return steps     
