def firstPlace(x):
    if not any(i=="=" for i in x):
        return "No road available"
    if not any(i.isalpha() for i in x):
        return "No car available"
    else:
        x=x.replace("=", "")
        return(x[-1])
        
print(firstPlace("aaa==aA"))