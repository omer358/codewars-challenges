def number(lines):
    for i in range(len(lines)):
        lines[i] = "{line}: {let}".format(line=i+1,let=lines[i])
    return lines


print(number(['a', 'b', 'c', 'd']))
