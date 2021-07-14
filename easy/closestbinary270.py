from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    c = 9999

    def closestValue(self, root: TreeNode, target: float) -> int:
        c = self.c
        if root == None:
            return c
        if abs(root.val - target) < abs(c - target):
            c = root.val

        p = self.closestValue(root.left, target)
        k = self.closestValue(root.right, target)

        return c

# Definition for a binary tree node.


def createtree(root: List) -> TreeNode:
    i = 0
    if i < len(root):
        t = TreeNode(root[i])
        if i+1 >= len(root):
            t.left = root[i+1]
        if i+2 >= len(root):
            t.right = root[i+2]
        i += 2
    return t


s = Solution
s.closestValue(s, createtree([1, None, 2]), 3.428571)
