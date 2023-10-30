import unittest
from DecodeWays import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        result = solution.numDecodings("27")
        self.assertEqual(1, result)



