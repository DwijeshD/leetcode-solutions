# Binary Search  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/binary-search) · synced 2026-08-13

**Language:** python3
**Topics:** Array, Binary Search
**Size:** 15 lines · 378 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        lo = 0
        hi = len(nums) -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
```
