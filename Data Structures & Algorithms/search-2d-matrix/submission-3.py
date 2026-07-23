class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new_array = []
        for index, value in enumerate(matrix):
            for j in range(len(value)):
                new_array.append(value[j])
                if target in new_array:
                    return True
        else:
                return False