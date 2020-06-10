class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr1 or not arr2:
            return None
        else:
            d = {}
            arr1.sort()
            for i in arr1:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            
            result = []
            print("array is {}".format(arr1))
            for j in arr2:
                result += [j]*d[j]
            for x in arr1:
                if x not in arr2:
                    result.append(x)
            return result
