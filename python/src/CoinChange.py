# https://leetcode.com/problems/coin-change/description/
from typing import List


class Solution:
    def __init__(self):
        self.memo = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in self.memo:
            return self.memo[amount]

        min_number = -1

        if amount == 0:
            return 0
        if amount < 0:
            return -1

        for coin in coins:
            number = self.coinChange(coins, amount - coin) + 1
            if number > 0 and (min_number == -1 or min_number > number):
                min_number = number

        self.memo[amount] = min_number
        return min_number
