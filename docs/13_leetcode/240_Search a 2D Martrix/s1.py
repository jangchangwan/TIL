class Solution:
    def searchMatrix(self, matrix, target):
        answer = False
        x = len(matrix)
        y = len(matrix[0])
        for i in range(x):
            for j in range(y):
                if matrix[i][j] == target:
                    answer = True

        return answer