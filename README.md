## Dynamic Array

This implementation creates a resizable array structure similar to a simplified dynamic array.

The array starts with a fixed capacity. When the array becomes full, its capacity is doubled and the existing elements are copied into a new larger array.

### Main Operations

| Operation                | Time Complexity | Explanation                                                                                          |
| ------------------------ | --------------: | ---------------------------------------------------------------------------------------------------- |
| `insert()`               |  O(1) amortized | Inserts at the end. Most insertions are constant time.                                               |
| `insert()` when resizing |            O(n) | When capacity is full, all existing elements must be copied into a larger array.                     |
| `remove_at()`            |            O(n) | Removing an element requires shifting all elements after the removed index one position to the left. |
| `index_of()`             |            O(n) | Performs a linear search through the array.                                                          |
| Access by index          |            O(1) | Direct array indexing is constant time.                                                              |
| `_grow()`                |            O(n) | Copies all elements into a new array with double the capacity.                                       |
| `_shrinkage()`           |            O(n) | Shifts elements left after a removal.                                                                |

### How It Works

The array keeps track of two important values:

- `size` — the current capacity of the internal array.
- `index` — the number of elements currently stored.

The internal storage is initialized using:

```python
self.my_array = [None] * size
```

Perfect — this gives us the Singly Linked List section.

For your implementation, I’d document it like this:

## Singly Linked List

This implementation creates a singly linked list where each node stores a value and a reference to the next node.

The list maintains references to both the first and last nodes, which makes insertion at either end efficient.

### Structure

Each node contains:

- `value` — the data stored in the node
- `next` — a reference to the next node

Example:

```text
first
  ↓
[10] → [20] → [30] → None
                  ↑
                 last

Because this is a singly linked list, nodes only know about the node that comes after them.

Main Operations
Operation	Time Complexity	Explanation
add_first()	O(1)	Inserts a node at the beginning by changing the first reference.
add_last()	O(1)	Uses the stored last reference to append directly to the end.
delete_first()	O(1)	Moves the first reference to the second node.
delete_last()	O(n)	Must traverse the list to find the node before the last node.
contains()	O(n)	Traverses nodes until the value is found or the end is reached.
index_of()	O(n)	Performs a linear traversal while tracking the current index.
to_array()	O(n)	Visits every node and inserts its value into an array.
reverse()	O(n)	Visits each node once and reverses its next reference.
kth_node_end()	O(n)	Uses two pointers separated by k positions and traverses the list once.
print()	O(n)	Visits every node to build the list representation.
Size lookup	O(1)	The list keeps track of its size in __size.
Space Complexity

The linked list requires:

O(n)

space because each element is stored in its own node.

Each node also stores one additional reference to the next node.
```
