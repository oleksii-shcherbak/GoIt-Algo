def merge_two_lists(left, right):
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_k_lists(lists):
    """Merge k sorted lists into one sorted list using divide and conquer."""
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            list1 = lists[i]
            list2 = lists[i + 1] if i + 1 < len(lists) else []
            merged = merge_two_lists(list1, list2)
            merged_lists.append(merged)

        lists = merged_lists

    return lists[0]


# Example usage
if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Sorted list:", merged_list)
