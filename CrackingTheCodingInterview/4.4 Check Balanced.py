"""
Implement a function to check if a binary tree is balanced. 
For the purposes of this question, a balanced tree is defined 
to be a tree such that the heights of the two subtrees of any 
node never differ by more than one.
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_children(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child


def check_height(node):
    if node is None:
        return 0

    left_height = check_height(node.left_child)
    if left_height is False:
        return False

    right_height = check_height(node.right_child)
    if right_height is False:
        return False

    if abs(left_height - right_height) > 1:
        return False

    return max(left_height, right_height) + 1


def is_balanced(root):
    return check_height(root) > 0


def create_tree_node_list(values):
    tree_node_lst = []
    for value in values:
        tree_node_lst.append(TreeNode(value))

    return tree_node_lst
