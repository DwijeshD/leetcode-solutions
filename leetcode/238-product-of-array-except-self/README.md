# Product of Array Except Self  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/product-of-array-except-self) · synced 2026-08-13

**Language:** python3
**Topics:** Array, Prefix Sum
**Size:** 14 lines · 398 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        left_total = 1
        right_total = 1

        for i in range(len(nums)):
            answer.append(left_total)
            left_total = left_total * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * right_total
            right_total *= nums[i]

```
