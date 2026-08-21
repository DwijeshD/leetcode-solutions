# Longest Common Prefix  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/longest-common-prefix) · synced 2026-08-21

**Language:** python3
**Topics:** Array, String, Trie
**Size:** 12 lines · 310 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
```
