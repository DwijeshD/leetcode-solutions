# Koko Eating Bananas  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/koko-eating-bananas) · synced 2026-08-24

**Language:** python3
**Topics:** Array, Binary Search
**Size:** 15 lines · 319 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        lo = 1
        hi = max(piles)
        answer = hi


        while lo <= hi:
            mid = (lo + hi) // 2
            hours = 0
            
            for j in range(len(piles)):
                hours += ceil(piles[j] / mid)
```
