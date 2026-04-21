# Binary Search & Binary Insertion Sort

二元搜尋與二元插入排序的 Python 實作。

## 演算法說明

### 二元搜尋（Binary Search）
在已排序陣列中，以折半搜尋的方式快速找到目標值的位置。

- 時間複雜度：O(log n)
- 空間複雜度：O(1)

### 二元插入排序（Binary Insertion Sort）
改良自傳統插入排序，用二分搜尋取代線性搜尋來找插入位置。

- 時間複雜度：O(n log n)（比較次數），O(n²)（移動次數）
- 空間複雜度：O(1)
- 穩定排序：✅

## 使用方式

```python
from binary_search import binary_insertion_sort, binary_insertion_sort_manual

arr = [64, 34, 25, 12, 22, 11, 90]
result = binary_insertion_sort(arr)
print(result)  # [11, 12, 22, 25, 34, 64, 90]
```

## 執行測試

```bash
python binary_search.py
```

## 測試案例

| 輸入 | 輸出 |
|------|------|
| `[64, 34, 25, 12, 22, 11, 90]` | `[11, 12, 22, 25, 34, 64, 90]` |
| `[5, 4, 3, 2, 1]` | `[1, 2, 3, 4, 5]` |
| `[3, 3, 3, 1, 1]` | `[1, 1, 3, 3, 3]` |
| `[1, 2, 3, 4, 5]` | `[1, 2, 3, 4, 5]` |
