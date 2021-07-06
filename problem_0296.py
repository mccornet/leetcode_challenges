# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        To reverse in place is it needed to keep track of
        The pointer that a node came from.
    
        1.  At first the previous will be None
            Since the start of the list should become the end and pointing to None
        
        2.  As long as we have a head node we make it point backwards to previous
            But we have to remember what it used to point to so it is possible
            To use that in next iterations

        example: (1, 2) -> (2, None)

        Iteration 1:
            prev = None
            head = (1, 2)
            next = None

            1. Find out next
            next = (2, None)
            
            2. Make the head point backwards
            head.next = prev (None)
            head = (1, None)

            3.  swap previous with head
                Note: previous becomes the head!
            prev = head (1, None)

            4. Set the head equal to the next node (2)
            head = (2, None)

        Iteration 2:
            prev = (1, None)
            head = (2, None)

            1. find out next
            Next = None

            2. Make the head point backwards
            head.next = prev
            head = (2, 1)

            3. swap places with previous
            prev = head = (2, 1)

            4. Make head the next_node
            head = next (None)

        This terminates the loop in the next iteration
        with the current data structure

        prev = (2, 1) -> (1, None)

        return prev as this has become the next head
        """
        prev = None
        next_node = None

        while head:
            next_node = head.next   # Store the next node before we alter in place
            head.next = prev        # Make the current head point backwards
            prev = head             # The previous node will swap places with head
            head = next_node        # And the head can now be moved forward to the next node
        
        return prev                 # After reversing in place previous will have move forward to the last node