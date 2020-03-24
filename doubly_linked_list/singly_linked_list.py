class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_mid(self):
        current_node_one = self.head
        current_node_two = self.head
        if not self.head.next:
            return self.head
        if not self.head.next.next:
            return self.head
        while current_node_one.next:
            if current_node_one.next.next:
                current_node_one = current_node_one.next.next
                current_node_two = current_node_two.next
            else:
                return current_node_two
        return current_node_two

    def reverse(self):
        if not self.head:
            pass
        elif self.head is self.tail:
            pass
        else:
            self.tail = self.head
            current_node = self.tail
            old_next = self.tail.next
            self.tail.next = None
            while old_next.next:
                old_next_next = old_next.next
                old_next.next = current_node
                current_node = old_next
                old_next = old_next_next
            old_next.next = current_node
            self.head = old_next

    def print_values(self):
        if self.head:
            current_node = self.head
            while current_node:
                print(current_node.value)
                current_node = current_node.next