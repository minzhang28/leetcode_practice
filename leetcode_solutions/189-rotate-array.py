class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if not nums or not k:
            return None
        else:
            for i in range(k):
                val = nums.pop()
                nums.insert(0, val)
