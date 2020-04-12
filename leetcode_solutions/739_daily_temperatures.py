class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:

        stack=[]
        output=[0]*len(nums)
        
        for i in range(len(nums)):
            # print("i is {}, value i is {}".format(i,nums[i]))
            while stack and nums[stack[-1]] < nums[i]:
                counter=stack.pop()
                output[counter] = i - counter
            stack.append(i)
            # print("stack appends {}, stack is {}".format(i, stack))
            
        # print("output is {}".format(output))
        return output
            
