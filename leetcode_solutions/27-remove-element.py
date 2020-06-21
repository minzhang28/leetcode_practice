class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0             
        for i in range(len(nums)):                
            if nums[i] != val:
                # print("nums is {}, idx is{}, i is {}".format(nums, idx, i))
                nums[idx] = nums[i]
                idx += 1
        return idx
