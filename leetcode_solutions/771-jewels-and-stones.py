class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return None
        else:
            result = 0
            for i in S:
                if i in J:
                    result += 1
                    
            return result
