def setOrNot(number, n):
    mask = 1
    if (n & mask) == 1 or (n & mask) == 0:
        if number & (1 << (n -1)):
            print("SET")
        else:
            print("NOT SET")
number = int (input("Enter your number:"))
n = int(input("Enter your bit position:"))
setOrNot(number , n)
