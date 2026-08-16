
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List
    [int]]:
        if not root:
            return []
        
        queue = deque([])
        queue.append(root)

        result = []

        while queue:
            level = []
            level_size = len(queue)