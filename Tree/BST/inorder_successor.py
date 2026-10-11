class Solution:
    def findPreSuc(self, root, key):
        # code here
        temp = root
        succ = None
        while temp:
            
            if temp.data > key:
                succ = temp
                temp = temp.left
                
            else:
                temp = temp.right
        
        # print(succ)
        pred = None
        temp = root
        while temp:
            
            if temp.data < key:
                pred = temp
                temp = temp.right
                
            else:
                temp = temp.left
        
        # print(pred)
        return [pred,succ]
            