class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def delete(self, head1,node):
        # Code here
        node.data = node.next.data
        node.next = node.next.next


        return head1
    
    def findNode(self, head, value):
        while head:
            if head.data == value:
                return head
            head = head.next

        return None
    
    def printList(self,head):

        ans = head
        while head:
            print(head.data,end=" -> ")
            head = head.next
        print("None")

    def createLinkedList(self,arr):
        n = len(arr)
        head = Node(arr[0])
        temp = head
        for i in range(1,n):
            new_node = Node(arr[i])
            temp.next = new_node
            temp = temp.next

        return head

    

if __name__ == "__main__":

    sol = Solution()

    head1 = sol.createLinkedList([4,5,1,9])
    val = 5
    node = sol.findNode(head1,val)

    merge=sol.delete(head1,node)
    sol.printList(merge)
