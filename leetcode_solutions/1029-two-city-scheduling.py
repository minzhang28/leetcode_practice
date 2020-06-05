class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return None
        else:
            cost_a = 0 
            cost_diff = []
            for c in costs:
                cost_a += c[0]
                cost_diff.append(c[1] - c[0])
                
            cost_diff.sort()
            
            for i in range(len(costs) // 2):
                cost_a += cost_diff[i]
                
            return cost_a
