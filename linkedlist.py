class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

#create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#connecting nodes to form linkedlist
node1.next = node2
node2.next = node3

#printing the linkedlist
head = node1
current = node1
while current is not None:
  print (current.data, end='->')
  current = current.next
print("None")

#adding new node at beginning
new_node = node(50)
new_node.next = head #new node points to prev head
head = new_node 
