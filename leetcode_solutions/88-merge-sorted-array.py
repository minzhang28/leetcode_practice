class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return None
        else:
            print(m, n)
            for i in range(n):
                val = m + i 
                nums1[val] = nums2[i]
            nums1.sort()
