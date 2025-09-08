# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # iterate to halfway point for slow
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list
        second = slow.next
        prev = slow.next = None
        while second:
            # we want to essentially flip the links from ... 4 -> 5 -> None to 5 -> 4 -> None
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # interleave both halves
        # we loop through setting second to the start of the reversed list
        # e.g. 1, 2, 3, 4, 5, None -> becomes "prev": 5 -> 4 -> None
        # head: 1 -> 2 -> 3
        first, second = head, prev
        while second:
            # here we then get what our next nodes should be since we are replacing the links
            tmp1, tmp2 = first.next, second.next
            # set to the current second node
            first.next = second
            # set to what should follow, naturally
            second.next = tmp1
            # then updating positions
            first, second = tmp1, tmp2