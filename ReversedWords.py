def reverse_words(s):
    words_list = s.split()
    return ' '.join(s.split()[::-1],)


print(reverse_words(" omer maki alkhalifa "))