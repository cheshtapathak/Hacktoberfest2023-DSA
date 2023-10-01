# Python3 implementation to modify the contents
# of the linked list

# Linked list node
class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to insert a node at the beginning
# of the linked list
def push(head_ref, new_data):

	# allocate node
	new_node =Node(0)
	
	# put in the data
	new_node.data = new_data
		
	# link the old list at the end
	#of the new node
	new_node.next = head_ref
		
	# move the head to point to the new node
	head_ref = new_node
	
	return head_ref

front = None
back = None

# Split the nodes of the given list
# into front and back halves,
# and return the two lists
# using the reference parameters.
# Uses the fast/slow pointer strategy.
def frontAndBackSplit( head):

	global front
	global back
	slow = None
	fast = None
	
	slow = head
	fast = head.next
	
	# Advance 'fast' two nodes, and
	# advance 'slow' one node
	while (fast != None):
	
		fast = fast.next
		if (fast != None):
			slow = slow.next
			fast = fast.next

	# 'slow' is before the midpoint in the list,
	# so split it in two at that point.
	front = head
	back = slow.next
	slow.next = None
	return head

# Function to reverse the linked list
def reverseList( head_ref):

	current = None
	prev = None
	next = None
	current = head_ref
	prev = None
	while (current != None):
	
		next = current.next
		current.next = prev
		prev = current
		current = next
	
	head_ref = prev
	return head_ref

# perform the required subtraction operation
# on the 1st half of the linked list
def modifyTheContentsOf1stHalf():

	global front
	global back
	front1 = front
	back1 = back
	
	# traversing both the lists simultaneously
	while (back1 != None):
	
		# subtraction operation and node data
		# modification
		front1.data = front1.data - back1.data
		
		front1 = front1.next
		back1 = back1.next
	
# function to concatenate the 2nd(back) list
# at the end of the 1st(front) list and
# returns the head of the new list
def concatFrontAndBackList( front, back):
	
	head = front
	
	if(front == None):
		return back
	
	while (front.next != None):
		front = front.next
		
	front.next = back
	return head

# function to modify the contents of the linked list
def modifyTheList( head):

	global front
	global back

	# if list is empty or contains only single node
	if (head == None or head.next == None):
		return head
	front = None
	back = None
	
	# split the list into two halves
	# front and back lists
	frontAndBackSplit(head)
		
	# reverse the 2nd(back) list
	back = reverseList(back)
	
	# modify the contents of 1st half
	modifyTheContentsOf1stHalf()
	
	# agains reverse the 2nd(back) list
	back = reverseList(back)
	
	# concatenating the 2nd list back to the
	# end of the 1st list
	head = concatFrontAndBackList(front, back)

	# pointer to the modified list
	return head

# function to print the linked list
def printList( head):

	if (head == None):
		return
	
	while (head.next != None):
	
		print(head.data , " -> ",end="")
		head = head.next
	
	print(head.data )

# Driver Code

head = None
	
# creating the linked list
head = push(head, 10)
head = push(head, 7)
head = push(head, 12)
head = push(head, 8)
head = push(head, 9)
head = push(head, 2)
	
# modify the linked list
head = modifyTheList(head)
	
# print the modified linked list
print( "Modified List:" )
printList(head)

# This code is contributed by Arnab Kundu
