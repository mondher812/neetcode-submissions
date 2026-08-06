class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = 1
        while k<len(matrix):
            if target < matrix[k][0]:
                break
            k+=1
        l , r = 0, len(matrix[k-1]) - 1

        print(matrix[k-1])
        while l<=r:
            m = (r+l)//2
            if matrix[k-1][m] > target:
                r = m-1
            elif matrix[k-1][m] < target:
                l = m+1
            else:
                return True
        return False
        