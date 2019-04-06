# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character,takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned.
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

## solution-1
        ## find the first string 
        _s = str.split()
        _res = ''
        if len(_s) != 0 :
            string = _s[0]
        else:
            return 0
        
        ## posititve or negative --> acutally int() can do it directly
        if string[0] == '-':
            _sign = False
            string = string[1:]
        elif string[0] == '+':
            _sign = True
            string = string[1:]
        elif not string[0].isdigit():
            return 0
        else:
            _sign = True
        
        ## get the digit
        for char in string:
            if char.isdigit():
                _res += char
            else:
                break
        
        ## print output
        if _res != '':
            res = int(_res)
            if not _sign:
                res = 0-res
        else:
            return 0

        ## check boundary 
        if res < -2**31:
            return -2**31
        elif res > 2**31-1:
            return 2**31-1
        else:
            return res