import random

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link
        current.link = Node(data)

    def search(self, target):
        current = self.head
        while current.link:
            if target == current.data:
                return f"{target}을 찾았습니다."
            else:
                current = current.link
        return f"{target}은 링크드 리스트 안에 존재하지 않습니다."

    def remove(self, target):
        current = self.head
        if current.data == target:
            self.head = self.head.link
            return
        previous = None
        while current:
            if current.data == target:
                previous.link = current.link
                current.link = None
            previous = current
            current = current.link

    def __str__(self):
        # current = self.head
        # while current is not None:
        #     print(current.data)
        #     current = current.link
        # return "end"

        current = self.head
        outText = ""
        while current is not None:
            # outText = outText + str(current.data) + "->"
            outText = outText + f"{current.data} -> "
            current = current.link
        return outText + "end"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
print(ll.search(10))
print(ll.search(1))
ll.remove(8)
ll.remove(-9)
print(ll)

for _ in range(0, 20):
    ll.append(random.randint(1, 30))
print(ll)
print(ll.search(20))