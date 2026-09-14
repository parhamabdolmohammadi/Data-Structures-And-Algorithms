# Data Structures and Algorithms

A collection of searching and sorting algorithms implemented in Python, with explanations of how each algorithm works and analysis of its time and space complexity.

---

## Searching Algorithms

Searching algorithms are used to find a specific value inside a collection of data.

In this implementation, I use **Linear Search, Binary Search, Ternary Search, Jump Search, and Exponential Search**.

> **Important:** Most of these algorithms require the array to be sorted first. Because this implementation creates and sorts a copy of the array, the returned index refers to the **sorted array**, not necessarily the original array.

### Linear Search

Linear Search checks every element one by one until the target value is found.

```text
[3, 7, 2, 9, 5]

Searching for 9:

3 → 7 → 2 → 9 ✓
```

In the best case, the target is the first element. In the average and worst cases, many or all elements may need to be checked.

| Case | Time Complexity |
| --- | ---: |
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |
| Space | O(1) |

---

### Binary Search

Binary Search works on a **sorted array**. Instead of checking every element, it compares the target with the middle element and eliminates half of the remaining search space.

```text
[1, 2, 3, 4, 5, 6, 7]
          ↑
        middle
```

Each recursive step reduces the search space approximately by half:

```text
n
n / 2
n / 4
n / 8
...
1
```

The search itself takes **O(log n)** time. Because the recursive implementation uses the call stack, its search space complexity is **O(log n)**.

However, this implementation first copies and sorts the array. Sorting takes **O(n log n)**, so when preprocessing is included, the overall running time becomes **O(n log n)**. The copied array requires **O(n)** additional space.

| Measure | Complexity |
| --- | ---: |
| Search Time | O(log n) |
| Recursive Search Space | O(log n) |
| Overall Time Including Sorting | O(n log n) |
| Overall Additional Space | O(n) |

---

### Iterative Binary Search

The iterative version of Binary Search uses a loop instead of recursion. It keeps track of three important values:

```text
beg
end
mid_index
```

After every comparison, either the left or right half is eliminated.

Both recursive and iterative Binary Search take **O(log n)** search time. The main difference is auxiliary space: the recursive version uses the call stack, while the iterative version only needs a few variables.

| Measure | Complexity |
| --- | ---: |
| Search Time | O(log n) |
| Search Space | O(1) |
| Overall Time Including Sorting | O(n log n) |
| Overall Additional Space | O(n) |

#### Recursive vs. Iterative Binary Search

| Version | Search Time | Search Space |
| --- | ---: | ---: |
| Recursive | O(log n) | O(log n) |
| Iterative | O(log n) | O(1) |

The iterative implementation is more space efficient.

---

### Ternary Search

Ternary Search is similar to Binary Search, but instead of splitting the search range into two sections, it splits it into **three sections**.

It uses two middle points:

```text
left      mid1      mid2      right
|----------|----------|----------|
```

The target is compared with both middle values, and only one-third of the search space is kept.

```text
n
n / 3
n / 9
n / 27
...
1
```

The search takes **O(log₃ n)** time, normally written as **O(log n)** in Big-O notation.

Because this implementation is recursive and also copies and sorts the input first:

| Measure | Complexity |
| --- | ---: |
| Search Time | O(log n) |
| Search Space | O(log n) |
| Overall Time Including Sorting | O(n log n) |
| Overall Additional Space | O(n) |

#### Binary Search vs. Ternary Search

Both algorithms have logarithmic search complexity. Binary Search divides the search space into two sections, while Ternary Search divides it into three.

Although Ternary Search eliminates more of the array per step, it normally performs more comparisons during each iteration. For normal sorted arrays, Binary Search is generally preferred.

---

### Jump Search

Jump Search requires a sorted array. Instead of checking every element, it jumps forward by blocks.

The ideal block size is approximately:

```text
√n
```

For an array containing 100 elements:

```text
√100 = 10

0 → 10 → 20 → 30 → ...
```

Once the algorithm finds the block where the target should exist, it performs a Linear Search inside that block.

The jumping phase and final linear scan each take approximately **O(√n)**, so the overall search remains **O(√n)**.

| Measure | Complexity |
| --- | ---: |
| Search Time | O(√n) |
| Search Space | O(1) |
| Overall Time Including Sorting | O(n log n) |
| Overall Additional Space | O(n) |

---

### Exponential Search

Exponential Search quickly identifies a range in which the target may exist.

It starts with a bound of `1` and repeatedly doubles it:

```text
1
2
4
8
16
32
...
```

After finding the range, Binary Search is performed inside that section.

Range discovery takes **O(log n)** and Binary Search also takes **O(log n)**. Because these happen sequentially, the complete search remains **O(log n)**.

In this implementation, the final Binary Search is recursive.

| Measure | Complexity |
| --- | ---: |
| Search Time | O(log n) |
| Search Space | O(log n) |
| Overall Time Including Sorting | O(n log n) |
| Overall Additional Space | O(n) |

---

### Searching Algorithms — Overall Comparison

