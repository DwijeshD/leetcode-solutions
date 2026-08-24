# Search in Rotated Sorted Array  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/search-in-rotated-sorted-array) · synced 2026-08-24

**Language:** python3
**Topics:** Array, Binary Search
**Size:** 15 lines · 375 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        rot = bisect_left(nums, True, key=lambda n: n <= nums[-1])
        
        lo, hi = 0, n - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + rot) % n

            if nums[real] == target:
                return real
                
```
