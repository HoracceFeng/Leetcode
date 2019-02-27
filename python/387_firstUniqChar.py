# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/34/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
## solution-1: 404ms
#         if len(s)<=0:
#             return -1
#         elif len(s)==1:
#             return 0
        
#         d = dict()
#         res = None
#         for index, char in enumerate(s):
#             if char not in d.keys():
#                 d[char] = [1, index]
#             else:
#                 d[char][0] += 1
                
#         count = len(s)
#         noflag = True
#         for i in d.keys():
#             if d[i][0] != 1:
#                 continue
#             else:
#                 if d[i][1] < count:
#                     count = d[i][1]
#                     noflag = False
                    
#         if noflag:
#             return -1
#         else:
#             return count
   
## solution-2: 200ms
        if len(s)<=0:
            return -1
        elif len(s)==1:
            return 0
        
        d = {'0':[], 'all':[]}
        for i in s:
            if i not in d['all']:
                d['0'].append(i)
                d['all'].append(i)
            else:
                if i in d['0']:
                    del d['0'][d['0'].index(i)]
        
        if len(d['0']) == 0:
            return -1
        else:
            return s.index(d['0'][0])

        
        