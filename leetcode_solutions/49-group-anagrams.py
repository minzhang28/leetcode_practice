class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        if not strs:
            return None
        else:
            d = {}
            for s in strs:
                sorted_s = "".join(sorted(s))
                if sorted_s in d:
                    d[sorted_s].append(s)
                else:
                    d[sorted_s] = [s]
            
            result = []
            for key in d.keys():
                result.append(d[key])
                
            return result
