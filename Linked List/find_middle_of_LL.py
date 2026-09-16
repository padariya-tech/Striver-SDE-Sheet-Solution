class Node:
    def __init__(self,data):

        self.data = data
        self.next = None

class Solution:
    def find_middle_of_LL(self,head):
        slow = head
        fast = head

        while fast != None and fast.next != None:
            # print(fast.data,slow.data)
            fast = fast.next.next
            slow = slow.next

        return slow.data


if __name__=="__main__":

    head = Node(1)

    head.next = Node(2)
    # head.next.next = Node(3)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)


    sol = Solution()
    ans = sol.find_middle_of_LL(head)
    print(ans)