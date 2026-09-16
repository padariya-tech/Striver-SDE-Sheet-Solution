class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def mergeList(self, head1,head2):
        # Code here
        
        dummy = Node(-1)
        temp = dummy

        l1 = head1
        l2 = head2
        if l1 == None:
            return l2
        
        if l2 == None:
            return l1
        while l1 != None and l2 != None:

            if l1.data <= l2.data:
                temp.next = l1
                l1 = l1.next

            else:
                temp.next = l2
                l2 = l2.next

            temp = temp.next

        if l1 == None:
            temp.next = l2
        if l2 == None:
            temp.next = l1

        return dummy.next
        
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

    head1 = sol.createLinkedList([1])
    head2 = sol.createLinkedList([4,5,6])

    merge=sol.mergeList(head1,head2)
    sol.printList(merge)