| Algorithm | Search Time | Search Space | Requires Sorted Data? | Overall Time in This Implementation |
| --- | ---: | ---: | :---: | ---: |
| Linear Search | O(n) | O(1) | No | O(n) |
| Recursive Binary Search | O(log n) | O(log n) | Yes | O(n log n) |
| Iterative Binary Search | O(log n) | O(1) | Yes | O(n log n) |
| Ternary Search | O(log n) | O(log n) | Yes | O(n log n) |
| Jump Search | O(√n) | O(1) | Yes | O(n log n) |
| Exponential Search | O(log n) | O(log n) | Yes | O(n log n) |

If the input were already sorted, the actual search complexities would remain:

```text
Binary Search      → O(log n)
Ternary Search     → O(log n)
Jump Search        → O(√n)
Exponential Search → O(log n)
```

Overall, **Binary Search is usually the best general choice for searching a sorted array**, while Linear Search is useful when the data is unsorted or the array is very small.

---

## Sorting Algorithms

Sorting algorithms arrange data in a specific order, usually from smallest to largest or largest to smallest.

In this implementation, I use **Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, Counting Sort, and Bucket Sort**.

### Bubble Sort

Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.

```text
[5, 3, 8]

Compare 5 and 3 → swap

[3, 5, 8]
```

If Bubble Sort includes an early-exit optimization, an already sorted array can be handled in **O(n)**. This implementation does not use an early-exit flag, so it performs all passes.

| Case | Complexity |
| --- | ---: |
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |
| Space in This Implementation | O(n) |

The **O(n)** space comes from creating a copy using `self.__array[:]`.

---

### Selection Sort

Selection Sort repeatedly finds the smallest element in the unsorted portion and moves it into the correct position.

```text
[7, 3, 5, 1]

Smallest = 1
Swap with first position

[1, 3, 5, 7]
```

The remaining unsorted elements are always scanned, even if the array is already sorted.

| Case | Complexity |
| --- | ---: |
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |
| Space in This Implementation | O(n) |

The additional space comes from copying the original array.

---

### Insertion Sort

Insertion Sort builds a sorted section of the array one element at a time. It takes the current element and shifts larger elements to the right until the correct position is found.

```text
[3, 7, 4]

Take 4
Shift 7 right

[3, 4, 7]
```

If the array is already sorted, each element only needs one comparison.

| Case | Complexity |
| --- | ---: |
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) |

This version sorts `self.__array` directly.

---

### Merge Sort

Merge Sort uses a **divide-and-conquer** approach. It repeatedly divides the array into two halves until each subarray contains only one element.

```text
        [8, 4, 2, 6]
          /       \
      [8, 4]     [2, 6]
       /  \       /  \
     [8]  [4]   [2]  [6]
```

The smaller arrays are then merged back together in sorted order.

The array is divided into approximately `log n` levels, and all `n` elements are processed during merging at each level.

| Case | Complexity |
| --- | ---: |
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |
| Space | O(n) |

---

### Quick Sort

Quick Sort also uses **divide and conquer**. It selects a pivot, partitions the array around it, and recursively sorts the left and right sections.

In this implementation, the final element is selected as the pivot:

```python
pivot = array[end]
```

After partitioning, the pivot is in its final sorted position.

With good pivots, the array is divided approximately in half. If the pivot repeatedly becomes the smallest or largest value, however, the partitions can become highly unbalanced.

For example:

```text
[1, 2, 3, 4, 5]

Partitions:

4 and 0
3 and 0
2 and 0
1 and 0
```

| Case | Time Complexity |
| --- | ---: |
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n²) |
| Average Recursive Space | O(log n) |
| Worst Recursive Space | O(n) |

The public `quick_sort()` also creates a copy:

```python
array = self.__array[:]
```

so the complete implementation additionally uses **O(n)** space for that copy.

#### Partition

The partition function processes the current section once. It keeps `i` at the end of the smaller-values section, moves values smaller than the pivot to the left, and finally moves the pivot to `i + 1`.

| Measure | Complexity |
| --- | ---: |
| Time | O(n) |
| Auxiliary Space | O(1) |

---

### Counting Sort

Counting Sort does not compare elements directly. Instead, it creates a counting array where each index represents a possible value.

```text
Input:
[2, 1, 2, 3]

Counts:
index: 0  1  2  3
count: 0  1  2  1
```

The sorted array is reconstructed from these counts.

Let:

- `n` = number of elements
- `k` = range of possible values

| Measure | Complexity |
| --- | ---: |
| Time | O(n + k) |
| Space | O(k) |

Counting Sort is especially useful when the values are integers within a reasonably small range.

---

### Bucket Sort

Bucket Sort distributes values into several smaller buckets based on their values.

In this implementation, the number of buckets equals the number of elements:

```python
buckets = [[] for _ in range(n)]
```

Each item is assigned to a bucket using:

```python
bucket_index = int(
    item * (n - 1) / max_value
)
```

This maps values to valid bucket indexes from `0` to `n - 1`.

