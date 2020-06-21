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


### Jun 21st
class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        else:
            stack = []
            result = [0]*len(nums)
            stack.append(0)

            for i in range(1, len(nums)):
                while stack and nums[i] > nums[stack[-1]]:
                    idx = stack.pop()
                    result[idx] = i - idx
                else:
                    stack.append(i)
            return result
