class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        n = 0
        m = r*c-1
        while n<=m:
            i = (n+m)//2
            
            if matrix[i//c][i%c] == target:
                return True
            elif matrix[i//c][i%c] > target:
                m = i-1
            else:
                n = i+1
        return False

