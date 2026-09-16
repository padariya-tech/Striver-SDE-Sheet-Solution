class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def removeNode(self, head,n):

        k = n 
        
        slow,fast = head,head

        while k > 0:
            fast = fast.next
            k -= 1

        if fast == None:
            return head.next


        while fast.next != None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
        

        

        
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

    head1 = sol.createLinkedList([1,2,3,4,5,6,7,8])
    n = 8
    merge=sol.removeNode(head1,n)
    sol.printList(merge)
