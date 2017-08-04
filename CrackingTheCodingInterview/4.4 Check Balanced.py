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


node_lst_test_one = create_tree_node_list(['A', 'B', 'C', 'D', 'E'])
node_lst_test_one[0].add_children(node_lst_test_one[1], node_lst_test_one[2])
node_lst_test_one[1].add_children(node_lst_test_one[3], None)
node_lst_test_one[2].add_children(node_lst_test_one[4], None)
""" # NOQA
        A
      /   \
     B     C
    /     /
   D     E
Answer: Balanced, True
"""
print is_balanced(node_lst_test_one[0])

node_lst_test_two = create_tree_node_list([1, 2, 'C', 'D', 'E', 'F'])
node_lst_test_two[0].add_children(node_lst_test_two[1], node_lst_test_two[2])
node_lst_test_two[1].add_children(node_lst_test_two[3], node_lst_test_two[4])
node_lst_test_two[3].add_children(node_lst_test_two[5], None)
""" # NOQA
        A
      /   \
     B     C
    / \    
   D   E  
  /
 F
Answer: Not balanced, False
"""
print is_balanced(node_lst_test_two[0])
