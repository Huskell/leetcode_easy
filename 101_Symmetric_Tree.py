# Definition for a binary tree node.
from idlelib.tree import TreeNode


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def check(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True

            if (not right and left) or (not left and right):
                return False

            if left.val != right.val:
                return False

            return check(left.right, right.left) and check(left.left, right.right)

        if root is None:
            return True
        else:
            return check(root.left, root.right)




if __name__ == '__main__':
    # root = [[1,2,2,3,4,4,3]]

    root2_1 = TreeNode(2)
    root2_1.left = TreeNode(3)
    root2_1.right = TreeNode(4)

    root2_2 = TreeNode(2)
    root2_2.left = TreeNode(4)
    root2_2.right = TreeNode(3)

    root = TreeNode(1)
    root.left = root2_1
    root.right = root2_2

    sol = Solution().isSymmetric(root)
    print(sol)