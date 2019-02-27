# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/6/linked-list/41/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        ## cannot search previous node, so we only can replace post-nodes recursively.
        current = node
        post = node.next
        if post != None:
            current.val = post.val
            current.next = post.next
        else:
            return post
        