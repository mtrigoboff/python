class Node:

	def __init__(self, data):
		self._data = data
		self._left = None
		self._right = None

	def __str__(self):
		return self._data

class BinarySearchTree:

	def __init__(self):
		self._tree = None

	def add_node(self, data):
		if self._tree is None:			# adding to empty tree
			self._tree = Node(data)
		else:
			self.add_node_r(self._tree, data)

	def add_node_r(self, parent, data):
		if data < parent._data:
			if parent._left is None:
				parent._left = Node(data)
			else:
				self.add_node_r(parent._left, data)
		else:
			if parent._right is None:
				parent._right = Node(data)
			else:
				self.add_node_r(parent._right, data)

	def print_tree(node):
		global tree_str
		if node._left is not None:
			BinarySearchTree.print_tree(node._left)
		tree_str += node._data
		if node._right is not None:
			BinarySearchTree.print_tree(node._right)
		return tree_str

	def __str__(self):
		global tree_str
		tree_str = ''
		return BinarySearchTree.print_tree(self._tree)

tree = BinarySearchTree()
tree.add_node('M')
tree.add_node('G')
tree.add_node('B')
tree.add_node('K')
tree.add_node('T')
tree.add_node('R')
tree.add_node('W')

print(tree)
