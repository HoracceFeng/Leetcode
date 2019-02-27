# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/32/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        s[:] = [s[len(s)-1-i] for i in range(len(s))]