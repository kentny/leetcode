import unittest
from LongestPalindromicSubstring import Solution

class MyTestCase(unittest.TestCase):
    def test_something(self):
        solution = Solution()
        result = solution.longestPalindrome("cbbd")
        self.assertEqual("bb", result)  # add assertion here

    def test_something2(self):
        solution = Solution()
        result = solution.longestPalindrome("babad")
        self.assertEqual("bab", result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
