class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if not s:
            return None
        else:
            for i in range(len(s)):
                left = i 
                right = len(s) - i - 1
                
                if left < right:
                    temp = s[left]
                    s[left]=s[right]
                    s[right]=temp
                else:
                    return
        
