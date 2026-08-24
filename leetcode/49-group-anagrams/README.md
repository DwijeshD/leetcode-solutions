# Group Anagrams  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/group-anagrams) · synced 2026-08-24

**Language:** python3
**Topics:** Array, Hash Table, String, Sorting
**Size:** 15 lines · 359 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}

        for i in range(len(strs)):
            word = strs[i]
            key = "".join(sorted(word))

            if key in keys:
                keys[key].append(word)
            else:
                keys[key] = [word]

        return list(keys.values())
```
