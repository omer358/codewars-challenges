def find_short(s):
    string_list = s.split()
    print(string_list)
    return min(string_list, key=len)


print(find_short("bitcoin take over the world maybe who knows perhaps"))
