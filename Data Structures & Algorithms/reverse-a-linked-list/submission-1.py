# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        dummy = head
        
        if head == None:
            return head
        

        while curr:
            dummy = curr
            curr = curr.next
            dummy.next = prev
            prev = dummy
            
        #curr.next = dummy
        #print("curr is at" + str(dummy.val))
        #print("curr points to" + str(dummy.next.val))
        return dummy
