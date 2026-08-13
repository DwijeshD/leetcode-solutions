# Palindrome Number  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/palindrome-number) · synced 2026-08-13

**Language:** python3
**Topics:** Math
**Size:** 15 lines · 285 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

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
