class TreeNode:

	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None

	def add_children(self, left_child, right_child):
		self.left_child = left_child
		self.right_child = right_child


def sum_parent_children(node):
	if node is None:
		return 0
	sum = node.data
	sum += sum_parent_children(node.left_child)
	sum += sum_parent_children(node.right_child)

	return sum

def create_node_lst(values):
	result = []
	for value in values:
		result.append(TreeNode(value))
	return result

lst = create_node_lst([1,2,3,4,5,6,7])
lst[0].add_children(lst[1], lst[2])
lst[1].add_children(lst[3], lst[4])
lst[2].add_children(lst[5], lst[6])

print sum_parent_children(lst[0])