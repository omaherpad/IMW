import sys

x = int(sys.argv[1])
x2 = int(sys.argv[2])

if (x <= 0 or x2 <= 0):
    print("Error")
else:
    if (x < x2):
        for i in range(x, 0, -1):
            if (x % i == 0 and x2 % i == 0):
                print ("El m.c.d. de", x, "y", x2, "es", i)
                break
    elif (x == x2):
        print ("El m.c.d. de", x, "y", x2, "es", x)
    else:
        for i in range(x2, 0, -1):
            if (x2 % i == 0 and x % i == 0):
                print ("el m.c.d. de", x, "y", x2, "es", i)
                break
