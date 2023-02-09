class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:

    def __init__(self):
        self.head = None

    def display(self):
        if self.head == None:
            print("The linked list is empty.")
        else:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next

    def append(self, new_data):
        new_node = Node(new_data)
        
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, location, new_data):
        ptr = self.head
        new_node = Node(new_data)
        try:
            for i in range(location-2):
                print("head value: ", ptr.data, "next value: ", ptr.next)
                ptr = ptr.next
            new_node.next = ptr.next
            ptr.next = new_node
        except:
            print("Given location is out of bound")

    def remove(self, key):
        if self.head.data == key:
            self.head = self.head.next
            return
        ptr = self.head
        while ptr is not None:
            if ptr.next.data == key:
                ptr.next = ptr.next.next
                return
        print("Given node does not exist")
