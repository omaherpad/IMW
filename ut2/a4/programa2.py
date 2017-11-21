import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100

sequence = "".join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])

suma_Ad = 0
suma_Gu = 0
suma_Cy = 0
suma_Th = 0

for cr in (sequence):
    if cr == "A":
        suma_Ad = suma_Ad + 1
    elif cr == "G":
        suma_Gu = suma_Gu + 1
    elif cr == "C":
        suma_Cy = suma_Cy + 1
    elif cr == "T":
        suma_Th = suma_Th + 1
print(f"Adenine:{suma_Ad}\nGuanine:{suma_Gu}\nCytosine:{suma_Cy}\nThymine:{suma_Th}")
