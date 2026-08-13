# Linked List Cycle  ·  Easy

> Leetcode · [Open problem](https://leetcode.com/problems/linked-list-cycle) · synced 2026-08-13

**Language:** python3
**Topics:** Hash Table, Linked List, Two Pointers, Floyd's Cycle Finding Algorithm
**Size:** 15 lines · 350 chars

## Complexity

- **Time:** _not analyzed yet_
- **Space:** _not analyzed yet_

## Solution

See [`Solution.py`](./Solution.py).

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:   

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
```
