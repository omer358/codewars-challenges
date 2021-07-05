"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""


def vowel(str):
    v = ['a', 'e', 'o', 'i', 'u', 'A', 'O', 'U', 'I', 'E']
    l = list(str)
    print(l)
    for i in str:
        if i in v:
            l.remove(i)
    return ''.join(l)


str = 'here in the ashes your soul cries Out'
print(vowel(str))
