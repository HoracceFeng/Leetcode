# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/27/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # num = 0
        # digits.reverse()
        # for index, i in enumerate(digits):
        #     num += i*10**index
        # num+=1
        num = ''
        res = []
        for i in digits:
            num += str(i)
        for j in str(int(num)+1):
            res.append(int(j))
        return res
        
        