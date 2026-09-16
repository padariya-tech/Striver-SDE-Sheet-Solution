class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def reverseList(self, head):
        # Code here
        
        prev = None
        ans = head
        while head:
            nxt = head.next

            head.next = prev
            prev = head
            head = nxt

        return prev
        
    def printList(self,head):

        ans = head
        while head:
            print(head.data)
            head = head.next

if __name__ == "__main__":

    head = Node(1)

    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

   

    sol = Solution()
    print("original Linked List")
    sol.printList(head)
    ans = sol.reverseList(head)

    print("Reversed Linked List")
    sol.printList(ans)
