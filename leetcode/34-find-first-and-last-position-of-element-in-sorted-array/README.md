# Find First and Last Position of Element in Sorted Array  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array) · synced 2026-08-13

**Language:** python3
**Topics:** Array, Binary Search
**Size:** 15 lines · 298 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List
    [int]:

        lo, hi = (0, len(nums) - 1)
        ans_left = -1
        ans_right = -1


        while lo <= hi:
            mid = (hi + lo) // 2                

            
            if nums[mid] >= target:
```
