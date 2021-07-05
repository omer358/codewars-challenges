"""
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""


def find_short(s):
    string_list = s.split()
    print(string_list)
    return min(string_list, key=len)


print(find_short("bitcoin take over the world maybe who knows perhaps"))
