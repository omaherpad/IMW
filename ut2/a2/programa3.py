import sys

notas = float(sys.argv[1])

if notas >= 0 and notas <= 10:

    if notas < 5:
        print ("Suspenso")
    if notas >= 5 and notas < 7:
        print ("Aprobando")
    if notas >= 7 and notas < 9:
        print ("Notable")
    if notas >= 9 and notas < 10:
        print ("Sobresaliente")
    if notas == 10:
        print ("Matrícula de honor")
else:
    print ("Error")
