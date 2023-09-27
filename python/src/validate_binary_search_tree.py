# 98. Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid_node(node: TreeNode, min_val: int | None, max_val: int | None) -> bool:
            if node is None:
                return True

            if (min_val is not None and node.val <= min_val) or (max_val is not None and max_val <= node.val):
                return False

            is_left_valid = is_valid_node(node.left, min_val, node.val)
            is_right_valid = is_valid_node(node.right, node.val, max_val)
            return is_left_valid and is_right_valid

        return is_valid_node(root, None, None)
