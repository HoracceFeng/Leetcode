# Given a linked list, remove the n-th node from the end of list and return its head.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/42/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        ## use `previous` is for avoiding to use node.next.next
        tail = head
        previous = head
        prior = head
        i = 1
        
        ## read first in order to catch the end
        while i < n and tail.next:
            tail = tail.next
            i += 1
        
        ## get the `nth distance` before the end
        while tail.next:
            prior = previous
            previous = previous.next
            tail = tail.next
            
        ## process remove and avoid Erros
        if head is previous:
            head = previous.next
        else:
            prior.next = previous.next
        return head  

        
# Could you do this in one pass?

        
            
        

            