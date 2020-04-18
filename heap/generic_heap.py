class Heap:
    # Per the unittest, the "comparator" function returns True when
    # the first argument has priority, and False when it doesn't.
    # So the equivalent of this for a max heap is "lambda x, y: x > y".
    # Thus, I have that as my default comparator.
    def __init__(self, comparator=lambda x,y: x>y):
        self.storage = []
        self.comparator = comparator

    def insert(self, value):
        # Same as my code in max_heap.py
        self.storage.append(value)
        size = self.get_size()
        index = self._bubble_up(size-1)
        while index != -1:
            if type(index) is not int:
                break
            index = self._bubble_up(index)

    def delete(self):
        # Same as my code in max_heap.py
        value = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        index = self._sift_down(0)
        while index != -1:
            if type(index) is not int:
                break
            index = self._sift_down(index)
        return value

    def get_priority(self):
        # Whichever value is selected by the priority function
        # will always be the upmost one. So just copy my code
        # from max_heap.py
        if self.storage:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        # Same as max_heap.py
        return len(self.storage)

    def _bubble_up(self, index):
        # Largely the same as in max_heap.py; but instead of seeing
        # if the parent is bigger than the child, we have to apply
        # the priority function.
        layer_id = self._find_layer_id(index)
        if layer_id == 0:
            return -1
        else:
            values_in_current_layer = 2**(layer_id)
            position_in_layer = index - values_in_current_layer + 1
            values_in_previous_layer = 2**(layer_id-1)
            parent_index = values_in_previous_layer - 1 + (position_in_layer // 2)
            # This is the new code
            child_value = self.storage[index]
            parent_value = self.storage[parent_index]
            # Again, the way the comparator works appears to be that it returns
            # True when the first argument has priority, and False when it doesn't.
            # So I put the child value into the comparator first, and if the result
            # is True, that means the child has priority and we have to swap them.
            if self.comparator(child_value, parent_value):
                self.storage[index] = parent_value
                self.storage[parent_index] = child_value
                return parent_index
            else:
                # Otherwise, don't swap and return -1
                return -1

    def _sift_down(self, index):
        # Again, everything is the same as max_heap.py until we start
        # comparing the values.
        layer_id = self._find_layer_id(index)
        values_in_current_layer = 2**(layer_id)
        position_in_layer = index - values_in_current_layer + 1
        child_1_index = index + values_in_current_layer + position_in_layer
        size = self.get_size()
        if child_1_index > size-1:
            return -1
        elif child_1_index == size-1:
            priority_child_index = child_1_index
        else:
            child_2_index = child_1_index + 1
            child_1_value = self.storage[child_1_index]
            child_2_value = self.storage[child_2_index]
            # If the result of the comparator function is True, that means
            # the first argument--in this case, the first child value--
            # has priority.
            if self.comparator(child_1_value, child_2_value):
                priority_child_index = child_1_index
            else:
                priority_child_index = child_2_index
        parent_value = self.storage[index]
        child_value = self.storage[priority_child_index]
        # If the child_value has priority, swap them.
        if self.comparator(child_value, parent_value):
            self.storage[index] = child_value
            self.storage[priority_child_index] = parent_value
            return priority_child_index
        else:
            return -1

    def _find_layer_id(self, index):
        # Same as max_heap.py
        layer_id = 0
        while index not in range(2**(layer_id)-1, 2**(layer_id+1)-1):
            layer_id += 1
        return layer_id