After distribution, each bucket is sorted using **Merge Sort**, and the buckets are combined into the final sorted array.

Because this implementation uses Merge Sort inside each bucket, its worst case differs from textbook versions that may use Insertion Sort. If every value falls into a single bucket, Merge Sort processes that bucket in **O(n log n)**.

| Measure | Complexity |
| --- | ---: |
| Distribution | O(n) |
| Best/Average | Depends on value distribution and bucket sorting cost |
| Worst | O(n log n) |
| Space | O(n) |

---

### Sorting Algorithms — Overall Comparison

| Algorithm | Best | Average | Worst | Additional Space |
| --- | ---: | ---: | ---: | ---: |
| Bubble Sort | O(n²) | O(n²) | O(n²) | O(n) in this implementation |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(n) in this implementation |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(n) overall due to copied array |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) |
| Bucket Sort | Distribution-dependent | Distribution-dependent | O(n log n) | O(n) |

For small or nearly sorted arrays, **Insertion Sort** can perform very well. For larger general-purpose arrays, **Merge Sort** and **Quick Sort** are usually much more efficient than Bubble Sort or Selection Sort.

**Counting Sort** can be extremely fast when integer values have a limited range, while **Bucket Sort** works best when values are distributed fairly evenly among buckets.

---

## Complexity Notation

- `n` — number of elements
- `k` — range of values or another algorithm-specific range
- `O(1)` — constant time
- `O(log n)` — logarithmic time
- `O(√n)` — square-root time
- `O(n)` — linear time
- `O(n log n)` — linearithmic time
- `O(n²)` — quadratic time

## Binary Trees — Binary Search Tree (BST)
A Binary Search Tree, or BST, is a data structure where each node can have a left child and a right child. The main rule is that values smaller than a node go to the left, while values greater than it go to the right. In my implementation, each node stores its value and references to its left and right children.

### Insert
    The insert function starts from the root and compares the new value with each node. If the value is smaller, it moves left; if it is larger, it moves right until it finds an empty position.

    Time Complexity: O(log n) average, O(n) worst case.

### Search
    The search function starts from the root and compares the target value with the current node. If the target is smaller, it searches the left subtree; if it is larger, it searches the right subtree. This continues until the value is found or there are no more nodes.

    Time Complexity: O(log n) average, O(n) worst case.

### Delete
    The delete operation searches for the node and removes it while maintaining the rules of the Binary Search Tree.

    Time Complexity: O(log n) average, O(n) worst case.

### Pre-Order Traversal
    The tree supports pre-order traversal, which visits the root first, then the left subtree, and finally the right subtree. Since every node must be visited once, the traversal depends on the total number of nodes.

    Time Complexity: O(n).

### Height
    The height function recursively calculates the height of the left and right subtrees and takes the larger value. In this implementation, an empty tree has a height of -1, while a leaf node has a height of 0. Because the function needs to visit every node to determine the maximum height, it takes linear time.

    Time Complexity: O(n).

### Minimum Value
    The minimum-value function finds the smallest value in the tree. In a Binary Search Tree, an optimized implementation can find the minimum by repeatedly moving to the left child until there is no left child.

    Time Complexity: O(log n) (optimized correct bst) average, O(n) worst case non bst tree.

### Equality
    The equality function checks whether two trees have the same structure and the same values in corresponding nodes. It recursively compares the left and right subtrees. In the worst case, every node needs to be compared.

    Time Complexity: O(n).

### BST Validation
    The validation function determines whether a tree follows the rules of a Binary Search Tree. Each node must stay within the correct minimum and maximum bounds determined by its ancestors. Since every node may need to be checked, the algorithm takes linear time.

    Time Complexity: O(n).

### Nodes at K Distance
    The nodes-at-k-distance function recursively moves through the tree until it reaches nodes that are exactly k edges away from the starting node. In the worst case, it may need to visit every node.

    Time Complexity: O(n).

### Level-Order Traversal — BFS
    The tree also supports level-order traversal, also known as Breadth-First Search (BFS). It visits the tree one level at a time, normally using a queue. Every node is visited once.

    Time Complexity: O(n).

### Overall Complexity
    When the Binary Search Tree is reasonably balanced:

    Search: O(log n).
    Insert: O(log n).
    Delete: O(log n).

    If the tree becomes completely unbalanced, it can behave similarly to a linked list:

    Search: O(n).
    Insert: O(n).
    Delete: O(n).

    The tree itself stores n nodes.

    Space Complexity: O(n).

Overall, a Binary Search Tree provides efficient searching, insertion, and deletion when it remains balanced, but these operations can degrade from O(log n) to O(n) when the tree becomes heavily unbalanced.


## AVL Tree
An AVL Tree is a self-balancing Binary Search Tree. It follows the normal BST rule, where smaller values go to the left and larger values go to the right, but it also keeps the tree balanced after every insertion.

Each node stores four things: its value, its left child, its right child, and its height.

