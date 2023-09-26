import unittest
from three_sum import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        result = solution.threeSum([-1,0,1,2,-1,-4])
        self.assertListEqual([[-1,-1,2],[-1,0,1]], result)


if __name__ == '__main__':
    unittest.main()
