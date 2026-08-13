# Palindrome Number  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/palindrome-number) · synced 2026-08-13

**Language:** python3
**Topics:** Math
**Size:** 15 lines · 285 chars

## Complexity

- **Time:** O(n) — each digit is compared at most once
- **Space:** O(n) — integer is converted to a string of length n

## How it works

![How it works](./solution.svg)

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if (x<0):
            return False

        num = str(x)
        left, right = 0, len(num) - 1

        while left < right:
            if num[left] != num[right]:
                return False

            left += 1
```
