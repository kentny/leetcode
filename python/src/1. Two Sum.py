class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}

        for i in range(len(nums)):
            index_dict[nums[i]] = i

        for i in range(len(nums) - 1):
            search_num = target - nums[i]
            if search_num in index_dict and index_dict[search_num] != i:
                return [i, index_dict[search_num]]

        return [0, 1]
