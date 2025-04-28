def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=" ")

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.data, end=" ")
    in_order(node.right)

def pre_order(node):
    if node is None:
        return
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)

class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = "nd1"

node2 = TreeNode()
node2.data = "nd2"
node1.left = node2

node3 = TreeNode()
node3.data = "nd3"
node1.right = node3

node4 = TreeNode()
node4.data = "nd4"
node2.left = node4

node5 = TreeNode()
node5.data = "nd5"
node2.right = node5

node6 = TreeNode()
node6.data = "nd6"
node3.left = node6

# print(node5.data)
# print(node1.left.right.data)

post_order(node1)
print()
in_order(node1)
print()
pre_order(node1)