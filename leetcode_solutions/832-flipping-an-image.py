iclass Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        
        
        if not A:
            return None
        else:
            
            for i in A:
                i.reverse()
            
            for i in range(len(A)):
                temp = A[i]
                temp = [abs(x - 1) for x in temp]
                A[i]= temp
            
            return A
        
        
