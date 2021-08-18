class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None

    
class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next is self.head:
                break
            node = node.next

    def traverse(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            if node.next is self.head:
                break
            node = node.next
        print()

    def CreateDCLL(self, nodeValue):
        if self.head:
            return
        node = Node(nodeValue)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node

    def Add(self, nodeValue):
        if not self.head:
            self.CreateDCLL(nodeValue)
            return
        node = Node(nodeValue)
        node.next = self.head
        node.prev = self.tail
        self.tail.next = node
        self.head.prev = node
        self.tail = node

    def insert(self, nodeValue, location):
        if not self.head:
            if location not in (0, - 1): return
            self.CreateDCLL(nodeValue)
            return
        newNode = Node(nodeValue)
        if location == 0:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
        elif location == -1:
            self.Add(nodeValue)
        else:
            tempNode = self.head
            i = 0
            while i < location - 1:
                if tempNode.next == self.head:
                    return
                tempNode = tempNode.next
                i += 1
            
            if tempNode.next == self.head:
                self.Add(nodeValue)
                return

            nextNode = tempNode.next
            newNode.next = nextNode
            newNode.prev = tempNode
            nextNode.prev = newNode
            tempNode.next = newNode


        

doublyCircularLinkedList = DoublyLinkedList()
doublyCircularLinkedList.CreateDCLL(1)
# print([node.value for node in doublyCircularLinkedList])
# doublyCircularLinkedList.traverse()

[doublyCircularLinkedList.Add(i) for i in range(2, 6, 2)]
doublyCircularLinkedList.insert(0, 0)
[doublyCircularLinkedList.insert(i, i) for i in range(3, 6, 2)]
doublyCircularLinkedList.insert(6,6)
doublyCircularLinkedList.traverse()