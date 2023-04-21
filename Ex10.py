def missingNum (x):
    overall_sum= 10*(10+1)/2
    current_sum=0
    for i in x:
        current_sum+=i
    return overall_sum-current_sum

print(missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]))