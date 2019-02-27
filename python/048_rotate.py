# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
## solution-1: The Best, using the matrix in Memory to make moves
        matrix[:] = [ [matrix[len(matrix)-1-i][j] for i in range(len(matrix))] for j in range(len(matrix))]
        
## solution-2: first rotate against x-axis, then rotate against the diagnosis
        # dim = len(matrix)
        # for i in range(dim//2):
        #     for j in range(dim):
        #         tmp = matrix[dim-1-i][j]
        #         matrix[dim-1-i][j] = matrix[i][j]
        #         matrix[i][j] = tmp
        # for i in range(dim):
        #     for j in range(i, dim):
        #         tmp = matrix[i][j]
        #         matrix[i][j] = matrix[j][i]
        #         matrix[j][i] = tmp
