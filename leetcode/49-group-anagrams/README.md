# Group Anagrams  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/group-anagrams) · synced 2026-09-27

**Language:** python3
**Topics:** Array, Hash Table, String, Sorting
**Size:** 3 lines · 89 chars
**Revisions:** 2

## Performance

| Metric | Value | Beats |
| --- | --- | --- |
| Runtime | 11 ms | 82.83% |
| Memory | 21.67 MB | 97.78% |

## Complexity

- **Time:** O(n · k log k) — k = max string length, for the sort key
- **Space:** O(n · k) — grouped strings stored in the map

## How it works

![How it works](./solution.svg)

## Solution

See [`Solution.py`](./Solution.py).

```python
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
```
