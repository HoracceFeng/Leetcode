# Reverse a singly linked list. --> A linked list can be reversed either iteratively or recursively. Could you implement both?
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/43/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
## solution-4 : iteration
        if head == None:
            return head
        end = None
        while head:
            temp = head
            head = temp.next
            temp.next = end
            end = temp
        return temp
            

# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
# ## resoultion-3: recursive-2 storage big
#         def recursive(p, prev=None):
#             if p == None:
#                 return prev
#             node = p.next     # <--- consume too much storage
#             p.next = prev
#             return recursive(node, p)
#         return recursive(head)
        
        
    
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
# ## resoultion-2: recursive-1 Best-1
#         self.newhead = None
#         self.reverse(head)
#         return self.newhead
    
#     def reverse(self, head):
#         if head == None:
#             return None
#         if head.next == None:
#             self.newhead = head
#             return head
#         tail = self.reverse(head.next)
#         tail.next = head
#         head.next = None
#         return head
        
        
        
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """        
# ## solution-1: Python 多元赋值时右侧的变量暂时不会变化
#         p, rev = head, None
#         while p:
#             rev, rev.next, p = p, rev, p.next
#         return rev
        
#         ## 思路与这个相当，但是这个超时了
# #         previous = head
# #         now = head
        
# #         while now.next:
# #             now = now.next
# #             now.next = previous
# #             previous = now

# #         head.next = None
# #         return now
            