class BSTIterator:

    def __init__(self,root,reverse):

        self.stack = []
        self.reverse = reverse
        self.pushAll(root)

    def pushAll(self,node):

        while node:
            self.stack.append(node)
            if self.reverse:
                node = node.right
            else:
                node = node.left

    
    def next(self):

        node = self.stack.pop()
        if self.reverse:
            self.pushAll(node.left)
        else:
            self.pushAll(node.right)

        return node.data

class Solution:

    def findTarget(self, root, target):

        if root is None:
            return False
        
        before = BSTIterator(root,False)
        after = BSTIterator(root, True)

        left = before.next()
        right = after.next()

        while left < right:
            total = left + right

            if total == target:
                return True
            elif total < target:
                left = before.next()
            else:
                right = after.next()

        return False