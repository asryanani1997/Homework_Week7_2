def intWithinBounds (x,y,z):
    if type(x)==int and type(y)==int and type(z)==int and y<=x<z:
        return True
    else:
        return False

print(intWithinBounds(3, 1.5, 9))