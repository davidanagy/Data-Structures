"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        if self.head:
            self.head.insert_before(value)
            new_head = self.head.prev
            self.head = new_head
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def remove_from_head(self):
        self.delete(self.head)

    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            new_tail = self.tail.next
            self.tail = new_tail
        else:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        self.delete(self.tail)

    def move_to_front(self, node):
        if self.head is node:
            pass
        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)

    def move_to_end(self, node):
        if self.tail is node:
            pass
        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

    def delete(self, node):
        try:
            node.delete()
            self.length -= 1
            if self.head is self.tail:
                self.head = None
                self.tail = None
            elif self.head is node:
                self.head = node.next
            elif self.tail is node:
                self.tail = node.prev
        except:
            raise ValueError('Node not found')

    def get_max(self):
        if self.length == 0:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value
