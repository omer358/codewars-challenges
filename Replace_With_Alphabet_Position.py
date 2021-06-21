def alphabet_position(text):
    positions = ''
    letters = list('abcdefghijklmnopqrstuvwxyz')
    for i in text:
        if i.isalpha():
            positions += str(letters.index(i.lower()) + 1) + ' '
    print(positions)
    return positions[0:len(positions)-1]


print(alphabet_position("The sunset sets at twelve o' clock."))
