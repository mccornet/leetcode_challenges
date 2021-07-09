# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    See problem 82 for a more difficult version

    This is a fast and slow pointer problem.


    Step 1. if current node exists and the next node exists 
            check if the value is the same

    Step 2. - Option 1: same value 
              -> skip the node with head.next.next (the fast pointer)
            - Option 2: different value
              -> move to the next node (the slow pointer)
        
    Step 3. Store a pointer to the head since we modify this in place

            NB: While this can be done with start = head in this particular problem
            It is more common to place a node before the head and return start.next

    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        start = ListNode(0, head)

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return start.next   