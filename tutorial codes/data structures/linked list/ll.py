class Node:
    def __init__(self , data=None, next= None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_the_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_the_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def print(self):
        if self.head is None:
            print("List is empty")
            return
        
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def remove_at(self,index):
        if index <0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self,index,data):
        if index <0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        if index == self.get_length():
            self.insert_at_the_end(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if  count == index -1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self,data_after, data_to_insert):
        if self.head is None:
            raise Exception("List is empty")
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next
        raise Exception("Value not found in the list")

    
    def remove_by_value(self, data):
        if self.head == None:
            raise Exception("List is empty")
        
        if self.head.data == data :
            self.head = self.head.next
            return
        
        itr = self.head
        while itr:
            if itr.next.data == data: 
                itr.next = itr.next.next
                return  
            itr = itr.next
            

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_at(4, "apple")
    ll.print()
    ll.insert_after_value('mango', "kiwi")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()

