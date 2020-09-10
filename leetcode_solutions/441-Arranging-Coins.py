class Solution:
    def arrangeCoins(self, n: int) -> int:
        if not n or n < 0:
            return 0
        else:
            result = []
            left = n 
            idx = 1
            while left >= idx:
                result.append(idx)
                left = left - idx 
                idx += 1
            else:
                return len(result) 
