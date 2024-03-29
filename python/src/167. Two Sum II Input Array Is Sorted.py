class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            sum_value = numbers[left] + numbers[right]
            if sum_value < target:
                left += 1
            else:
                right -= 1

        return [left + 1, right + 1]
