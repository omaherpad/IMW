import sys
import math

radio = float(sys.argv[1])
print ("(1) Calcular el diámetro de la circunferencia:")
print ("(2) Calcular el perímetro de la circunferencia:")
print ("(3) Calcular el área del círculo:")
print ("(4) Salir.")

option = int(input("Elije una opción:"))

diametro = 2 * radio
perimetro = 2 * math.pi * radio
area = math.pi * radio**2

if option == 1:
    print (diametro)
elif option == 2:
    print (perimetro)
elif option == 3:
    print (area)
elif option == 4:
    print ("Has salido correctamente")

else:
    print ("Elija una opción correcta")
