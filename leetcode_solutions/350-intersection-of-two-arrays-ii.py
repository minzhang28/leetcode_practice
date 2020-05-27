class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        if not nums1 or not nums2 :
            return None
        else:
            def get_result(nums1: List[int], nums2: List[int]) -> List[int]:
                result = []
                for i in nums1:
                    if i in nums2:
                        result.append(i)
                        nums2.remove(i)
                return result
            
            if len(nums1) <= len(nums2):
                return get_result(nums1, nums2)
            else:
                return get_result(nums2, nums1)
                
