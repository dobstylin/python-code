
def dates(d,m,y):
    max_year = 2100
    min_year = 2000
    if y < min_year or y > max_year:
        return False
    if m < 1 or m > 12:
        return False
    if d < 1 or d > 31:
        return False
    if m == 2:
        return d <= 28
    if m ==4 or m == 6 or m == 9 or m == 1:
        return d <=30
    return True

def printDates(y1, y2):
    for year in range(y1, y2+1, 1):
        str1 = str(year)
        rev = str1
        rev = rev[::-1]
        day = int(rev[0:2])
        month = int(rev[2:4])
        rev += str1
        if (dates(day,month,year)):
            print('{}/{}/{}'.format(rev[0:2], rev[2:4], rev[4:]))

if __name__ == '__main__':
    y1 = 2000
    y2 = 2100
    printDates(y1,y2)
