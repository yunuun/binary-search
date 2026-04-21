import bisect


def binary_insertion_sort(arr):
    """
    二元插入排序
    使用二分搜尋找到插入位置，減少比較次數
    時間複雜度: O(n²)（移動次數），O(n log n)（比較次數）
    空間複雜度: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        pos = bisect.bisect_left(arr, key, 0, i)
        arr[pos + 1 : i + 1] = arr[pos:i]
        arr[pos] = key
    return arr


def binary_search(arr, key, low, high):
    """手動實作二分搜尋（不使用 bisect 模組）"""
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low


def binary_insertion_sort_manual(arr):
    """使用手動實作的二分搜尋版本"""
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
        print(f"輸入: {original}")
        print(f"輸出: {result}")
        print("-" * 40)
