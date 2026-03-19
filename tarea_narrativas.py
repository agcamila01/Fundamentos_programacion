# Historia interactiva haciendo uso de la función *if*

# Texto inicial
print("\n\n~~~Una historia de amor~~~\n\n")
print("En este juego, debes presionar la tecla Enter para avanzar el texto.\n")
input()
print("Se te presentarán diversas elecciones que afectarán la historia. ¡Buena suerte!\n")
input()

# Nombre del jugador y del interés amoroso
nombre_jugador = input("¿Cuál es tu nombre?\n")
nombre_interes = input("¿Cuál es el nombre del amor de tu vida?\n")

# Ruta común
print(f"\nDesde que conociste a {nombre_interes}, no pudiste evitar enamorarte.")
input()
print(f"Tal vez era la manera en la que te hablaba, o quizás era su sonrisa inocente.")
input()
print(f"Tras mucho dudar y no saber si pedirle una cita o no, {nombre_interes} tomó la inciativa.")
input()
print(f"Estás en camino a tu primera cita con {nombre_interes}.")
input()
print(f"De repente, un número desconocido llama a tu teléfono.")
input()
print(f"Piensas en contestar, pero queda poco tiempo para tu cita y no quieres perder el tiempo.")
input()

print("\n\n~~~~~~~~~~~~~~~~~~~~~~~")
print(f"¿Contestas la llamada?")
print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
print("1. Sí                2. No")

opcion_ruta_comun= input("Elige 1 o 2: ")

if opcion_ruta_comun == "1" :        # Comienzo ruta A
    print(f"\nPiensas que contestar no debería quitarte mucho tiempo.")
    input()
    print(f"Al contestar, escuchas una voz familiar. Es la voz de tu madre.")
    input()
    print(f"Madre:    ¡Hola! Perdón por llamarte de repente. ¿Tienes tiempo?")
    input()
    print(f"{nombre_jugador}:    Eh... No mucho. Espera, ¿por qué me llamas desde este número?")
    input()
    print(f"Madre:    ¿No te avisé ya que me cambiaría de número?")
    input()
    print(f"{nombre_jugador}:    Ah, tienes razón. Bueno, ¿pasa algo? ¿Por qué la llamada tan repentina?")
    input()
    print(f"Madre:    Verás... Acabo de ganar un concurso y tengo un cupón para dos porciones de cena en un restaurante esta noche.")
    input()
    print(f"Madre:    Pensé en invitar a tu padre a una cita, pero ya me avisó que no podría.")
    input()
    print(f"Madre:    Asi que se me ocurrió invitarte a ti. ¿Qué te parece?")
    input()
    print(f"Tu cita probablemente se alargue hasta la noche. No es buena idea decirle que sí.")
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
        print(f"Notas el desinterés de {nombre_interes}.")
        input()
        print(f"Al finalizar la cita, {nombre_interes} dice que probablemente te invite a otra cita en algún momento.")
        input()
        print(f"Nunca llegas a tener otra cita.")
        input()
        print("Final A-2: Cita arruinada")

    else:
        print("¡Opción inválida!")

elif opcion_ruta_comun == "2":        # Comienzo ruta B
    print(f"\nDecides ignorar la llamada. Pronto te llega un mensaje que también decides ignorar.")
    input()
    print(f"Llegas a tu cita con {nombre_interes}. {nombre_interes} te está esperando en una plaza.")
    input()
    print(f"{nombre_jugador}:    ¡{nombre_interes}!")
    input()
    print(f"{nombre_interes}:    H-hola, {nombre_jugador}. ¿Cómo estás?")
    input()
    print(f"{nombre_jugador}:    De maravilla. ¿Tardé mucho en llegar?")
    input()
    print(f"{nombre_interes}:    Para nada. Si acaso, yo llegué muy temprano, hehe.")
    input()
    print(f"No puedes evitar sonrojarte al escuchar la risita de {nombre_interes}.")
    input()
    print(f"Conversas con {nombre_interes} en la plaza por un buen rato. {nombre_interes} la está pasando bien.")
    input()
    print(f"Tras una agradable charla, decides que es hora de llevar a {nombre_interes} a algún lugar.")
    input()
    print(f"Sin embargo, no planeaste de antemano a dónde le llevarías.")
    input()
    print(f"Se te vienen a la mente dos lugares.")
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
        print(f"Se queda con un divertido recuerdo de su primera cita contigo.")
        input()
        print(f"{nombre_interes} te invita a una segunda cita la semana siguiente. ¡Felicidades!")
        input()
        print("Final B-1: Cita salvada")

    elif opcion_ruta_b == "2":        # Final B-2
        print(f"\nSabías que a {nombre_interes} le gusta leer y pensaste que la librería sería un buen lugar.")
        input()
        print(f"Sin embargo, {nombre_interes} parece perder interés conforme pasa el tiempo.")
        input()
        print(f"{nombre_interes} quería pasar tiempo de calidad contigo y estuviste\ntodo el tiempo intentando verte intelectual para impresionarle.")
        input()
        print(f"Te das cuenta demasiado tarde.")
        input()
        print(f"Al finalizar la cita, dudas de si tendrás una segunda cita con {nombre_interes}.")
        input()
        print("Final B-2: Incertidumbre")
    else:
        print("¡Opción inválida!")
else:
    print("¡Opción inválida!")
