# Container With Most Water  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/container-with-most-water) · synced 2026-08-13

**Language:** python3
**Topics:** Array, Two Pointers, Greedy
**Size:** 15 lines · 346 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:

            area = (right-left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
```
