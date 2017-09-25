"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify
the input 2D matrix directly. DO NOT allocate another 2D matrix and do
the rotation.
"""


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix)-1
        while l < r:
            for i in range(l, r):
                temp1 = matrix[i][r]
                matrix[i][r] = matrix[l][i]
                temp2 = matrix[r][r-i+l]
                matrix[r][r-i+l] = temp1
                temp1 = matrix[r-i+l][l]
                matrix[r-i+l][l] = temp2
                matrix[l][i] = temp1
            l += 1
            r -= 1
