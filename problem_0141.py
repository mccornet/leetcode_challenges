# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Floyd's algorithm.
        
        Using fast and slow pointers.
        
        If fast and slow pointers meet there is proof of a loop.
        If the fast pointer finds a None we exit our loop
        """
        
        slow = fast = head

        # Exit the search when:
        # 1. fast is None due to either
        # - Empty input
        # - fast.next.next was None
        # 2. fast.next is None 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            # Floyd's algorithm: if they meet there is a loop
            if fast == slow:
                return True
        
        # If fast found an end to the list there is no loop
        return False

    """
    However, it is more pythonic to assume there 
    is a valid entry and use a try / except block
    """
    def hasCycle(self, head: ListNode) -> bool:

        # initialize the pointers
        slow = fast = head 

        try:
            while True:
                slow = slow.next
                fast = fast.next.next
                
                if slow == fast:
                    # proving the cycle
                    return True
        except:
            # .next was None and calling 
            # .next on None threw the exception
            return False