from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        set_dict = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]

                if num == ".":
                    continue

                row_set = set_dict[f'row-{i}']
                column_set = set_dict[f'column-{j}']
                cell_set = set_dict[f'cell-{int(i / 3)}-{int(j / 3)}']

                if num in row_set or num in column_set or num in cell_set:
                    return False
                row_set.add(num)
                column_set.add(num)
                cell_set.add(num)

        return True
