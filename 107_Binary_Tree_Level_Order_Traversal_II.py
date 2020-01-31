# Definition for a binary tree node.
from collections import deque
from typing import List



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        que = deque()
        que.append([root, 0])
        result = []

        while que:
            l = que.popleft()
            node, level = l[0], l[1]
            if node:
                if len(result) < level+1:
                    result.insert(0, []) # вставляем пустой лист в индекс "0"
                result[-(level+1)].append(node.val) # всатвляем цифру в последний уровень
                que.append((node.left, level+1))
                que.append((node.right, level+1))
        return result


if __name__ == '__main__':
    # s = [3,9,20,None,None,15,7]

    root2_1 = TreeNode(2)
    root2_1.left = TreeNode(3)
    root2_1.right = TreeNode(4)

    root2_2 = TreeNode(2)
    root2_2.left = TreeNode(4)
    root2_2.right = TreeNode(3)

    root = TreeNode(1)
    root.left = root2_1
    root.right = root2_2

    sol = Solution().levelOrderBottom(root)
    print(sol)
