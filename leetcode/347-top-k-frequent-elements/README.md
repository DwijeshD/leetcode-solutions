# Top K Frequent Elements  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/top-k-frequent-elements) · synced 2026-08-13

**Language:** python3
**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect
**Size:** 15 lines · 419 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_sets = {}
        for num in nums:
            if num in num_sets:
                num_sets[num] += 1
            else:
                num_sets[num] = 1
        
        sorted_items = sorted(num_sets.items(), key=lambda x: x
        [1], reverse=True)
        top_k = [x[0] for x in sorted_items[:k]]

        return top_k
```
