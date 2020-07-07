class Solution:
    def integerReplacement(self, n: int) -> int:
        
        if not n:
            return None
        else:            
            def getCnt(number: int, cnt: int) -> int:
                # print("number is {}, cnt is {}".format(number, cnt))
                if number > 1:
                    if number % 2 == 0:
                        return getCnt(number/2, cnt+1)
                    else:
                        return min(getCnt(number-1, cnt+1), getCnt(number+1, cnt+1))
                return cnt
            
            return getCnt(n, 0)
