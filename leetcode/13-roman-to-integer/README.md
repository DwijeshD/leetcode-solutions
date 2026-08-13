# Roman to Integer  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/roman-to-integer) · synced 2026-08-13

**Language:** python3
**Topics:** Hash Table, Math, String
**Size:** 14 lines · 254 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0

```
