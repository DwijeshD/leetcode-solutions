# Subarray Sum Equals K  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/subarray-sum-equals-k) · synced 2026-08-20

**Language:** python3
**Topics:** Array, Hash Table, Prefix Sum
**Size:** 11 lines · 249 chars
**Revisions:** 2

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

        for i in range(len(nums)):
            prefix += nums[i]
            needed = prefix - k
            if needed in map:
                counter += map[needed]
            map[prefix] = map.get(prefix, 0) + 1

        return counter

        
```
