def is_on_xy(dot1, dot2):
    # Use a breakpoint in the code line below to debug your script.
    if (dot1 > 0 or dot1 < 0) and (dot2 > 0 or dot2 < 0):
        return "NOT ON X AND Y"
    elif dot1 == 0 and dot2 == 0:
        return "ON X AND Y"
    elif (dot1 > 0 or dot1 < 0) and dot2 == 0:
        return "ON Y"
    elif (dot2 > 0 or dot2 < 0) and dot1 == 0:
        return "ON X"


if __name__ == '__main__':
    # lab 1
    x = int(input("X:"))
    y = int(input("Y:"))
    print(is_on_xy(x, y))
