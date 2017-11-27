import sys

number = int(sys.argv[1])
text = str(sys.argv[2])

if number < 0:
    print("Error. El número es negativo")
    sys.exit()
else:
    text_list = text.split(" ")
    suma = 0

    for cr in text_list:
        if len(cr) == number:
            suma = suma + 1
    print(f"Hay {suma} palabras de tamaño {number}")
