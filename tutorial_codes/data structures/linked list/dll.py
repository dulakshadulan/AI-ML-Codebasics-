class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        
        node = Node(data,self.head,None)
        self.head.prev = node
        self.head = node

    def insert_at_the_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None,itr)



    def Print(self):
        if self.head == None:
            print("List is empty")
            return
        itr = self.head
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + '<-->'
            itr = itr.next
        print(dllstr)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def print_forward(self):
        if self.head is None:
            print("List is empty")
            return
        itr = self.head
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + '<-->'
            itr = itr.next
        print(dllstr)

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return
        last_node = self.get_last_node()
        itr = last_node
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + '<-->'
            itr = itr.prev
        print(dllstr)

        

    def get_last_node(self):
        if self.head == None:
            print("List is empty")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_values(["banana", "mango", "grapes", "orange"])
    dll.print_forward()
    dll.print_backward()

        