### Insert
    The insert function first inserts the new value like a normal Binary Search Tree. After the insertion, it updates the height of the current node and checks whether that node has become unbalanced.

    Because an AVL tree keeps itself balanced, insertion takes O(log n) time in both the average and worst case.

    Time Complexity: O(log n).

### Height
    The tree stores the height of every node. The __get_height function simply returns the stored height of a node, or -1 if the node does not exist.

    Because the height is already stored inside the node, we do not need to calculate it recursively every time.

    Time Complexity: O(1).

### Balance Factor
    The balance factor determines whether a node is balanced.

    It is calculated as:

    left subtree height - right subtree height

    If the result is between -1 and 1, the node is balanced.

    If it is greater than 1, the node is left-heavy.

    If it is less than -1, the node is right-heavy.

    Time Complexity: O(1).

### Right-Heavy Check
    The __is_right_heavy function checks whether the balance factor is less than -1.

    If it is, the right side of the tree is too tall and a rotation is required.

    Time Complexity: O(1).

### Left-Heavy Check
    The __is_left_heavy function checks whether the balance factor is greater than 1.

    If it is, the left side of the tree is too tall and a rotation is required.

    Time Complexity: O(1).

### Left Rotation
    A left rotation is normally used when the tree is too heavy on the right side.

    For example:

    10
    \
    20
        \
        30

    After a left rotation:

        20
    /  \
    10    30

    The rotation only changes a small number of references between nodes and then updates their heights:
            then we upgrade the height of old root which is lower then new root which is higher since only height of these two are changed in every rotation

    Time Complexity: O(1).

### Right Rotation
    A right rotation is normally used when the tree is too heavy on the left side.

    For example:

        30
        /
        20
    /
    10

    After a right rotation:

        20
    /  \
    10    30

    Like the left rotation, it only changes a few references and updates node heights:
            then we upgrade the height of old root which is lower then new root which is higher since only height of these two are changed in every rotation

    Time Complexity: O(1).

### Right-Left Case
    A Right-Left case happens when a node is right-heavy < -1, but its right child is left-heavy > 0.

    The tree first performs a right rotation on the right child, followed by a left rotation on the unbalanced node.

    Each rotation takes constant time.

    Time Complexity: O(1) for the rotations.

### Left-Right Case
    A Left-Right case happens when a node is left-heavy 1 > , but its left child is right-heavy < 0.

    The tree first performs a left rotation on the left child, followed by a right rotation on the unbalanced node.

    Time Complexity: O(1) for the rotations.

### Resetting Node Height
    After insertion or rotation, the node's height must be updated.

    The new height is calculated using the greater height of its two children plus one.

    Because the children's heights are already stored, this calculation is constant time.

    Time Complexity: O(1).

### Child Height
    The __get_child_height function gets the heights of the left and right children.

    Since both values are already stored in the nodes, this takes constant time.

    Time Complexity: O(1).

### Printing the Tree
    The print_tree function recursively visits the nodes and displays each node with its value, height, left-child height, and right-child height.

    Since every node may need to be visited, the running time depends on the total number of nodes.

    Time Complexity: O(n).

### Overall Complexity
    Because the AVL Tree automatically keeps itself balanced, its height remains approximately O(log n).

    Therefore:

    Search: O(log n).
    Insert: O(log n).
    Delete: O(log n).

    The rotations themselves are very fast:

    Left Rotation: O(1).
    Right Rotation: O(1).
    Balance Factor: O(1).
    Height Lookup: O(1).

    The recursive insertion uses the call stack, and the tree height is O(log n).

    Space Complexity for insertion: O(log n).

    The entire tree stores n nodes.

    Total Tree Space Complexity: O(n).

Overall, the main advantage of an AVL Tree over a normal Binary Search Tree is that it prevents the tree from becoming heavily unbalanced. Because of this, searching, insertion, and deletion remain O(log n) even in the worst case.


## Max Heap

A **Max Heap** is a complete binary tree where every parent is greater than or equal to its children. In this implementation, the heap is stored inside an array instead of using separate node objects.

The root of a Max Heap always contains the **largest value**.

### Insert

    The **insert** function first places the new value at the end of the heap. After that, it uses **bubble up** to move the value upward until the Max Heap property is restored.

    Because the height of a heap is logarithmic, the inserted value can move upward at most `O(log n)` levels.

    **Time Complexity: O(log n).**

If the underlying array becomes full, the array is doubled and all existing values are copied into the new array.

    **Resize Time Complexity: O(n).**

The heap can store up to `n` values.

    **Total Heap Space Complexity: O(n).**

### Bubble Up

    The **bubble up** function compares a node with its parent. If the child is greater than the parent, they are swapped. The process continues recursively until the node reaches the correct position.

    The node can move from the bottom of the heap to the root, which is at most the height of the heap.

    **Time Complexity: O(log n).**

    Because this implementation uses recursion, each recursive call uses stack memory.

    **Space Complexity: O(log n).**

### Parent Index

    The parent index of a node is calculated using:

    (index - 1) // 2

    This calculation does not depend on the size of the heap.

    **Time Complexity: O(1).**

    **Space Complexity: O(1).**

