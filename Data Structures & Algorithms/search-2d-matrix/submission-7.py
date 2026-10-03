class Solution:
    def searchRow(self,row : List[int], target: int):
        L, R = 0, len(row)-1
        while L<=R:
            mid = int((L+R)/2)
            if target > row[mid]:
                L=mid+1
            elif target < row[mid]:
                R=mid-1
            else:
                return True
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l, row_r = 0, len(matrix)-1
        while row_l <= row_r:
            mid = int((row_l + row_r)/2)
            if matrix[mid][0]>target:
                row_r = mid - 1
            elif matrix[mid][-1]<target:
                row_l = mid + 1
            else:
                return self.searchRow(matrix[mid],target)
        return False
        
        

                

        