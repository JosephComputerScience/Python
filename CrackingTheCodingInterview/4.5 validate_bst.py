"""
Implement a function to check if a binary tree is a binary search tree.
"""


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_children(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child


def create_tree_node_list(values):
    tree_node_lst = []
    for value in values:
        tree_node_lst.append(TreeNode(value))

    return tree_node_lst


def check_bst(root):
    return check_bst_helper(root)


def check_bst_helper(focus_node, min=None, max=None):
    if focus_node is None:
        return True

    if focus_node.data < min and min is not None or \
       focus_node.data > max and max is not None:
        return False

    return check_bst_helper(focus_node.left_child, min, focus_node.data) and \
        check_bst_helper(focus_node.right_child, focus_node.data, max)
