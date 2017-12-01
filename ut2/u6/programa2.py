def add_contacts(phone_book, name, phone):
    phone_book[name] = phone

def show_contacts(phone_book):
    print("-")
    if phone_book == {}:
        print("Lista sin registros")
    for name, number in phone_book.items():
        print("{}: {}".format(name, number))
    print("-")
    input("Pulsa una opción para regresar: ")

def remove_contacts(phone_book, name):
    del(phone_book[name])


def menu():
    phone_book = {}
    while True:
        print("1. Mostrar lista de contactos")
        print("2. Añadir contactos")
        print("3. Eliminar contactos")
        print("4. Salir")
        option = input("Pulsa alguna de la siguientes opciones: ")
        option = int(option)
        if option == 1:
            show_contacts(phone_book)
        if option == 2:
            name = input("¿Nombre del contacto? ")
            if name in phone_book:
                print("Lo siento. Este número ya existe actualmente")
            else:
                phone = input("¿Número del contacto? ")
                add_contacts(phone_book, name, phone)
        if option == 3:
            name = input("¿Qué contacto quieres eliminar? ")
            if name in phone_book:
                remove_contacts(phone_book, name)
            else:
                print("Contacto erróneo")
        if option == 4:
            print("Programa cerrado")
            break

menu()
