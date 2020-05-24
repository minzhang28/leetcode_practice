class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        if not prices or len(prices) == 0:
            return None    
        else:
            stack = []
            result = 0
            stack.append(prices[0])
            for i in range(1,len(prices)):
                val = prices[i]
                print("i is {}, max val in stack is {}".format(prices[i], stack))
                if val > stack[-1]:
                    stack.append(val)
                else:
                    result += (stack[-1] - stack[0])
                    stack = []
                    stack.append(val)
            return result + stack[-1] - stack[0]
