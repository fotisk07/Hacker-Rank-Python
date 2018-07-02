import calendar
def day(y,m,d):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y -= m<3
    c= (y + y//4 - y//100 + y//400 + t[m-1] + d-1) % 7
    if c == 0:
        print("MONDAY")
    elif c == 1:
        print("TUESDAY")
    elif c == 2:
        print("WEDNESDAY")
    elif c==3:
        print("THURSDAY")
    elif c==4:
        print("FRIDAY")
    elif c== 5:
        print("SATURDAY")
    elif c==6:
        print("SUNDAY")


if __name__ == "__main__":
    date = input()
    list_date = date.split()
    list_date=[int(x) for x in list_date]
    day(list_date[2],list_date[0],list_date[1])
    
