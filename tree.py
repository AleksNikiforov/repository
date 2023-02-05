class Node:

    def __init__(self, value):
        self.value = value
        self.children = []
    
    def append_child(self, node):
        self.children.append(node)



root = Node(0)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
root.append_child = node1
root.append_child = node2
root.append_child = node3

node4 = Node(4)
node5 = Node(5)
node1.append_child = node4
node1.append_child = node5