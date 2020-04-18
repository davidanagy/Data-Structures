"""
Node class to keep track of
the data internal to individual nodes
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""
A tree class to keep track of things like the
balance factor and the rebalancing logic
"""
class AVLTree:
    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    """
    Display the whole tree. Uses recursive def.
    """
    def display(self, level=0, pref=''):
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None: 
            print ('-' * level * 2, pref, self.node.key,
                   f'[{self.height}:{self.balance}]',
                   'L' if self.height == 0 else ' ')
            if self.node.left != None:
                self.node.left.display(level + 1, '<')
            if self.node.right != None:
                self.node.right.display(level + 1, '>')

    """
    Computes the maximum number of levels there are
    in the tree
    """
    def update_height(self):
        # If there's no node on this tree, set height to -1
        if self.node is None:
            self.height = -1
        else:
            # Calculate height with a depth-first traversal
            def dft_calculate_height(node):
                # Begin with left_height and right_height at 0.
                # (The minimum value is 0 because this tree must
                # have at least one node.)
                left_height = 0
                right_height = 0
                if node.left:
                    # Add 1 to the left_height if it has a left node.
                    left_height += 1
                    # (The commented-out print statements were for
                    # error-checking.)
                    #print('left height plus one')
                    # Re-run this function on the left node to calculate
                    # its height, and add the result.
                    left_height += dft_calculate_height(node.left.node)
                    #print('left_height:', left_height)
                if node.right:
                    # Same as the above, just for the right node.
                    right_height += 1
                    #print('right height plus one')
                    right_height += dft_calculate_height(node.right.node)
                    #print('right_height:', right_height)

                # Return the bigger height
                return max(left_height, right_height)

            # Calculate height of self.
            self.height = dft_calculate_height(self.node)
            # Re-run this function on the left and right nodes, if they exist,
            # so that the height of each node is updated.
            if self.node.left:
                self.node.left.update_height()
            if self.node.right:
                self.node.right.update_height()

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        # Start by calculating the heights of the left and right
        # branches.
        if self.node.left:
            left_height = self.node.left.height
        else:
            # If there is no left node, set left_height to -1,
            # as the convention in this class is that the height
            # of a nodeless branch is -1 due to zero-indexing.
            left_height = -1
        # Do same for right_height
        if self.node.right:
            right_height = self.node.right.height
        else:
            right_height = -1
        # Subtract right_height from left_height
        self.balance = left_height - right_height
        # Run this function on all nodes so every node's balance
        # is updated.
        if self.node.left:
            self.node.left.update_balance()
        if self.node.right:
            self.node.right.update_balance()

    """
    Perform a left rotation, making the right child of this
    node the parent and making the old parent the left child
    of the new parent. 
    """
    def left_rotate(self):
        # The goal is not merely to flip the parent and child.
        # We also have to update the right/left branches of each.
        # (The details are taken from the diagram in the repo's ReadMe.)
        child = self.node.right
        # I had to save these as variables before swapping the nodes,
        # since I ran into problems when I didn't.
        old_child_left = child.node.left
        old_child_right = child.node.right
        old_self_left = self.node.left
        self.node, child.node = child.node, self.node
        # Note that, at this point, "child" is the old "parent"
        # and "self" is the old child.
        child.node.left = old_self_left
        child.node.right = old_child_left
        self.node.right = old_child_right
        self.node.left = child

    """
    Perform a right rotation, making the left child of this
    node the parent and making the old parent the right child
    of the new parent. 
    """
    def right_rotate(self):
        # Very similar process as left_rotate.
        child = self.node.left
        old_child_left = child.node.left
        old_child_right = child.node.right
        old_self_right = self.node.right
        self.node, child.node = child.node, self.node
        child.node.left = old_child_right
        child.node.right = old_self_right
        self.node.left = old_child_left
        self.node.right = child


    """
    Sets in motion the rebalancing logic to ensure the
    tree is balanced such that the balance factor is
    1 or -1
    """
    def rebalance(self):
        # Start by updating the height and balance.
        self.update_height()
        self.update_balance()
        if self.balance in range(-1, 2):
            # If the balance is -1, 0, or 1, do nothing.
            pass
        else:
            # I used the diagram in the ReadMe for help with this,
            # as well as this website: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
            if self.balance >= 2:
                if self.node.left.balance < 0:
                    # left right case
                    self.node.left.left_rotate()
                    self.right_rotate()
                else:
                    # left left case
                    self.right_rotate()
            else:
                if self.node.right.balance > 0:
                    # right left case
                    self.node.right.right_rotate()
                    self.left_rotate()
                else:
                    # right right case
                    self.left_rotate()
            # Rebalance again until the balance is in the correct range.
            self.rebalance()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if not self.node:
            # If there is no node in this branch, just add the key
            # as a new node.
            self.node = Node(key)
        else:
            def insert_recursion(tree, key):
                # The logic here is the same as a binary search tree,
                # we just rebalance after each recursion call.
                node = tree.node
                if key < node.key:
                    if node.left:
                        insert_recursion(node.left, key)
                        tree.rebalance()
                    else:
                        node.left = AVLTree(Node(key))
                        tree.rebalance()
                else:
                    if node.right:
                        insert_recursion(node.right, key)
                        tree.rebalance()
                    else:
                        node.right = AVLTree(Node(key))
                        tree.rebalance()

            insert_recursion(self, key)
