def multiplyNums (x):
    separate_numbers=x. split(", ") 
    final=1
    for i in separate_numbers:
        final*=int(i)
    return final

print(multiplyNums("10, -2"))
