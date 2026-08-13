# Reorder List  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/reorder-list) · synced 2026-08-13

**Language:** python3
**Topics:** Linked List, Two Pointers, Stack, Recursion
**Size:** 15 lines · 403 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find middle (slow/fast)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split into two halves
        second = slow.next
        slow.next = None  # break list
```
