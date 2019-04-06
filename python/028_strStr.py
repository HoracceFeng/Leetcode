# Implement strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ## KMP algorithm: https://www.cnblogs.com/yjiyjige/p/3263858.html
        ##                https://blog.csdn.net/starstar1992/article/details/54913261/

## solution-1: brute force        
        hlen = len(haystack)
        nlen = len(needle)
        
        if nlen == 0:
            return 0
        if hlen == 0 or hlen < nlen:
            return -1
        
        for i in range(hlen-nlen+1):
            if haystack[i] != needle[0]:
                continue
            else:
                if haystack[i:i+nlen] == needle:
                    return i
        
        return -1
