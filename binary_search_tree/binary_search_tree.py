import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        def insert_recursion(tree, value):
            if value < tree.value:
                if tree.left:
                    insert_recursion(tree.left, value)
                else:
                    tree.left = BinarySearchTree(value)
            else:
                if tree.right:
                    insert_recursion(tree.right, value)
                else:
                    tree.right = BinarySearchTree(value)
        
        insert_recursion(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        def search_recursion(tree, target):
            if target == tree.value:
                #print('true')
                return True
            elif target < tree.value:
                if tree.left:
                    #print('search left branch')
                    return search_recursion(tree.left, target)
                else:
                    #print('false')
                    return False
            else:
                if tree.right:
                    #print('search right branch')
                    return search_recursion(tree.right, target)
                else:
                    #print('false')
                    return False

        return search_recursion(self, target)

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value
        right = self.right
        while right:
            max_value = right.value
            right = right.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        def for_each_recursion(tree, cb):
            tree.value = cb(tree.value)
            if tree.left:
                for_each_recursion(tree.left, cb)
            if tree.right:
                for_each_recursion(tree.right, cb)

        for_each_recursion(self, cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
