# Historia interactiva haciendo uso de la función *if*

# Texto inicial
print("\n\n~~~Una historia de amor~~~\n\n")
print("En este juego, debes presionar la tecla Enter para avanzar el texto.\n")
input()
print("Se te presentarán diversas elecciones que afectarán la historia. ¡Buena suerte!\n")
input()

# Nombre del jugador y del interés amoroso
nombre_jugador = input("¿Cuál es tu nombre?\n")
nombre_interes = input("¿Quién quieres que te acompañe en esta historia?\n")

# Ruta común
print(f"Estás en camino a tu primera cita con {nombre_interes}.")
input()
print(f"De repente, un número desconocido llama a tu teléfono.")
input()

print("\n\n~~~~~~~~~~~~~~~~~~~~~~~")
print(f"¿Contestas la llamada?")
print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
print("1. Sí                2. No")

opcion_ruta_comun= input("Elige 1 o 2: ")

if opcion_ruta_comun == "1" :        # Comienzo ruta A
    print(f"Al contestar, escuchas una voz familiar. Es la voz de tu madre.")
    input()
    print(f"Madre:    Acabo de ganar un concurso y tengo un cupón para dos porciones de cena en un restaurante esta noche.")
    input()
    print(f"Madre:    Se me ocurrió invitarte a ti. ¿Qué te parece?")
    input()
    print(f"Tu madre no sabe que hoy tienes una cita.")
    input()

    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"¿Le cuentas al respecto?")
    print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    print("1. Sí                2. No")


    opcion_ruta_a = input("Elige 1 o 2: ")

    if opcion_ruta_a == "1":        # Final A-1
        print(f"\nTu madre decide regalarte los cupones y tras una agradable cita,\ninvitas a {nombre_interes} a cenar contigo con los cupones que te regaló tu madre.")
        input()
        print(f"{nombre_interes} te invita a una segunda cita a la semana siguiente. ¡Felicidades!")
        input()
        print("Final A-1: Cena romántica")

    elif opcion_ruta_a == "2":        # Final A-2
        print(f"\nTe encuentras a tu madre en medio de tu cita con {nombre_interes} y arruina completamente el ambiente.")
        input()
        print(f"Nunca llegas a tener otra cita.")
        input()
        print("Final A-2: Cita arruinada")

    else:
        print("¡Opción inválida!")

elif opcion_ruta_comun == "2":        # Comienzo ruta B
    print(f"\nDecides ignorar la llamada.")
    input()
    print(f"Llegas a tu cita con {nombre_interes}.")
    input()
    print(f"Tras una agradable charla, decides que es hora de llevar a {nombre_interes} a algún lugar.")
    input()

    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"¿A dónde le llevas?")
    print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    print("1. A una cafetería elegante            2. A una librería")

    opcion_ruta_b = input("Elige 1 o 2: ")

    if opcion_ruta_b == "1":        # Final B-1
        print(f"\nTodo va bien, pero cuando traen tu café, lo derramas por accidente y manchas tu ropa.")
        input()
        print(f"Entras en pánico, pero logras calmarte y ayudas a los camareros a limpiar el desastre.")
        input()
        print(f"Al salir de la cafetería, decides dejar una propina generosa.")
        input()
        print(f"A {nombre_interes} le llamó la atención tu capacidad de manejar esa situación vergonzosa.")
        input()
        print(f"{nombre_interes} te invita a una segunda cita la semana siguiente. ¡Felicidades!")
        input()
        print("Final B-1: Cita salvada")

    elif opcion_ruta_b == "2":        # Final B-2
        print(f"\nSabías que a {nombre_interes} le gusta leer y pensaste que la librería sería un buen lugar.")
        input()
        print(f"Sin embargo, {nombre_interes} parece perder interés conforme pasa el tiempo.")
        input()
        print(f"Al finalizar la cita, dudas de si tendrás una segunda cita con {nombre_interes}.")
        input()
        print("Final B-2: Incertidumbre")
    else:
        print("¡Opción inválida!")
else:
    print("¡Opción inválida!")
