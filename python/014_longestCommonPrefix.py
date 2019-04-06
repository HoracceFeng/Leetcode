# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ## solution-1: direct search algorithms 
        if len(strs) == 0:
            return ''
        strlist = [ list(string) for string in strs ]
        aligns = zip(*strlist)
        res = ''
        
        ## three methods to search after using zip():
        ## 1. direct search, like below
        ## 2. binary search, /2 time
        ## 3. using sets, to check len(sets(align))
        
        if len(aligns) != 0:
            for align in aligns:
                align = sorted(align)
                if align[0] == align[-1]:
                    res += align[0]
                    continue
                else:
                    break
        return res


        ## solution-2: using ASCII code character
        res = ''
        if not strs:
            return res
        minstr = min(strs)
        maxstr = max(strs)
        for i in range(min(len(minstr), len(maxstr))):
            if minstr[i] == maxstr[i]:
                res += minstr[i]
            else:
                break
        return res

