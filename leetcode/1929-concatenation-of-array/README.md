# Concatenation of Array  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/concatenation-of-array) · synced 2026-08-13

**Language:** python3
**Topics:** Array, Simulation
**Size:** 6 lines · 140 chars
**Revisions:** 5

## Complexity

- **Time:** O(n) — one pass concatenates the two arrays
- **Space:** O(n) — creates a new list of length 2n

## How it works

![How it works](./solution.svg)

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newlist = nums + nums
        return newlist
        
```
