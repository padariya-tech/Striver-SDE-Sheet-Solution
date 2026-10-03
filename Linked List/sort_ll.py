class Solution:
    def sortList(self, head):
        # Base case
        if head is None or head.next is None:
            return head

        # Find middle of the linked list
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split into two halves
        right = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(right)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, list1, list2):
        dummy = ListNode(0)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        # Attach remaining nodes
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next