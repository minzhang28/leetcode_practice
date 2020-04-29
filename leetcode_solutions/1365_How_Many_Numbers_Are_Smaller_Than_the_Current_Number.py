class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        result = []
        if not nums:
            return None
        else:
            
            for i in nums:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            
            print("d is {}".format(d))

            
            for i in nums:
                temp = 0
                for j in list(d):
                    if j < i :
                        temp += d[j]
                        
                result.append(temp)

            return result
