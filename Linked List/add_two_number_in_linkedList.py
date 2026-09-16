class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def reverse(self,head):
        prev = None
        
        while head:

            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev

    def addTwoLists(self, head1,head2):
        # Code here
        
        rev1 = self.reverse(head1)
        rev2 = self.reverse(head2)

        carry = 0
        l1 = rev1
        l2 = rev2
        dummy = None

        while l1 != None or l2 != None:
            summ = carry
            if l1 != None:
                summ += l1.data 
                l1 = l1.next
            if l2 != None:
                summ += l2.data
                l2 = l2.next

            new_node = Node(summ % 10)
            carry = summ // 10
            
            new_node.next = dummy
            dummy = new_node

        if carry:
            new_node = Node(carry)
            new_node.next = dummy
            dummy = new_node

        return dummy
        
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

    head1 = sol.createLinkedList([1,2,3])
    head2 = sol.createLinkedList([9,9,9])

    merge=sol.addTwoLists(head1,head2)
    sol.printList(merge)
