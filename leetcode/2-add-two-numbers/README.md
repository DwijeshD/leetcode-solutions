# Add Two Numbers  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/add-two-numbers) · synced 2026-08-13

**Language:** python3
**Topics:** Linked List, Math, Recursion
**Size:** 15 lines · 449 chars

## Complexity

- **Time:** O(n) — single pass through both lists
- **Space:** O(n) — result list (plus dummy node)

## How it works

![How it works](./solution.svg)

## Solution

See [`Solution.py`](./Solution.py).

```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional
    [ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        current = dummy
        while l1 or l2 or carry: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
```
