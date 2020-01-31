"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        if root == None:
            return 0
        depth = 0
        stack = [root]
        while stack:
            next_level = []
            while stack:
                node = stack.pop()
                if node.children:
                    next_level += node.children
            stack = next_level
            depth += 1
        return depth


if __name__ == '__main__':
    pass