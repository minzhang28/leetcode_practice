class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        # output = [-1]*len(nums)
    
        circled_list=nums+nums
        output = [-1]*len(circled_list)

        for i in range(len(circled_list)):
            while stack and circled_list[i] > circled_list[stack[-1]]:
                out_number_index = stack.pop()
                print("out_number_index is {}".format(out_number_index))
                output[out_number_index] = circled_list[i]
            stack.append(i)

        print("output is {}".format(output[:len(nums)]))
        return output[:len(nums)]
