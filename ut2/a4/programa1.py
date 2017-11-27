import sys

dni = int(sys.argv[1])

dni_l = "TRWAGMYFPDXBNJZSQVHLCKE"
calcular_letra = dni % 23
calcular_dni_letra = dni_l[calcular_letra]
print(f"{dni}{calcular_dni_letra}")
