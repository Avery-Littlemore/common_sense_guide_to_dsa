# Write an algorithm that finds the greatest value within a binary search tree.

def greatest_value(node):
    if node.right_child:
        greatest_value(node.right_child)
    else:
        return node.value