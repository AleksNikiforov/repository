from binary_tree import root


def direct(node):
    print(node.value, end=' ')
    if node.left_child:
        direct(node.left_child)
    if node.right_child:
        direct(node.right_child)


direct(root)

