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
        if self.node is None:
            self.height = -1
        else:
            def dft_calculate_height(node):
                left_height = 0
                right_height = 0
                if node.left:
                    left_height += 1
                    #print('left height plus one')
                    left_height += dft_calculate_height(node.left.node)
                    #print('left_height:', left_height)
                if node.right:
                    right_height += 1
                    #print('right height plus one')
                    right_height += dft_calculate_height(node.right.node)
                    #print('right_height:', right_height)

                return max(left_height, right_height)

            self.height = dft_calculate_height(self.node)
            if self.node.left:
                self.node.left.update_height()
            if self.node.right:
                self.node.right.update_height()

    """
    Updates the balance factor on the AVLTree class
    """
    def update_balance(self):
        if self.node.left:
            left_height = self.node.left.height
        else:
            left_height = -1
        if self.node.right:
            right_height = self.node.right.height
        else:
            right_height = -1
        self.balance = left_height - right_height
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
        child = self.node.right
        old_child_left = child.node.left
        old_child_right = child.node.right
        old_self_left = self.node.left
        self.node, child.node = child.node, self.node
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
        self.update_height()
        self.update_balance()
        if self.balance in range(-1, 2):
            pass
        else:
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
            self.rebalance()
        
    """
    Uses the same insertion logic as a binary search tree
    after the value is inserted, we need to check to see
    if we need to rebalance
    """
    def insert(self, key):
        if not self.node:
            self.node = Node(key)
        else:
            def insert_recursion(tree, key):
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
