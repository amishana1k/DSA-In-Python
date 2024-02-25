class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_to(self, data):  #insert at begininig
        node = Node(data, self.head,None)
        if self.head is None:
            self.head = node
        self.head.prev = node
        self.head = node

    def print_forward(self):
        if self.head is None:
            print("list is empty")
        s = ""
        itr = self.head
        while itr:
            s += str(itr.data) + '--->'
            itr = itr.next
        print(s)

    def print_backward(self):
        if self.head is None:
            print("list is empty")
        itr = self.head
        while itr.next:
            itr = itr.next

        s = ""
        while itr:
            s += str(itr.data) + '<-->'
            itr = itr.prev

        print(s)


if __name__=='__main__':
    dl = DoublyLinkedList()
    dl.insert_to(10)
    dl.insert_to(20)
    dl.insert_to(30)
    dl.print_forward()
    dl.print_backward()