class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')


ll = LinkedList()
n = int(input("Enter number of elements: "))
for _ in range(n):
    value = int(input("Enter value to insert: "))
    ll.insert(value)

print("Linked List after insertion:")
ll.display()

delete_value = int(input("Enter value to delete: "))
ll.delete(delete_value)
print("Linked List after deletion:")
ll.display()
