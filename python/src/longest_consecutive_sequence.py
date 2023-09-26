class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set()
        for i in range(len(nums)):
            num_set.add(nums[i])

        longest_length = 1

        while len(num_set) > 0:
            num = num_set.pop()
            length = 1
            left = num - 1
            right = num + 1
            while left in num_set or right in num_set:
                if left in num_set:
                    num_set.remove(left)
                    length += 1
                    left -= 1
                if right in num_set:
                    num_set.remove(right)
                    length += 1
                    right += 1
                longest_length = max(longest_length, length)

        return longest_length
