# https://leetcode.com/problems/longest-palindromic-substring/

from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        is_palindrome = defaultdict(bool)
        is_palindrome[""] = True
        longest_palindrome_left = 0
        longest_palindrome_right = 0

        for length in range(1, len(s) + 1):
            for left in range(len(s) - length + 1):
                right = left + length - 1
                if s[left] == s[right] and (length <= 2 or is_palindrome[f"{left+1}-{right-1}"]):
                    is_palindrome[f"{left}-{right}"] = True
                    longest_palindrome_left = left
                    longest_palindrome_right = right

        return s[longest_palindrome_left:longest_palindrome_right+1]
