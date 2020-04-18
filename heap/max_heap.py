class Heap:
    def __init__(self):
        self.storage = []

    # This website was helpful to understand how to do insert and delete:
    # https://www.tutorialspoint.com/data_structures_algorithms/heap_data_structure.htm
    def insert(self, value):
        # Append value
        self.storage.append(value)
        size = self.get_size()
        # We append to the end, so the index number
        # of the new value is always size-1
        index = self._bubble_up(size-1)
        # Now I want to run self._bubble_up until swaps
        # stop happening. The way I wrote it, _bubble_up(index)
        # returns an index number if a swap happens and -1
        # if it doesn't. So I run a while loop until index equals 1.
        while index != -1:
            # The following two lines are to get the unittest to work.
            # Basically, the unittest sets _bubble_up equal to a
            # MagicMock object, and the output of that MagicMock object
            # is not an integer strictly speaking but a different Mock
            # object. So to avoid an infinite loop since index never equals
            # -1 strictly speaking, I force the loop to break if the type
            # is not an integer.
            if type(index) is not int:
                break
            # This print statement was to figure out the error with the
            # unittest discussed above.
            #print('index:', index)

            # Run the _bubble_up method on the index number. It then returns
            # an index number equal to the value's new position (or -1 if the)
            # value didn't move, so I run the method again on that new index number.
            index = self._bubble_up(index)

    def delete(self):
        # Keep the value that's getting deleted so we can return it.
        value = self.storage[0]
        # Set the first value to be the last value, then delete the last value.
        # (This effectively deletes the first value and moves the last value to
        # the first position.)
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        # Do the _sift_down method on the new first value.
        index = self._sift_down(0)
        # Similar to the _bubble_up method discussed above, the _sift_down method
        # returns the value's new index number if a swap happens, and -1 if a swap
        # doesn't happen. So set "index" equal to "_sift_down(index)", then keep
        # running the method until we end up with -1.
        while index != -1:
            if type(index) is not int:
                break
            # This print statement was to figure out the problem with the unittest,
            # discussed previously.
            #print('index:', index)

            index = self._sift_down(index)
        return value

    def get_max(self):
        if self.storage:
            # The max value is always the first one in a Max Heap.
            return self.storage[0]
        else:
            # Return None if the heap has no values
            return None

    def get_size(self):
        # Most straightforward way is to use Python's len() function.
        return len(self.storage)

    def _bubble_up(self, index):
        # This function checks the index number with its parent, then swaps
        # if the parent is smaller.
        # The basic challenge with this function was figuring out the index
        # number of the parent, given the child. I'm sure there are a number
        # of ways to do this, but my solution was to basically assign a
        # "Layer ID number" to each layer in the heap. So position 0 is layer
        # 0; its children, 1 and 2, are layer 1; the children of layer 1,
        # 2-3-4-5, are layer 2; and so son.
        # See the new _find_layer_id method below for details on how I find it.
        layer_id = self._find_layer_id(index)
        # If the value is already in the first position, it can't be moved up,
        # so return -1 (which is my signal that no swaps happened).
        if layer_id == 0:
            return -1
        else:
            # This is the pattern I noticed: each layer has a number of values
            # equal to 2^(layer_id). For example, layer 0 has 2^0 == 1 value; layer 1
            # has 2^1 == 2 values; layer 2 has 2^2 == 4 values; etc. With this knowledge,
            # we can assign each value in the layer a "position" in that layer. So for instance,
            # index 3 is the first value in layer 2, so it has a position of 0, while index 4 has
            # a position of 1, etc. Then, by applying the four operations outlined below,
            # we can find the parent index. (I could probably write a proof that this works
            # if I had to, but I promise it works; the pattern is clear.)
            values_in_current_layer = 2**(layer_id)
            position_in_layer = index - values_in_current_layer + 1
            values_in_previous_layer = 2**(layer_id-1)
            parent_index = values_in_previous_layer - 1 + (position_in_layer // 2)
            # If the child is bigger than the parent, swap the values, then return the
            # child's new index number.
            if self.storage[index] > self.storage[parent_index]:
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
                return parent_index
            # Otherwise, just return -1.
            else:
                return -1

    def _sift_down(self, index):
        # The challenge her is, given a parent index number, find the index
        # numbers of its children. Same as _bubble_up above, we start by finding
        # the layer_id and "position" of the index number. Then, we can find the index
        # number of its *first* child by adding those two to the original index number.
        # (Again, I don't have a rock-solid proof of this at the moment, but
        # the pattern is clear.)
        layer_id = self._find_layer_id(index)
        values_in_current_layer = 2**(layer_id)
        position_in_layer = index - values_in_current_layer + 1
        child_1_index = index + values_in_current_layer + position_in_layer
        # Now, we need to make sure this child actually exists! See if its greater
        # than the final index number in storage (which is just size minus 1).
        size = self.get_size()
        if child_1_index > size-1:
            # If the child doesn't exist, then obviously we can't sift down
            # anymore, so return -1.
            return -1
        elif child_1_index == size-1:
            # If the first child is the **last** value in storage, then there's
            # no second child, so the max of the first and second child
            # is just the first child.
            max_child_index = child_1_index
        else:
            # The second child's index is always 1 greater than the first's.
            child_2_index = child_1_index + 1
            # Now, compare the values of both childre. "max_child_index"
            # is the index of the bigger value.
            if self.storage[child_1_index] > self.storage[child_2_index]:
                max_child_index = child_1_index
            else:
                max_child_index = child_2_index
        # Swap the max_child_index with the parent_index if it's bigger,
        # and return the child's new index.
        if self.storage[max_child_index] > self.storage[index]:
            self.storage[max_child_index], self.storage[index] = self.storage[index], self.storage[max_child_index]
            return max_child_index
        # If the max_child_index isn't bigger, just return -1 since no swaps can happen.
        else:
            return -1
        
    def _find_layer_id(self, index):
        # As a reminder, I've assigned each layer of the heap a "layer ID"--layer here
        # meaning all the values whose parents all share a layer. So index 0 is layer 0;
        # its children 1 and 2 are layer 1; their children 3, 4, 5, and 6 are layer 2; and so on.
        # If you draw it out, you'll find that all the index numbers in a given layer L
        # are between the following values:
        # 2**L - 1 <= index_number < 2**(L+1) - 1
        # So just start at 0 and increment until we find a range that the given index
        # number is inside, and return the resultant layer_id number.
        layer_id = 0
        while index not in range(2**(layer_id)-1, 2**(layer_id+1)-1):
            layer_id += 1
        return layer_id
