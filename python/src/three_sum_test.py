import unittest
from three_sum import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        result = solution.threeSum([-1,0,1,2,-1,-4])
        self.assertListEqual([[-1,-1,2],[-1,0,1]], result)


if __name__ == '__main__':
    unittest.main()


# import unittest
# from typing import List, Dict, Any
#
# # ここにSolutionクラスを貼り付けてください
# # class Solution:
#
# class TestSolution(unittest.TestCase):
#
#     def test_isValidSudoku(self):
#         solution = Solution()
#         board = [
#             [".", ".", ".", ".", "5", ".", ".", "1", "."],
#             [".", "4", ".", "3", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", "3", ".", ".", "1"],
#             ["8", ".", ".", ".", ".", ".", ".", "2", "."],
#             [".", ".", "2", ".", "7", ".", ".", ".", "."],
#             [".", "1", "5", ".", ".", ".", ".", ".", "."],
#             [".", ".", ".", ".", ".", "2", ".", ".", "."],
#             [".", "2", ".", "9", ".", ".", ".", ".", "."],
#             [".", ".", "4", ".", ".", ".", ".", ".", "."]
#         ]
#
#         self.assertTrue(solution.isValidSudoku(board))
#
# if __name__ == "__main__":
#     unittest.main()
