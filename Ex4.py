def days (x, y):
    if x in [1, 3, 5, 7, 8, 10, 12]:
        return "31"
    elif x in [4, 6, 9, 11]:
        return "30"
    elif x==2:
        if y%4==0 and y%100!=0:
            return "29"
        else:
            return "28"
    

print(days(2, 2016))