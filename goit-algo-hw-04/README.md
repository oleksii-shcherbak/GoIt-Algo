# Sorting Algorithms Benchmark

## Objective

This project performs an empirical comparison of three sorting algorithms:

- **Insertion Sort** – simple to implement, but with quadratic time complexity.
- **Merge Sort** – an efficient divide-and-conquer algorithm.
- **Timsort** – Python’s built-in hybrid algorithm combining merge sort and insertion sort.

The performance of each algorithm is tested using Python’s `timeit` module across various input sizes.

## Dataset Sizes Used

- 1,000 elements  
- 5,000 elements  
- 10,000 elements  
- 50,000 elements  

Each dataset consists of randomly generated integers in the range [0, 100000].

---

## Results

| Array Size | Insertion Sort (s) | Merge Sort (s) | Timsort (s) |
|------------|--------------------|----------------|-------------|
| 1,000      | 0.01166            | 0.00086        | 0.00006     |
| 5,000      | 0.26922            | 0.00530        | 0.00034     |
| 10,000     | 1.06816            | 0.01205        | 0.00073     |
| 50,000     | 27.44218           | 0.06714        | 0.00429     |

---

## Observations

- **Insertion Sort** exhibits poor scalability and becomes impractically slow for large datasets due to its O(n²) time complexity.
- **Merge Sort** demonstrates much better performance and predictable behavior (O(n log n)), suitable for larger input sizes.
- **Timsort**, Python’s built-in sorting algorithm, clearly outperforms both alternatives thanks to its adaptive nature and hybrid strategy.

---

## Conclusion

This empirical comparison validates the theoretical time complexities:

- **Insertion Sort** is inefficient beyond small arrays.
- **Merge Sort** provides reliable performance at scale.
- **Timsort is the most efficient** in practice and should be preferred for production use in Python.
