# Given a 32-bit signed integer, reverse digits of an integer.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/33/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2**31-1 or x < -2**31:
            return 0
        
        _list = list(str(x))
        negative = 0
        if _list[0] == '-':
            negative = 1
            _list = _list[1:]
        _list[:] = [ _list[len(_list)-1-i] for i in range(len(_list)) ]
        
        res = ''
        for i in range(len(_list)):
            res += _list[i]
        
        res = int(res)
        if negative:
            res = 0-res

        if res > 2**31-1 or res < -2**31:
            return 0
        
        return res