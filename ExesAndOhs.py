"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:
    XO("ooxx") => true
    XO("xooxx") => false
    XO("ooxXm") => true
    XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
    XO("zzoo") => false
"""


def xo(s):
    s_upper = s.lower()
    if s_upper.count('x') == s_upper.count('o'):
        return True
    else:
        return False


print(xo("xoxoxoxoxxxooxoo"))