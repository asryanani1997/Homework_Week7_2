def censor (x):
    words=x.split()
    for i in range(len(words)):
        if len(words[i])>4:
            words[i]="*"*len(words[i])

    return" ".join(words)

print(censor("Two plus three is five"))