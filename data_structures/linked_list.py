class Node:
	def __init__(self, data):
		self.data = data  # The value stored in the node
		self.next = None  # Pointer to the next node (initially None)

class LinkedList:
	def __init__(self):
		self.head = None  # The list starts empty

	# Method to add a node at the end
	def append(self, data):
		new_node = Node(data)
		
		# If the list is empty, make the new node the head
		if not self.head:
			self.head = new_node
			return

		# Otherwise, traverse to the last node
		last = self.head
		while last.next:
			last = last.next
		
		# Point the last node to our new node
		last.next = new_node

	def delete_node(self, key):
		current = self.head

		# Case 1: If the head node itself holds the key to be deleted
		if current and current.data == key:
			self.head = current.next # Changed head
			current = None # Free up memory
			return

		# Case 2: Search for the key to be deleted, keep track of the previous node
		prev = None
		while current and current.data != key:
			prev = current
			current = current.next

		# Case 3: If the key was not present in the list
		if current is None:
			return

		# Unlink the node from linked list
		prev.next = current.next
		current = None

	# Method to print the list
	def display(self):
		current = self.head
		elements = []
		while current:
			elements.append(str(current.data))
			current = current.next
		print(" -> ".join(elements) + " -> None")

# Create a new Linked List
my_list = LinkedList()

# Add some data
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
my_list.append(60)

# Show the result
my_list.display()
# Output: 10 -> 20 -> 30 -> None
