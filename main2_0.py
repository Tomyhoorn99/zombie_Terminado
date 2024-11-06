from funciones2_0 import *

def jugar():
    print("¡Bienvenido al juego de combate contra zombies!")
    historial_personajes = []
    seguir_jugando = True
    
    # Configurar el primer personaje
    personaje = configurar_personaje()
    historial_personajes.append(personaje)
    
    while seguir_jugando:
        print(f"\nTurno de {personaje['nombre']} - Clase: {personaje['clase']} - Vida: {personaje['vida']} - Puntos: {personaje['puntos']}")
        
        # Realizar el turno de combate
        combate(personaje)
        
        # Zombie ataca al personaje
        ataque_zombie(personaje)
        
        # Opción de lo que hacer
        while True:
            print("\n¿Qué deseas hacer ahora?")
            print("1: Continuar jugando con el mismo personaje")
            print("2: Ver Historial")
            print("3: Comprar (arma o vendas)")
            print("4: Salir del juego")
            
            opcion = int(input("Ingresa el número de la opción: "))
            
            if opcion == 1:
                break  # Continuar con el mismo personaje
            elif opcion == 2:
                mostrar_historial(historial_personajes)
            elif opcion == 3:
                comprar(personaje)  # Función de compra opcional
            elif opcion == 4:
                mostrar_historial(historial_personajes)
                print("¡Gracias por jugar!")
                seguir_jugando = False
                break

jugar()
