from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        # length begins at 0
        self.length = 0
        # need both a storage_list and a storage_dict
        self.storage_list = DoublyLinkedList()
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage_dict.keys():
            # The value of each key in storage_dict is a node
            # in the storagee_list
            node = self.storage_dict[key]
            # Move the node to the front
            self.storage_list.move_to_front(node)
            # The node itself is a key/value tuple, so return its
            # second value
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Each node in our list is a key/value tuple, so let's create it
        key_value_tuple = (key, value)
        if key in self.storage_dict.keys():
            # Get the relevant node
            node = self.storage_dict[key]
            # Override the node's current value with the new tuple
            node.value = key_value_tuple
            # Move the node to the front, since it was just used
            self.storage_list.move_to_front(node)
        else:
            # Add the new tuple as a node to the head of the list
            self.storage_list.add_to_head(key_value_tuple)
            # Get the new node, then add it to the storage_dict
            # alongside the relevant key
            new_node = self.storage_list.head
            self.storage_dict[key] = new_node
            # If we're at the limit, we want to delete the tail
            if self.length == self.limit:
                # First, get the tail's key, since we want to remove
                # that from the storage_dict as well
                removed_key = self.storage_list.tail.value[0]
                # Now delete the tail, as well as the relevant key
                self.storage_list.remove_from_tail()
                del self.storage_dict[removed_key]
            else:
                # Otherwise, just add one to the length
                self.length += 1
