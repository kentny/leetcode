# https://leetcode.com/problems/decode-ways/description/
from collections import defaultdict

class Solution:
    def __init__(self):
        self.hash_map = defaultdict(int)

    def numDecodings(self, s: str) -> int:
        def numDecodingsWithIndex(index: int) -> int:
            if index in self.hash_map:
                return self.hash_map[index]

            if index > len(s) - 1:
                return 1

            if s[index] == "0":
                return 0

            if index == len(s) - 1:
                return 1

            if int(s[index:index+2]) > 26:
                num = numDecodingsWithIndex(index + 1)
                self.hash_map[index] = num
                return num

            num = numDecodingsWithIndex(index + 1) + numDecodingsWithIndex(index + 2)
            self.hash_map[index] = num
            return num

        return numDecodingsWithIndex(0)

# 512
# 5 f(12)
# 5 1 f(2)
# 5 1 2, 5 12,

# 1201
# 1 201
# 12 01
# 1 201

# 2323
# 2 3 2 3
# 2 3 23
# 23 23
# 23 2 3
