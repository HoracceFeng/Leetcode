# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/36/


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
## solution-1: OOM
        # string = ''
        # for char in s:
        #     if char.isalnum():
        #         string += char.lower()
        # if len(string) == 0 or len(string) == 1:
        #     return True
        
        # max_id = len(string)-1
        # for i in range(max_id//2+1):
        #     if string[i] != string[max_id-i]:
        #         return False
        
        # return True
        
## solution-2
## solution-2
        if len(s) == 0 or len(s) == 1 or len(list(set(s).intersection(set(string.digits+string.ascii_letters)))) == 0:
            return True
        
        head_id = 0
        tail_id = len(s)-1
        
        while head_id < tail_id:
            while not s[head_id].isalnum():
                head_id += 1
            while not s[tail_id].isalnum():
                tail_id -= 1
            if s[head_id].lower() != s[tail_id].lower():
                return False
            head_id += 1
            tail_id -= 1
            
        return True
            

## solution-3: The Best --> str only can be used in python3
        # s = ''.join(filter(str.isalnum,s)).lower()
        # return s==s[::-1]

## solution-4: using regulation expression. r'' for regulation expression, ^ means `except`. re.sub() for replacement
        if not s:
            return True
        else:
            return re.sub(r'[^a-zA-Z0-9]', r'', s).lower() == re.sub(r'[^a-zA-Z0-9]', r'', s).lower()[::-1]
