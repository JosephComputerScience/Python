"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashm = {}
        if head is None:
            return False
        while head.next is not None:
            if head.val == 'true':
                return True
            elif head.val is not True:
                head.val = 'true'
            head = head.next
            
        return False