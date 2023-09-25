from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        sorted_nums = sorted(nums)

        # [-1,  0, 1, 2, -1, -4]
        # [-4, -1,-1, 0,  1,  2]
        for i in range(len(sorted_nums) - 2):
            if i > 0 and sorted_nums[i-1] == sorted_nums[i]:
                continue
            left = i + 1 # 2
            right = len(sorted_nums) - 1 # 5
            search_sum = -sorted_nums[i] # 1
            while left < right:
                if i + 1 < left and sorted_nums[left - 1] == sorted_nums[left]:
                    left += 1
                    continue
                if right < len(sorted_nums) - 2 and sorted_nums[right] == sorted_nums[right + 1]:
                    right -= 1
                    continue

                if search_sum < 2 * sorted_nums[left] or search_sum > 2 * sorted_nums[right]:
                    break

                sum_value = sorted_nums[left] + sorted_nums[right] # 1
                if sum_value == search_sum:
                    result.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                elif sum_value < search_sum:
                    left += 1
                elif sum_value > search_sum:
                    right -= 1

        return result

