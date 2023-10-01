import unittest
from search_a_2D_matrix import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        result = solution.searchMatrix(matrix, 3)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
