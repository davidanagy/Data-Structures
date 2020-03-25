class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        if self.get_size() == 0:
            self.storage.append(value)
        else:
            self.storage.append(value)
            size = self.get_size()
            index = size-1
            while self._bubble_up(index):
                index = self._bubble_up(index)

    def delete(self):
        value = self.storage[0]
        self.storage[0] = self.storage[-1]
        self.storage.pop()
        index = 0
        while self._sift_down(index):
            index = self._sift_down(index)
        return value

    def get_max(self):
        if self.storage:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        layer_id = self._find_layer_id(index)
        if layer_id == 0:
            return False
        else:
            current_mult = 2**(layer_id)
            diff = index - current_mult
            position = round(diff/2)
            previous_mult = 2**(layer_id-1)
            parent_index = previous_mult - 1 + position
            if self.storage[index] > self.storage[parent_index]:
                self.storage[index], self.storage[parent_index] = self.storage[parent_index], self.storage[index]
                return parent_index
            else:
                return False

    def _sift_down(self, index):
        layer_id = self._find_layer_id(index)
        current_mult = 2**(layer_id)
        diff = index - current_mult
        child_1_index = index + current_mult + diff + 1
        size = self.get_size()
        if child_1_index > size-1:
            return False
        elif child_1_index == size-1:
            max_child_index = child_1_index
        else:
            child_2_index = child_1_index + 1
            max_child_index = max((child_1_index, child_2_index))
        if self.storage[max_child_index] > self.storage[index]:
            self.storage[max_child_index], self.storage[index] = self.storage[index], self.storage[max_child_index]
            return max_child_index
        else:
            return False
        
    def _find_layer_id(self, index):
        if index == 0:
            return 0
        else:
            layer_id = 1
            while index in range(2**(layer_id)-1, 2**(layer_id+1)-1):
                layer_id += 1
            return layer_id
