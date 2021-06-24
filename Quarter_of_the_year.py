def quarter_of(month):
        if month < 4:
            return 1
        elif 3 < month < 7:
            return 2
        elif 6 < month < 10:
            return 3
        elif 9 < month <= 12:
            return 4


print(quarter_of(12))
