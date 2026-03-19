print("----COMIENZA LA HISTORIA----")
print("eleccion 1")
print("1. Camino1")
print("2. Camino2")

opcion_elegida = input("Elige 1 o 2: ")

if opcion_elegida == "1" :
    print("elecion 2")
    print("1-------")
    print("2-------")

    opcion_elegida = input("Elige 1 o 2: ")

    if opcion_elegida == "1":
        print("eleccion 3")
        print("1=====")
        print("2=====")
        opcion_elegida = input("Elige 1 o 2: ")

        if opcion_elegida == "1" :
            print("fin")
        else :
            if opcion_elegida == "2":
                print("otro fin")
            else :
                print("opcion no valida, sin fin")

    else :
        if opcion_elegida == "2":
            print("otro fin distinto")
        else :
            print("opcion no valida, sin fin")

#aca faltan los caminos
else :
    if opcion_elegida == "2" :
        print("elegiste 2")
    else:
        print("opcion no valida, fin de la historia")
