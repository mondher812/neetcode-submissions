class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        k = 1

        top = 0
        bottom = len(matrix)-1
        while top <= bottom:
            m = (top + bottom) //2
            
            if target > matrix[m][-1]:
                top = m +1
            elif target< matrix[m][0]:
                bottom = m -1
            else:
                 break
        if top > bottom:
            return False
            
              

        k = m+1


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
        