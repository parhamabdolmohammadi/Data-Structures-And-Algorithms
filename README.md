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
