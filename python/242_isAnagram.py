# Given two strings s and t , write a function to determine if t is an anagram of s.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/35/

## definition of 'anagram': same length, same chars but different words

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
# solution-1: The Best
        if len(s) != len(t):
            return False

        s = sorted(s)
        t = sorted(t)
        
        for index in range(len(s)):
            if s[index] != t[index]:
                return False
        
        return True
        
## solution-2:
#         if len(s) != len(t):
#             return False

#         t = list(t)
#         for char in s:
#             try:
#                 index = t.index(char)
#             except:
#                 return False   
#             if index == -1:
#                 return False
#             else:
#                 del t[index]
                
#         return True
        
#         ## min Edit Distance
#         len_s, len_t = len(s)+1, len(t)+1
#         matrix = [ [0]*len_t for i in range(len_s)]
#         cost = 0
        
#         for i in range(1, len_s):
#             matrix[i][0] = matrix[i-1][0] + 1
#         for j in range(1, len_t):
#             matrix[0][j] = matrix[0][j-1] + 1
            
#         for i in range(1, len_s):
#             for j in range(1, len_t):
#                 if s[i-1] == t[i-1]:
#                     cost = 0
#                 else:
#                     cost = 1
#             ## either insert, or replace, or delete
#             matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+cost)
            

        