import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # ANSWER: Because the only position we need to access is the first one
        # (or the last one--the point is, only one position need be accessible.)
        self.storage = DoublyLinkedList()

    def push(self, value):
        # Push and pop from the head.
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        # Push and pop from the head.
        if self.size == 0:
            # Return None when attempting to pop from an empty stack
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        # Just return the size
        return self.size
