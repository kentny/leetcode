# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_map = {}
        longest = 0
        length = 0
        i = 0
        while i < len(s):
            if s[i] in index_map:
                i = index_map[s[i]] + 1
                index_map.clear()
                length = 0
            else:
                length += 1
                index_map[s[i]] = i
                i += 1
            longest = max(longest, length)

        return longest
