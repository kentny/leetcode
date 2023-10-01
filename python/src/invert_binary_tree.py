# https://leetcode.com/problems/invert-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = []
        if root is not None:
            stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            left_node = node.left
            right_node = node.right
            node.left = right_node
            node.right = left_node

            if left_node is not None:
                stack.append(left_node)
            if right_node is not None:
                stack.append(right_node)

        return root
