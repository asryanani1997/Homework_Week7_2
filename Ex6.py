def absolute_added (x): 
    words=x.split()
    for i in range(len(words)):
        if words[i]=="a":
            words[i]="an absolute"
        elif words[i]=="A":
            words[i]="An absolute"
    return " ".join(words)
print(absolute_added("A man with no haters."))