### Remove

    The **remove** function removes and returns the maximum value, which is stored at the root.

    First, the root value is saved. Then the last element in the heap is moved to the root. The heap size is reduced, and **bubble down** is used to restore the Max Heap property.

    The bubble-down process can move through the height of the heap.

    **Time Complexity: O(log n).**

### Bubble Down

    The **bubble down** function compares the current node with its left and right children. It selects the larger child, and if that child is greater than the current node, they are swapped.

    This process continues until the node reaches the correct position.

    Because the node can move down at most the height of the heap:

    **Time Complexity: O(log n).**

    Because this implementation is recursive:

    **Space Complexity: O(log n).**

### Left Child

The left child index is calculated using:

    index * 2 + 1

    This is a direct mathematical calculation.

    **Time Complexity: O(1).**

    **Space Complexity: O(1).**

### Right Child

The right child index is calculated using:

    index * 2 + 2

    This is also a direct calculation.

    **Time Complexity: O(1).**

    **Space Complexity: O(1).**

### Swap

    The **swap** function exchanges two values in the internal heap array.

    Only two array positions are changed.

    **Time Complexity: O(1).**

    **Space Complexity: O(1).**

### Heapify

    The **heapify** function converts a normal array into a Max Heap.

    It starts from the last parent node and performs bubble down on each parent moving toward the root.

    Even though an individual bubble-down operation can take `O(log n)`, building the entire heap this way has a tighter overall bound.

    **Time Complexity: O(n).**

    The heapify operation modifies the provided array directly instead of creating another heap.

    **Space Complexity: O(1).**

### Bubble Down During Heapify

    The `__bubble_down_array` function is used by heapify. It compares a node with its children and repeatedly swaps it with the larger child until the heap property is restored.

    A single node can move through the height of the heap.

    **Time Complexity: O(log n).**

    **Space Complexity: O(1).**

### Kth Largest Value

    The `get_kth_largest_number` function first creates a Max Heap by inserting every value from the input array.

    Inserting `n` values individually takes:

    **Time Complexity: O(n log n).**

    After the heap is created, the maximum value is removed `k` times. Each removal takes `O(log n)`.

    Therefore:

    **Removal Time Complexity: O(k log n).**

    The total running time is:

    ```text
    O(n log n + k log n)
    ```

    which can also be written as:

    ```text
    O((n + k) log n)
    ```

    The temporary heap stores the input values.

    **Space Complexity: O(n).**

### String Representation

    The `__str__` function returns the active heap values as a string.

    Because it slices the internal array and processes the heap values:

    **Time Complexity: O(n).**

    The slice creates another list containing the heap values.

    **Space Complexity: O(n).**

### Iteration

    The `__iter__` function allows the heap to be used in a loop.

    It creates a slice containing the active heap elements.

    Iterating through all heap values takes:

    **Time Complexity: O(n).**

    Because the slice creates another list:

    **Space Complexity: O(n).**

### Boolean Check

    The `__bool__` function checks whether the heap contains at least one value.

    It simply compares the heap size with zero.

    **Time Complexity: O(1).**

    **Space Complexity: O(1).**

### Overall Complexity

    The most important Max Heap operations are:

    **Insert: O(log n).**

    **Remove Maximum: O(log n).**

    **Peek Maximum: O(1), if implemented by reading the root.**

    **Heapify: O(n).**

    **Bubble Up: O(log n).**

    **Bubble Down: O(log n).**

    The heap stores its values in an array.

    **Total Space Complexity: O(n).**

    Overall, a Max Heap is useful when we frequently need access to the largest value. The maximum value is always stored at the root, while insertion and removal remain efficient because the height of a heap is **O(log n)**.


## Trie
A Trie is a tree-based data structure used mainly for storing and searching strings efficiently.

Each node represents a single character, and in this implementation every node has an array of 26 possible children, one for each lowercase English letter from a to z.

Each node also stores a Boolean value called is_end, which tells us whether that node represents the end of a complete word.

### Node Creation
Each Trie node stores its character value, its is_end status, and an array of 26 child references.

Because the number of children is always fixed at 26, creating a node takes constant time.

Time Complexity: O(1).

Space Complexity: O(1) per node.

### Character Index
The Trie converts each lowercase character into an array index using:

ord(char) - 97

For example:

a → 0
b → 1
c → 2
...
z → 25

This allows the Trie to directly access the correct child position.

Time Complexity: O(1).

### Insert
The insert function adds a word into the Trie one character at a time.

It begins at the root and processes each character in the word. For every character, it calculates the corresponding index and checks whether a child already exists there.

If the child does not exist, a new node is created.

The function then moves to that child and continues until the entire word has been inserted.

At the final character, is_end is set to True so the Trie knows that a complete word ends at that node.

If the word contains n characters, each character is processed once.

Time Complexity: O(n).

In the worst case, every character creates a new node.

Space Complexity: O(n).

### Contains
The contains function checks whether a complete word exists in the Trie.

