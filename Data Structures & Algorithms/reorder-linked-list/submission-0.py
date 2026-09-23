# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = []
        curr = head
        #length = [2,4,6,8]
        
        while curr:
            length.append(curr)
            print(length[len(length)-1].val)
            curr = curr.next
        l = 0
        r = len(length)-1
        while l < r:
            length[l].next = length[r]
            l += 1
            if l == r:
                break
            length[r].next = length[l]
            r -= 1

        length[l].next = None
