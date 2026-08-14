class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = None
        top = 0
        bottom = len(matrix) -1
        while top<=bottom:
            m = (top+bottom)//2
            if matrix[m][0] <= target and matrix[m][-1]>= target:
                k = m
                break
            if matrix[m][0] > target:
                bottom = m-1
            else:
                top = m+1
        if k is None:
            return False
        l = 0
        r = len(matrix[k])-1
        while l <= r:
            m = (l+r)//2
            if matrix[k][m] == target:
                return True
            elif matrix[k][m] < target:
                l = m+1
            else:
                r = m-1
        return False
