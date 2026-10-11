''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def largestBst(self, root: 'Node') -> int:
        # Your code here
        def solve(node):
            
            if node is None:
                return float('inf'),float('-inf'),0
                
            left_min,left_max,left_size = solve(node.left)
            right_min,right_max,right_size = solve(node.right)
            
            if left_max < node.data < right_min:
                return (
                    min(node.data,left_min),
                    max(node.data,right_max),
                    left_size+right_size+1
                    )
                    
            return (
                float('-inf'),
                float('inf'),
                max(left_size,right_size)
            )
                
        return solve(root)[2]
        