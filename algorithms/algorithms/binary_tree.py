class BinaryNode:

    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None
    
    def __str__(self):
        return str(self.value)



root = BinaryNode(0)

node1 = BinaryNode(1)
node2 = BinaryNode(2)
root.left_child = node1
root.right_child = node2

node3 = BinaryNode(3)
node4 = BinaryNode(4)
node1.left_child = node3
node1.right_child = node4

node5 = BinaryNode(5)
node6 = BinaryNode(6)
node2.left_child = node5
node2.right_child = node6

