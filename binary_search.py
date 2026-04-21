import bisect


def binary_insertion_sort(arr):
    """
    Binary Insertion Sort
    Uses binary search to find the insertion position, reducing comparisons.
    Time complexity: O(n²) for shifting, O(n log n) for comparisons
    Space complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        # Find insertion position using binary search in the sorted portion [0, i)
        pos = bisect.bisect_left(arr, key, 0, i)
        # Shift elements to the right to make room for insertion
        arr[pos + 1 : i + 1] = arr[pos:i]
        arr[pos] = key
    return arr


def binary_search(arr, key, low, high):
    """
    Manual implementation of binary search (without using bisect module).
    Finds the leftmost position where key can be inserted to maintain sorted order.
    """
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low


def binary_insertion_sort_manual(arr):
    """
    Binary Insertion Sort using manual binary search implementation.
    Same as binary_insertion_sort, but with self-implemented binary search.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, key, 0, i)
        arr[pos + 1 : i + 1] = arr[pos:i]
        arr[pos] = key
    return arr


if __name__ == "__main__":
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1],
        [],
        [3, 3, 3, 1, 1],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
    ]

    for data in test_cases:
        original = data.copy()
        result = binary_insertion_sort(data)
        print(f"Input: {original}")
        print(f"Output: {result}")
        print("-" * 40)