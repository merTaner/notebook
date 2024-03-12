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

    # Constructor to initialize the node object
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head):
        
        prev = None
        # it store with a tuple like (val, next)
        # we access current.next on head
        current = head  
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev

        return head
                
    def recursive_reverseList(self, head):
        
        if not head:
            return None
        
        new_head = head
        if head.next:
            new_head = self.recursive_reverseList(head.next)
            head.next.next = head
        head.next = None

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