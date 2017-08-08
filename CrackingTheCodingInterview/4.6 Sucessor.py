"""
Write an alogrithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree.
You may assume that each node has a link to its parent.
"""

class TreeNode:

	def __init__(self, data = None):
		self.data = data
		self.left_child = None
		self.right_child = None

	def add_children(self, left_child, right_child):
		self.left_child = left_child
		self.right_child = right_child


class BST:
	
	def __init__(self):
		self.root = None

	def  find_min(self, node):
		while node.left_child is not None:
			node = node.left_child

		return node.data

	def add_root(self, node):
		self.root = node

	def find_num(self, node):
		temp = root
		while temp is not None:
			if node.data < temp.data:
				temp = temp.left_child
			else:
				temp = temp.right_child

		return temp

	def find_successor(self, node):
		if find_num is None:
			return None

		if node.right_child is not None:
			node = node.right_child
			return self.find_min(node)

		else:
			ancestor = self.root
			successor = None
			while ancestor is not None:
				
				if node.data < ancestor.data:
					successor = ancestor
					ancestor = ancestor.left_child
				else:
					ancestor = ancestor.right_child

			if successor is None:
				return None

			return successor.data


def create_node_lst(values):
	node_lst = []
	for value in values:
		node_lst.append(TreeNode(value))

	return node_lst

