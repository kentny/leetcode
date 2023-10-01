# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m - 1
        target_row = None

        while left <= right:
            mid = int((right + left) / 2)
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][0] < target:
                left = mid + 1
                target_row = mid
            else:
                return True

        if target_row is None:
            return False

        left = 0
        right = n - 1

        while left <= right:
            mid = int((right + left) / 2)
            if matrix[target_row][mid] > target:
                right = mid - 1
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                return True

        return False
