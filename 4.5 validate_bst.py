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


def check_bst(binary_tree_root):
    queue = []
    if binary_tree_root is None:
        return False

    queue.append(binary_tree_root)
    while len(queue) != 0:
        focus_node = queue.pop(0)
        if focus_node.left_child is not None:
            if focus_node.left_child.data > focus_node.data:
                return False

            queue.append(focus_node.left_child)

        if focus_node.right_child is not None:
            if focus_node.right_child.data < focus_node.data:
                return False

            queue.append(focus_node.right_child)

    return True
