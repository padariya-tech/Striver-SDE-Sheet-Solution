class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    ''' Merge the two linked lists in a particular
     order based on the data value '''
    def merge(self, list1, list2):
        ''' Create a dummy node as a 
        placeholder for the result '''
        dummyNode = ListNode(-1)
        res = dummyNode

        # Merge the lists based on data values
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            res.next = None

        # Connect the remaining elements if any
        if list1:
            res.child = list1
        else:
            res.child = list2

        # Break the last node's link to prevent cycles
        if dummyNode.child:
            dummyNode.child.next = None

        return dummyNode.child

    # Function to flatten a linked list with child pointers 
    def flattenLinkedList(self, head):
        # If head is null or there is no next node
        if head is None or head.next is None:
            return head # Return head

        # Recursively flatten the rest of the linked list
        mergedHead = self.flattenLinkedList(head.next)

        # Merge the lists
        head = self.merge(head, mergedHead)
        return head

# Function to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()

# Function to print the linked list in a grid-like structure
def printOriginalLinkedList(head, depth):
    while head is not None:
        print(head.val, end="")

        ''' If child exists, recursively
         print it with indentation '''
        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        # Add vertical bars for each level in the grid
        if head.next:
            print()
            for i in range(depth):
                print("| ", end="")
        
        head = head.next

if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    # Print the original linked list structure
    print("Original linked list:")
    printOriginalLinkedList(head, 0)

    # Creating an instance of Solution class
    sol = Solution()
    
    # Function call to flatten the linked list
    flattened = sol.flattenLinkedList(head)
    
    # Printing the flattened linked list
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)