# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        depth = 0
        
        queue = []
        
        queue.append(root)
        
        while(queue):
                       
            size = len(queue)

            while(size > 0):
                
                root = queue.pop(0)
                
                if root.left != None:
                    queue.append(root.left)
                    
                if root.right != None:
                    queue.append(root.right)
                
                size -= 1
            
            depth += 1
    
        return depth