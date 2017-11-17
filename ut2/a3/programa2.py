import sys
x = int(sys.argv[1])

if x >= 0:
    sumando = 0
    for suma in range(1, x + 1):
        cuadrado = suma**2
        sumando += cuadrado
    else:
        print(sumando)
else:
    print("No puede ser un numero negativo")
