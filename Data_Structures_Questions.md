Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

**Answer:** O(1)

2. What is the runtime complexity of `dequeue`?

**Answer:** O(1)

3. What is the runtime complexity of `len`?

**Answer:** O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

**Answer:** Worst case is O(n); average case is O(log n).

2. What is the runtime complexity of `contains`?

**Answer:** Worse case is O(n); average case is O(log n).

3. What is the runtime complexity of `get_max`?

**Answer:** Worst case is O(n); average case is O(log n).

## Heap

1. What is the runtime complexity of `_bubble_up`?

**Answer:** O(1)

2. What is the runtime complexity of `_sift_down`?

**Answer:** O(1)

3. What is the runtime complexity of `insert`?

**Answer:** O(log n)

4. What is the runtime complexity of `delete`?

**Answer:** O(log n)

5. What is the runtime complexity of `get_max`?

**Answer:** O(1)

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

**Answer:** O(1)

2. What is the runtime complexity of `ListNode.insert_before`?

**Answer:** O(1)

3. What is the runtime complexity of `ListNode.delete`?

**Answer:** O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

**Answer:** O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

**Answer:** O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

**Answer:** O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

**Answer:** O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

**Answer:** O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

**Answer:** O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?

**Answer:** O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    **Answer:** The DLL's method has a much faster runtime (removing from an Array is O(n) worst case), but it does require that you have a variable pointing to the relevant node; i.e., it's not enough to just know what the value is you want to remove.