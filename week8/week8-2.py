class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=' ')

def insert(root, value):
    newNode = TreeNode()
    newNode.data = value

    if root is None:
        return newNode

    current = root
    while True:
        if number < current.data:
            if current.left is None:
                current.left = newNode
                break
            current = current.left
        else:
            if current.right is None:
                current.right = newNode
                break
            current = current.right
    return root

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 1, 7, 20]
    root = None

    for number in numbers:
        root = insert(root, number)

    post_order(root)

    find_number = int(input())
    current = root
    while True:
        if find_number == current.data:
            print(f"{find_number}을(를) 찾았습니다")
            break
        elif find_number < current.data:
            if current.left is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.right
