class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return None
        else:
            people.sort(key = lambda x: (-x[0], x[1]))
            print("people is {}".format(people))
            result = []
            for p in people:
                result.insert(p[1], p)
            return result
