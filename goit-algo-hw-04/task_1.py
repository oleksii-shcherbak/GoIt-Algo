import random
import timeit
import pandas as pd

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Generate test arrays and measure execution time
def measure_sorting_algorithms():
    sizes = [1000, 5000, 10000, 50000]
    results = []

    for size in sizes:
        print(f"\nTesting with array size: {size}")
        data = [random.randint(0, 100000) for _ in range(size)]

        data_copy = data[:]
        insertion_time = timeit.timeit(lambda: insertion_sort(data_copy[:]), number=1)
        print(f"Insertion Sort: {insertion_time:.5f} seconds")

        data_copy = data[:]
        merge_time = timeit.timeit(lambda: merge_sort(data_copy[:]), number=1)
        print(f"Merge Sort: {merge_time:.5f} seconds")

        data_copy = data[:]
        timsort_time = timeit.timeit(lambda: sorted(data_copy[:]), number=1)
        print(f"Timsort (built-in): {timsort_time:.5f} seconds")

        results.append((size, insertion_time, merge_time, timsort_time))

    # Create DataFrame summary
    summary_df = pd.DataFrame(results, columns=["Array Size", "Insertion Sort (s)", "Merge Sort (s)", "Timsort (s)"])
    print("\nSummary of Execution Times:")
    print(summary_df.to_string(index=False))

if __name__ == "__main__":
    measure_sorting_algorithms()
