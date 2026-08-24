# Subarray Sum Equals K  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/subarray-sum-equals-k) · synced 2026-08-24

**Language:** python3
**Topics:** Array, Hash Table, Prefix Sum
**Size:** 15 lines · 375 chars
**Revisions:** 3

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        prefix = 0
        counter = 0

        for i in range(len(nums)):
            prefix += nums[i]
            needed = prefix - k
            if needed in map:
                counter += map[needed]
            map[prefix] = map.get(prefix, 0) + 1

        return counter
```
