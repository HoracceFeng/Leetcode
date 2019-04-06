# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
            

        ''' brute method, not work
        res = ListNode(None)
        stop = False
        while not stop:
            if l1 is None:
                if l2 is not None:
                    if res.val is not None:
                        res.next = ListNode(l2.val)
                    else:
                        res.val = l2.val
                    l2 = l2.next
                else:
                    stop = True
            else:
                if l2 is None:
                    if res.val is not None:
                        res.next = ListNode(l1.val)
                    else:
                        res.val = l1.val
                    l1 = l1.next
                else:
                    if l1.val <= l2.val:
                        if res.val is not None:
                            res.next = ListNode(l1.val)
                        else:
                            res.val = l1.val
                        l1 = l1.next
                    else:
                        if res.val is not None:
                            res.next = ListNode(l2.val)
                        else:
                            res.val = l2.val
                        l2 = l2.next
        return res
        '''
               
                
                
                
                
                