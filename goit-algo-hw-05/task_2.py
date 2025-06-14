def binary_search_upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    upper_bound = None
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] >= target:
            upper_bound = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return iterations, upper_bound


# Example usage
if __name__ == "__main__":
    array = [0.1, 1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.0]
    target = 3.0
    result = binary_search_upper_bound(array, target)
    print(f"Iterations: {result[0]}, Upper Bound: {result[1]}")
