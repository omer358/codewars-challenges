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
