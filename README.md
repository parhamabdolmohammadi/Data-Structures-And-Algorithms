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
