# The count-and-say sequence is the sequence of integers with the first five terms as following:

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            string = "1"
        for i in range(n-1):
            string = self.cArray(string)
        return string

    def cArray(self, string):
        if len(string) == 1:
            return "11"
        counter = 0
        value = ''
        res = ''
        for i, char in enumerate(string):
            if i == len(string)-1:
                if char == value:
                    counter += 1
                    res += str(counter)
                    res += char
                else:
                    res += str(counter)
                    res += value
                    res += '1'
                    res += char
            else:
                if i == 0:
                    value = char
                    counter += 1
                else:
                    if char == value:
                        counter += 1
                    else:
                        res += str(counter)
                        res += value
                        counter = 1
                        value = char
        return res
        
        