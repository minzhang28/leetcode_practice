class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        if not S or not words:
            return None
        else:                        
            def isSubString(s1 :str, s2 :str) -> bool:                
                p1, p2 = 0,0
                while p1 < len(s1) and p2 < len(s2):
                    if s1[p1] == s2[p2]:
                        p1 += 1
                        p2 += 1
                    else:
                        p2 += 1                        
                return p1 == len(s1)            
            result = 0
        
            d = {}
            for i in words:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1

            for i in d.keys():
                if isSubString(i, S):
                    result += d[i]            
            return result
                    
