class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index, value in enumerate(matrix):
            for j in range(len(value)):
                if target == value[j]:
                    return True
        else:
            return False