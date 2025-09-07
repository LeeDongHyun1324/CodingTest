class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head

        while cur.next is not None:
            cur = cur.next
        
        cur.next = Node(value)

    def print_all(self):
        cur = self.head

        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index != index:
            cur = cur.next
            cur_index +=1

        return cur.data
    
    
linked_list = LinkedList(5)
linked_list.append(12)
print(linked_list.get_node(1))
linked_list.print_all()