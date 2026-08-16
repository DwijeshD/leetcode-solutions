# Binary Tree Level Order Traversal  ·  Medium

> Leetcode · [Open problem](https://leetcode.com/problems/binary-tree-level-order-traversal) · synced 2026-08-16

**Language:** python3
**Topics:** Tree, Breadth-First Search, Binary Tree
**Size:** 16 lines · 423 chars
**Revisions:** 4

## Complexity

- **Time:** O(n) — each node is visited once in the queue
- **Space:** O(m) — queue holds at most the number of nodes on one level (≤ n)

## How it works

![How it works](./solution.svg)

## Solution

See [`Solution.py`](./Solution.py).

```python

        queue = deque([])
        queue.append(root)

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
```