It starts at the root and follows the child corresponding to each character.

If at any point the expected child does not exist, the function returns False.

After reaching the final character, it checks is_end to make sure the path represents a complete word and not only a prefix.

For a word of length n, every character is checked once.

Time Complexity: O(n).

The function does not create any additional data structure.

Space Complexity: O(1).

### Why is_end Is Important
Suppose the Trie contains:

car

The path:

c → a

exists, but "ca" was never inserted as a complete word.

The is_end flag allows the Trie to distinguish between a complete word and only part of another word.

Checking this value takes constant time.

Time Complexity: O(1).

### Get Child
The get_children function directly accesses one child using its index.

Since array access is constant time:

Time Complexity: O(1).

Space Complexity: O(1).

### Set Child
The set_children function creates a new child node and places it at a specific index in the children array.

Because the position is accessed directly:

Time Complexity: O(1).

Space Complexity: O(1) for the new node.

### Remove Child
The remove_child function removes a child reference by replacing it with None.

Because the child is accessed directly by index:

Time Complexity: O(1).

Space Complexity: O(1).

### Has Children
The has_children function checks whether a node has any children.

It loops through the node's 26 possible child positions.

Since there are always exactly 26 positions, this is treated as a constant amount of work.

Time Complexity: O(26), which simplifies to O(1).

Space Complexity: O(1).

### Remove
The remove function deletes a word from the Trie recursively.

It follows the characters of the word until reaching the final node.

When the final node is reached, its is_end value is changed to False.

Then, while recursion returns upward, unnecessary nodes are removed if they are no longer part of another word.

For example, if we have:

car
cart

and remove:

cart

the nodes belonging only to "cart" can be removed, but the nodes for "car" must remain.

The recursion follows at most the length of the word.

Time Complexity: O(n).

Because the recursive call stack can contain one call for every character:

Space Complexity: O(n).

### Autocomplete
The autocomplete function returns all words that begin with a particular prefix.

First, it follows the prefix through the Trie.

For example, for:

prefix = "ca"

it moves through:

root → c → a

Finding the prefix takes time proportional to the prefix length.

Prefix Search Time Complexity: O(p).

Here, p is the length of the prefix.

After finding the prefix node, the Trie recursively explores all words below that node.

If k represents the total number of characters explored while collecting matching words:

Collection Time Complexity: O(k).

Therefore, the total autocomplete complexity is:

O(p + k)

Time Complexity: O(p + k).

The resulting matching words are stored in a list.

Space Complexity: O(k), plus recursive stack space.

### Collect Words
The __collect_words function recursively performs a traversal starting from the prefix node.

Whenever it reaches a node where is_end is True, the current prefix is added to the result list.

Then it recursively explores every existing child.

Because the function explores all relevant nodes below the prefix:

Time Complexity: O(k).

If the deepest remaining branch has height h, recursion may create up to h active calls.

Recursive Space Complexity: O(h).

The result list itself may require additional space for the collected words.

### Overall Trie Complexity
The most important Trie operations are:

Insert: O(n).

Search / Contains: O(n).

Remove: O(n).

Autocomplete: O(p + k).

Get Child: O(1).

Set Child: O(1).

Remove Child: O(1).

Has Children: O(1), because only 26 child positions are checked.

Here, n is the length of the word, p is the length of the prefix, and k represents the amount of Trie data explored while collecting autocomplete results.

The main advantage of a Trie is that searching depends mostly on the length of the word, rather than on the total number of words stored.

For example, searching for a 6-character word requires at most about 6 character steps, regardless of whether the Trie contains 100 words or 100,000 words.

Overall, Tries are especially useful for dictionaries, prefix searching, autocomplete systems, and word lookup.

---

## Graph

A **Graph** is a data structure made of **nodes**, also called vertices, and **edges** that connect those nodes.

In this implementation, the graph is a **directed graph** and uses an **adjacency list**. Each node is stored in a dictionary, and every node has a linked list containing its neighboring nodes.

### Add Node

    The **add_node** function creates a new node and stores it in the graph.

    The node is added to the nodes dictionary, and a new empty linked list is created for its adjacency list.

    Dictionary insertion is usually constant time.

    **Average Time Complexity: O(1).**

    Because dictionary operations can degrade because of hash collisions:

    **Worst Time Complexity: O(V).**

    **Space Complexity: O(1) per added node.**

### Add Edge

    The **add_edge** function creates a directed connection from one node to another.

    First, it finds the two nodes. Then the destination node is added to the adjacency list of the source node.

    For example:

    ```text
    A → B
    ```

    means there is an edge from `A` to `B`.

    Because adding to the end of the linked list is constant time:

    **Time Complexity: O(1).**

    **Space Complexity: O(1) per edge.**

### Remove Node

    The **remove_node** function removes a node from the graph.

    Before deleting the node, the algorithm goes through the other adjacency lists and removes any edges that point to that node.

    Because every node and potentially every edge may need to be checked:

    **Time Complexity: O(V + E).**

    **Space Complexity: O(1).**

