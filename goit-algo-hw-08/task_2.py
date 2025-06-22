import heapq

def merge_k_lists(lists):
    heap = []
    result = []

    # Initialize the heap with the first element of each non-empty list
    for i, lst in enumerate(lists):
        if lst is not None and len(lst) > 0:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list index, element index)

    # Extract elements from the heap and push next elements from lists
    while heap is not None and len(heap) > 0:
        value, list_idx, elem_idx = heapq.heappop(heap)
        result.append(value)

        # If the list has more elements, push the next one to the heap
        if elem_idx + 1 < len(lists[list_idx]):
            next_value = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, list_idx, elem_idx + 1))

    return result

# Example usage:
if __name__ == "__main__":
    lists = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    merged_list = merge_k_lists(lists)
    print(f"Sorted list: {merged_list}")
