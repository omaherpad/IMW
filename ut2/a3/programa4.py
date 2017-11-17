import sys
x = int(sys.argv[1])
if x >= 0:
    valor = 1
    for i in range(1, x + 1):
        valor = i * valor
        print(i, "!=", valor)
else:
    print("No puede ser un numero negativo")
