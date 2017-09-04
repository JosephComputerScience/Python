"""
Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest
common ancestor is defined between two nodes v and w as the
lowest node in T that has both v and w as descendants
(where we allow a node to be a descendant of itself).”
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def contain(self, parent, node):
        queue = [parent]
        while len(queue) != 0:
            current = queue.pop(0)
            if current == node:
                return True
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return False

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        result = root
        queue = [root]
        if self.contain(p, q):
            return p.val
        if self.contain(q, p):
            return q.val
        while (len(queue) != 0):
            curr_node = queue.pop()
            if self.contain(curr_node, p) and self.contain(curr_node, q):
                result = curr_node
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
        return result.val
