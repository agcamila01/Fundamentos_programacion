# Historia interactiva haciendo uso de la función *if*

# Texto inicial
print("\n\n~~~Una historia de amor~~~\n\n")
print("En este juego, debes presionar la tecla Enter para avanzar el texto.\n")
input()
print("Se te presentarán diversas elecciones que afectarán la historia. ¡Buena suerte!\n")
input()

# Nombre del jugador y del interés amoroso
# nombre_jugador = input("¿Cuál es tu nombre? ")
# nombre_interes= input("¿Cuál es el nombre del amor de tu vida? ")

# Ruta común
print("eleccion 1")
print("1. Camino1")
print("2. Camino2")

opcion_ruta_comun= input("Elige 1 o 2: ")

if opcion_ruta_comun == "1" : # Comienzo ruta A
    print("elecion 2")
    print("1-------")
    print("2-------")

    opcion_ruta_a = input("Elige 1 o 2: ")

    if opcion_ruta_a == "1":
        print("final 1")
    elif opcion_ruta_a == "2":
        print("final 2")
    else:
        print("opcion no valida, sin fin")

elif opcion_ruta_comun == "2": # Comienzo ruta B
    print("elecion 2")
    print("1-------")
    print("2-------")

    opcion_ruta_b = input("Elige 1 o 2: ")

    if opcion_ruta_b == "1":
        print("final 3")
    elif opcion_ruta_b == "2":
        print("final 4")
    else:
        print("opcion no valida, sin fin")
else:
    print("opcion no valida, sin fin")
