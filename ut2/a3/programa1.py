import sys

x = int(sys.argv[1])
if x <= 0:
    print ("Numero no es positivo, fin del programa")
else:
    for a in range(2, x):
        resto = x % a
        if resto == 0:
            break
            print ("No es un número primo")
    else:
        print ("Es un número primo")
