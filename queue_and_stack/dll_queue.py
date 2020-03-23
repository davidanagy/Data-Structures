import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # ANSWER: It's a good choice because we need to quickly access the front
        # and end of the list, but we **only** need to access those.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # When we queue a value, we add it to the *end* of our list--
        # i.e., its tail.
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        # When we dequeue a value, we remove it from the **start** of
        # our list--i.e., its head.
        if self.size == 0:
            # Looking at the test file, we want to return None when we
            # attempt to de-queue from an empty queue.
            return None
        else:
            self.size -= 1
            # The remove_from_head() method gives us the removed value,
            # so we just need to return that.
            return self.storage.remove_from_head()

    def len(self):
        # Just return the size
        return self.size
