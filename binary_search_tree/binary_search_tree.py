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
        # Define recursion function
        def insert_recursion(tree, value):
            if value < tree.value:
                # If the given value is smaller than the tree's value,
                # then put it to the tree's left. Run the recursion function
                # again if there's already a node there; if not, create a node
                # for the given value.
                if tree.left:
                    insert_recursion(tree.left, value)
                else:
                    # This functions as a base case.
                    tree.left = BinarySearchTree(value)
            else:
                # Same as above, except put the value to the tree's right.
                if tree.right:
                    insert_recursion(tree.right, value)
                else:
                    # This functions as a base case.
                    tree.right = BinarySearchTree(value)
        
        # Run the recursion function.
        insert_recursion(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Define a recursion function.
        def search_recursion(tree, target):
            # If the tree's value is the same as the target,
            # we've found it so return True.
            if target == tree.value:
                # The commented-out print statements here were
                # for error-finding.
                #print('true')
                return True
            elif target < tree.value:
                # If the target is smaller than the tree's value,
                # that means that (if it exists) it must be on the
                # tree's left, so run the recursion function on the tree's left.
                if tree.left:
                    #print('search left branch')
                    return search_recursion(tree.left, target)
                else:
                    # If there is nothing to the left of the tree, we
                    # know the value cannot exist in this tree.

                    #print('false')
                    return False
            else:
                # Same ase above, except we look to the tree's right.
                if tree.right:
                    #print('search right branch')
                    return search_recursion(tree.right, target)
                else:
                    #print('false')
                    return False

        # Run the recursion function.
        return search_recursion(self, target)

    # Return the maximum value found in the tree
    def get_max(self):
        # We just have to keep going right until we run into a node
        # that has no right node. That value will be the max one.
        max_value = self.value
        right = self.right
        while right:
            max_value = right.value
            right = right.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # Define recursion function.
        def for_each_recursion(tree, cb):
            # Apply the "cb" function to the tree's value.
            tree.value = cb(tree.value)
            if tree.left:
                # Run the recursion function on the tree's left,
                # if it exists.
                for_each_recursion(tree.left, cb)
            if tree.right:
                # Run the recursion function on the tree's right,
                # if it exists.
                for_each_recursion(tree.right, cb)

        # Run the recursion function on the tree's root.
        for_each_recursion(self, cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # I used this website: https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
        # In-order print means printing in the following order:
        # "Left, Root, Right."
        # So run this function on the left node (if it exists),
        # print the node's value,
        # then run the function on the right node (if it exists).
        if node.left:
            node.in_order_print(node.left)
        print(node.value)
        if node.right:
            node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Use a queue
        bft = Queue()
        # Start by enqueueing the base node.
        bft.enqueue(node)
        # Run a while loop as long as the queue has nodes in it.
        while bft.len() > 0:
            # Basically we want to dequeue a node, then enqueue any nodes
            # to its left or right. Then we print the node's value.
            # By running this iteratively, due to the way queues work,
            # we add nodes to the queue one layer at a time.
            node = bft.dequeue()
            if node.left:
                bft.enqueue(node.left)
            if node.right:
                bft.enqueue(node.right)
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # Same logic as the above, but we use a stack instead.
        dft = Stack()
        dft.push(node)
        while dft.len() > 0:
            node = dft.pop()
            if node.left:
                dft.push(node.left)
            if node.right:
                dft.push(node.right)
            print(node.value)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # Same logic as in_order_dft, we just do it in
        # "Root, Left, Right" order instead.
        print(node.value)
        if node.left:
            node.pre_order_dft(node.left)
        if node.right:
            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # Same logic as teh above, we just do it in
        # "Left, Right, Root" order instead.
        if node.left:
            node.post_order_dft(node.left)
        if node.right:
            node.post_order_dft(node.right)
        print(node.value)
