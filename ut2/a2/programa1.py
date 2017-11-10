import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if a == 0:
    solucion = -c / b
    print(solucion)
else:
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        print("no_solución")
    else:
        x = (-b + math.sqrt(discriminante)) / 2 * a
        print("x", x)

        x2 = (-b - math.sqrt(discriminante)) / 2 * a
        print("x2", x2)