### Remove Edge

    The **remove_edge** function removes a connection between two nodes.

    Since the neighbors are stored in a linked list, the linked list may need to be traversed to find the correct edge.

    **Time Complexity: O(E) in the worst case.**

    **Space Complexity: O(1).**

### Recursive Depth-First Search

    **Depth-First Search**, or DFS, explores one path of the graph as deeply as possible before going back and trying another path.

    The recursive implementation uses a stack and a list of visited nodes.

    In a standard optimized graph implementation:

    **General DFS Time Complexity: O(V + E).**

    However, in this implementation, `visited_nodes` is a list. Checking:

    ```python
    node in visited_nodes
    ```

    can take O(V) time.

    The neighbors are also sorted before being added to the stack.

    Because of this:

    **Time Complexity in this implementation: O(V² + E).**

    The visited list and recursive stack may contain up to V nodes.

    **Space Complexity: O(V).**

### Iterative Depth-First Search

    The **iterative DFS** performs the same type of traversal, but instead of recursion it explicitly uses a stack.

    A node is removed from the stack, marked as visited, and then its unvisited neighbors are added to the stack.

    A standard DFS would have:

    **General Time Complexity: O(V + E).**

    In this implementation, list membership checks such as:

    ```python
    node not in visited_nodes
    ```

    take O(V), and neighbors are also sorted.

    Therefore:

    **Time Complexity in this implementation: O(V² + E).**

    The stack and visited list can store up to V nodes.

    **Space Complexity: O(V).**

### Breadth-First Search

    **Breadth-First Search**, or BFS, explores the graph one level at a time.

    It starts from a node, visits its neighbors, then visits the neighbors of those nodes.

    BFS normally uses a queue.

    A standard BFS has:

    **General Time Complexity: O(V + E).**

    In this implementation, the queue is a Python list and uses operations such as:

    ```python
    queue.pop(0)
    ```

    and list membership checks.

    Removing index zero from a Python list requires shifting elements, which increases the running time.

    Therefore:

    **Time Complexity in this implementation: O(V² + E).**

    The queue and visited list may store up to V nodes.

    **Space Complexity: O(V).**

### Get Weight

    The **get_weight** function assigns a numeric weight to a node label.

    It processes each character of the label and calculates a value based on the character and its position.

    If the label has `m` characters:

    **Time Complexity: O(m).**

    **Space Complexity: O(1).**

### Topological Sort

    A **topological sort** returns the nodes of a directed graph in an order where a node appears before the nodes that depend on it.

    Topological sort only works if the graph is a **Directed Acyclic Graph**, also called a DAG.

    This implementation first checks whether the graph contains a cycle. Then it uses DFS and adds each node to a stack after visiting its neighbors.

    Each node and edge is processed once.

    **Time Complexity: O(V + E).**

    The visited set and stack can contain up to V nodes.

    **Space Complexity: O(V).**

### Cycle Detection

    The **has_cycle** function checks whether the directed graph contains a cycle.

    It uses two sets:

    ```text
    visiting
    visited
    ```

    `visiting` contains nodes that are currently part of the recursive path.

    `visited` contains nodes that have already been completely processed.

    If the algorithm reaches a node that is already inside `visiting`, a cycle has been found.

    For example:

    ```text
    A → B → C
    ↑       ↓
    └───────┘
    ```

    Each node is visited once and each edge is checked once.

    **Time Complexity: O(V + E).**

    The two sets and recursive call stack may contain up to V nodes.

    **Space Complexity: O(V).**

### Overall Complexity

    The important operations in this Graph implementation are:

    **Add Node: O(1) average, O(V) worst case.**

    **Add Edge: O(1).**

    **Remove Node: O(V + E).**

    **Remove Edge: O(E) worst case.**

    **Recursive DFS: O(V + E) 

    **Iterative DFS: O(v + E) 

    **BFS: O(V + E) 

    **Topological Sort: O(V + E).**

    **Cycle Detection: O(V + E).**

    Here, `V` represents the number of vertices and `E` represents the number of edges.

    A normal optimized DFS or BFS using a `set` for visited nodes and a proper queue such as `deque` would normally run in:

    **Time Complexity: O(V + E).**

    Overall, adjacency lists are especially efficient for graphs where each node is connected to only a relatively small number of other nodes.


## Weighted Graph
A Weighted Graph is a graph where each edge has a numerical value called a weight.

The weight can represent things such as distance, cost, time, or difficulty.

In this implementation, the graph is undirected, which means when an edge is added from A to B, another edge is also added from B to A. Each node is stored in a dictionary, and each adjacency list stores Edge objects containing the source node, destination node, and weight.

### Add Node
    The add_node function creates a new node if the label does not already exist.

    The node is stored in the nodes dictionary, and an empty adjacency list is created for it.

    Dictionary insertion is usually constant time.

    Average Time Complexity: O(1).

    In the worst case, hash collisions can make dictionary operations slower.

    Worst Time Complexity: O(V).

    Space Complexity: O(1) per added node.

