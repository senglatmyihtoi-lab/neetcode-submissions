class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l,r=0,len(i)-1
            while l<=r:
                if i[l] == target or i[r] == target:
                    return True
                elif i[l]<target:
                    l+=1
                elif i[r]>target:
                    r-=1
        return False 
            
        