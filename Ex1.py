def countTrue(x):
    Quantity=0
    for i in x: 
        if i==True:
            Quantity+=1
    return Quantity

print(countTrue([True, False, False, True, False]))