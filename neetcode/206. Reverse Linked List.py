"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

 
Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

 

Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?



Takeaway:


"""

# Definition for singly-linked list.
class ListNode:
    # streamline memory usage
    # used for memory optimization. 
    # class is just includes defined variables.
    __slots__ = "val", "next"

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList_(self, head):
         # the list looks like 1 -> 2 -> 3
        # to make it look like 1 <- 2 <- 3
        prev = None
        current = head
        
        # while current is not None
        while current:

            next_node = current.next  # Save the next node
            current.next = prev       # Reverse the pointer
            
            # move on to the next node

            prev = current            # Move prev to the current node
            current = next_node       # Move current to the saved next node
        
        return prev
        

    def reverseList(self, head):
        # Base case for recursion: If the current head or the next node is None, 
        # it means we have reached the end of the list or the list is empty.
        if not head or not head.next:
            # Just return the current head (which will become 
            # the new tail in the reversed list).
            return head

        # Recursively call the function with the next node in the list.
        # This will reverse the sublist starting from the next node.
        new_head = self.reverseList(head.next)

        # Now, we need to reverse the pointers for the current node and the next node.
        # Make the next node's "next" pointer point back to the current node.
        head.next.next = head
        # Set the current node's "next" pointer to None to break the original link.
        head.next = None

        # Finally, return the new_head, which is the head of the reversed list.
        return new_head


if __name__ == '__main__':
    sol = Solution()
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    solution = Solution()
    reversed_head = solution.reverseList(head)
    
    # new head after reversal
    current = reversed_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print()