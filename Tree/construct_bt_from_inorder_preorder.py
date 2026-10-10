class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def build(self,prestart,preend,instart,inend,in_map):

        if prestart > preend and instart > inend:
            return None

        pre_element = preorder[prestart]
        node = TreeNode(pre_element)

        find_in_map = in_map[pre_element]

        leftElement = find_in_map - instart

        node.left = self.build(prestart,prestart+leftElement,instart,find_in_map-1)
        node.right = self.build(prestart+leftElement+1,preend,find_in_map+1,inend,in_map)

        return node

    def ConstructTree(self,inorder,preorder):
        
        in_map = {}
        for i in range(len(inorder)):
            in_map[inorder[i]]=i

        prestart = 0
        preend = len(preorder) - 1
        instart = 0
        inend = len(inorder) - 1
        root = self.build(prestart,preend,instart,inend,in_map)

        return root


if __name__== "__main__":

    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    sol = Solution()
    root = sol.ConstructTree(inorder,preorder)
    print(root)


    