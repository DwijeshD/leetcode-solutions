# Binary Tree Level Order Traversal  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/binary-tree-level-order-traversal) · synced 2026-08-16

**Language:** python3
**Topics:** Tree, Breadth-First Search, Binary Tree
**Size:** 15 lines · 425 chars
**Revisions:** 3

## Complexity

- **Time:** O(n) — each node is dequeued and processed exactly once
- **Space:** O(n) — the queue may hold up to all nodes in the worst case

## How it works

![How it works](./solution.svg)

## Solution

See [`Solution.py`](./Solution.py).

```python

        result = []

        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

```
