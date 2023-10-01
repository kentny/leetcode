# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countGoodNode(node: TreeNode, max_value: int | None, good_node_count: int) -> int:
            new_max_value = max_value
            new_good_node_count = good_node_count

            if max_value is None or node.val >= max_value:
                new_max_value = node.val
                new_good_node_count += 1

            if node.left is not None:
                new_good_node_count = countGoodNode(node.left, new_max_value, new_good_node_count)
            if node.right is not None:
                new_good_node_count = countGoodNode(node.right, new_max_value, new_good_node_count)

            return new_good_node_count

        return countGoodNode(root, None, 0)
