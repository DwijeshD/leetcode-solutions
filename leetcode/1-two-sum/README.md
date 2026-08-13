# Two Sum  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/two-sum) · synced 2026-08-13

**Language:** python3
**Topics:** Array, Hash Table
**Size:** 12 lines · 303 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i
                    
        
```