### Add Edge
    The add_edge function connects two nodes using a weight.

    Because the graph is undirected, two edges are created:

    A → B
    B → A

    Both edges have the same weight.

    Appending each edge to an adjacency list is constant time.

    Time Complexity: O(1).

    Space Complexity: O(1) per edge insertion.

### Shortest Distance
    The get_shortest_distance function finds the shortest weighted distance between two nodes.

    It uses a version of Dijkstra's algorithm.

    At the beginning, every node is given an infinite distance except the starting node, which has distance zero.

    The algorithm then repeatedly relaxes edges and updates a neighbor's distance if a shorter path is found.

    For example, if we have:

    A --3-- B --1-- E

    A --2-- D --6-- B

    the algorithm compares possible routes and keeps the smallest known distance.

    In the standard optimized implementation using a priority queue:

    General Time Complexity: O((V + E) log V).

    However, this implementation scans all nodes to find the next closest unvisited node instead of using a priority queue.

    Time Complexity in this implementation: O(V² + E).

    The distances dictionary stores information for every node.

    Space Complexity: O(V).

### Edge Relaxation
    During Dijkstra's algorithm, the algorithm calculates:

    new distance =
    current distance + edge weight

    If the new distance is smaller than the previously known distance, the distance and previous node are updated.

    This process is called relaxation.

    Across the entire algorithm, the edges contribute:

    Time Complexity: O(E).

    Finding the Next Closest Node

    After processing the current node's edges, the implementation scans the distances dictionary to find the closest unvisited node.

    Because this scan may examine all V vertices, it takes:

    Time Complexity: O(V) per selection.

    Since this can happen for many vertices, it is the main reason this version of Dijkstra becomes:

    Overall Time Complexity: O(V² + E).

### Shortest Path
    The get_shortest_path function returns the actual route rather than only the distance.

    The algorithm stores the previous node for every node whose distance is updated.

    After reaching the destination, it follows those previous-node references backward and places the nodes into a stack.

    The stack is then popped to create the path in the correct order.

    For example:

    A → B → E

    The path reconstruction may process up to V nodes.

    Path Reconstruction Time Complexity: O(V).

    Space Complexity: O(V).

### Cycle Detection
    The has_cycle function determines whether the undirected weighted graph contains a cycle.

    It uses DFS along with visiting and visited sets.

    Because the graph is undirected, the algorithm also keeps track of the parent node.

    This is important because when moving from A to B, the edge from B back to A should not automatically be considered a cycle.

    Each node and edge is processed a constant number of times.

    Time Complexity: O(V + E).

    The sets and recursive call stack can store up to V nodes.

    Space Complexity: O(V).

### Minimum Spanning Tree
    A Minimum Spanning Tree, or MST, connects all vertices using the minimum possible total edge weight without creating unnecessary cycles.

    This implementation uses Prim's algorithm.

    The algorithm begins from one node and repeatedly chooses the smallest available edge that connects to an unvisited node.

    For example:

    A --2-- D
    A --3-- B
    A --4-- C
    B --1-- E

    Prim's algorithm keeps choosing the cheapest useful edge until all vertices are connected.

    Prim's Algorithm in This Implementation

    This version stores candidate edges inside a normal list.

    To find the minimum edge, it scans the available edges.

    It also uses lists for visited and unvisited nodes.

    Because of those linear scans:

    Time Complexity: O(VE).

    For a dense graph where E can approach V²:

    Worst Dense-Graph Time Complexity: O(V³).

    The algorithm stores vertices and candidate edges.

    Space Complexity: O(V + E).

### Adding Available Edges
    The __add_to_available_edges function adds edges connected to the current node into the candidate-edge list.

    It also checks whether each edge is already in the list.

    Because list membership checking is linear, this can become expensive.

    Time Complexity: up to O(E²) contribution in the worst case.

    Using a set could improve membership checking to approximately O(1) average.

### Optimized Prim's Algorithm
    The class also contains a more standard version of Prim's algorithm using Python's heapq.

    A min-heap allows the algorithm to efficiently retrieve the smallest available edge.

    Each heap push or pop takes logarithmic time.

    Time Complexity: O((V + E) log E).

    This is commonly simplified for graph analysis to:

    Time Complexity: O(E log V).

    The visited set, heap, and MST edge list require:

    Space Complexity: O(V + E).

### Overall Complexity
    The most important operations in this Weighted Graph are:

    Add Node: O(1) average.

    Add Edge: O(1).


    Optimized Dijkstra with a priority queue: Time Complexity:
        O((V + E) log V)

    Space Complexity:
        O(V + E)

    Cycle Detection: O(V + E).

    Prim's MST in this implementation: O(VE).

    Optimized Prim with a heap: O(v + E log V). in melake

    Here, V is the number of vertices and E is the number of edges.

    Overall, weighted graphs are useful when the connections between nodes have different costs. Algorithms such as Dijkstra's algorithm are used to find shortest paths, while Prim's algorithm is used to create a minimum spanning tree with the smallest possible total edge weight

