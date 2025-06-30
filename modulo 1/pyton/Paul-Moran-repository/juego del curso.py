def juego_de_aventura():
    print("Estás explorando una antigua ruina subterránea. Frente a ti hay una MOCHILA y un CUCHILLO. ¿Cuál eliges?")
    eleccion1 = input(">> ").upper()

    if eleccion1 == "MOCHILA":
        print("\nTomas la mochila y la abres. Dentro hay una cuerda, una linterna y una botella de agua.")
        print("Sigues avanzando y encuentras una cueva muy oscura. ¿Quieres USAR linterna, GRITAR para ver si hay eco o ESPERAR?")
        eleccion2 = input(">> ").upper()

        if eleccion2 == "USAR LINTERNA":
            print("\nEnciendes la linterna y ves una criatura durmiendo. Tienes que decidir si la ESQUIVAS o la DESPIERTAS.")
            eleccion3 = input(">> ").upper()
            if eleccion3 == "ESQUIVAS":
                print("\nLa esquivas con éxito y encuentras una salida secreta. ¡Has escapado de la ruina con vida!")
            elif eleccion3 == "DESPIERTAS":
                print("\nLa criatura despierta furiosa y te ataca. Fin del juego.")
            else:
                print("\nOpción no válida. La criatura despierta mientras dudas. Fin del juego.")

        elif eleccion2 == "GRITAR":
            print("\nEl eco resuena fuertemente. Algo se despierta al fondo y corre hacia ti. ¿CORRER o ESCONDERTE?")
            eleccion3 = input(">> ").upper()
            if eleccion3 == "CORRER":
                print("\nCorres a toda velocidad y logras salir por donde entraste. ¡Sobreviviste!")
            elif eleccion3 == "ESCONDERTE":
                print("\nTe escondes tras una roca, pero lo que despertaste te encuentra. Fin del juego.")
            else:
                print("\nOpción no válida. La criatura te alcanza mientras dudas. Fin del juego.")

        elif eleccion2 == "ESPERAR":
            print("\nEsperas pacientemente. Escuchas pasos acercándose. ¿HABLAR o ATACAR?")
            eleccion3 = input(">> ").upper()
            if eleccion3 == "ATACAR":
                print("\nAtacas por sorpresa a un explorador amistoso. No fue buena idea. Fin del juego.")
            elif eleccion3 == "HABLAR":
                print("\nEra otro explorador. Te ayuda a salir. ¡Sobreviviste!")
            else:
                print("\nOpción no válida. El extraño te confunde con un enemigo. Fin del juego.")
        else:
            print("\nOpción no válida. Te pierdes en la oscuridad. Fin del juego.")

    elif eleccion1 == "CUCHILLO":
        print("\nTomas el cuchillo y avanzas por un pasillo. Un grupo de murciélagos te ataca. ¿DEFENDERTE o AGACHARTE?")
        eleccion2 = input(">> ").upper()

        if eleccion2 == "DEFENDERTE":
            print("\nUsas el cuchillo para espantarlos, pero uno te muerde. Encuentras una sala con tres puertas: ROJA, VERDE, AZUL. ¿Cuál eliges?")
            eleccion3 = input(">> ").upper()
            if eleccion3 == "ROJA":
                print("\nCaes en una trampa de fuego. Fin del juego.")
            elif eleccion3 == "VERDE":
                print("\nEncuentras un pasadizo secreto hacia la salida. ¡Has escapado con vida!")
            elif eleccion3 == "AZUL":
                print("\nUna sala llena de gas tóxico. Fin del juego.")
            else:
                print("\nOpción no válida. Te desorientas y te desmayas. Fin del juego.")

        elif eleccion2 == "AGACHARTE":
            print("\nTe agachas y los murciélagos pasan de largo. Encuentras un mapa en el suelo. ¿SEGUIR el mapa o ROMPERLO?")
            eleccion3 = input(">> ").upper()
            if eleccion3 == "SEGUIR":
                print("\nEl mapa te guía a una cámara secreta llena de tesoros. ¡Victoria!")
            elif eleccion3 == "ROMPERLO":
                print("\nRompes el mapa y te pierdes en los pasadizos. Fin del juego.")
            else:
                print("\nOpción no válida. El mapa se te cae en una grieta. Fin del juego.")
        else:
            print("\nOpción no válida. Los murciélagos te rodean y huyes confundido. Fin del juego.")
    else:
        print("\nOpción no válida. No tomas nada y te pierdes sin rumbo. Fin del juego.")

# Iniciar el juego
juego_de_aventura()

2