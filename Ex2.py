def intWithinBounds (x,y,z):
    if y<=x<z:
        return True
    else:
        return False

print(intWithinBounds(6, 1, 6))