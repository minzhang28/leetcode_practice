class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return None
        else:
            while n >= 3:
                n = n/3
            else:
                if n == 1:
                    return True
                else:
                    return False
