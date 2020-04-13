class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        output = []
        if not nums or len(nums) == 0:
            return None
        else:
            length= len(nums)
            left = [None] * length
            right = [None] * length

            left[0] = 1
            right[-1] = 1


            for i in range(1, length):
                left[i] = left[i-1] * nums[i-1]
                right[length-i-1] = right[length-i] * nums[length - i]

            print("left result is {}".format(left))
            print("right result is {}".format(right))

            for i in range(length):

                output.append(left[i] * right[i])

        print("output is {}".format(output))
        return output
