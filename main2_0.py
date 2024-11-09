from funciones2_0 import *

# def jugar():
#     print("¡Bienvenido al juego de combate contra zombies!")
#     historial_personajes = []
#     seguir_jugando = True
    
#     # Configurar el primer personaje
#     personaje = configurar_personaje()
#     historial_personajes.append(personaje)
    
#     while seguir_jugando:
#         print(f"\nTurno de {personaje['nombre']} - Clase: {personaje['clase']} - Vida: {personaje['vida']} - Puntos: {personaje['puntos']}")
        
#         # Realizar el turno de combate
#         combate(personaje)
        
#         # Zombie ataca al personaje
#         ataque_zombie(personaje)
        
#         # Opción de lo que hacer
#         while True:
#             print("\n¿Qué deseas hacer ahora?")
#             print("1: Continuar jugando con el mismo personaje")
#             print("2: Ver Historial")
#             print("3: Comprar (arma o vendas)")
#             print("4: Salir del juego")
            
#             opcion = int(input("Ingresa el número de la opción: "))
            
#             if opcion == 1:
#                 break  # Continuar con el mismo personaje
#             elif opcion == 2:
#                 mostrar_historial(historial_personajes)
#             elif opcion == 3:
#                 comprar(personaje)  # Función de compra opcional
#             elif opcion == 4:
#                 mostrar_historial(historial_personajes)
#                 print("¡Gracias por jugar!")
#                 seguir_jugando = False
#                 break

# jugar()


from funciones2_0 import *

def jugar():
    print("¡Bienvenido al juego de combate contra zombies!")
    historial_personajes = []
    seguir_jugando = True
    
    # Configurar el primer personaje
    personaje = configurar_personaje()
    personaje['zombies_eliminados'] = 0  # Contador de zombies eliminados
    historial_personajes.append(personaje)
    
    while seguir_jugando:
        print(f"\nTurno de {personaje['nombre']} - Clase: {personaje['clase']} - Vida: {personaje['vida']} - Puntos: {personaje['puntos']}")
        
        # Realizar el turno de combate
        combate(personaje)
        personaje['zombies_eliminados'] += 1  # Incrementar zombies eliminados
        
        # Zombie ataca al personaje
        ataque_zombie(personaje)
        
        # Verificar si el personaje ha sido derrotado
        if personaje['vida'] <= 0:
            print(f"\n{personaje['nombre']} ha sido derrotado. Fin del juego.")
            print("Historial del juego:")
            print(f"Nombre del personaje: {personaje['nombre']}")
            print(f"Zombies eliminados: {personaje['zombies_eliminados']}")
            print(f"Puntos finales: {personaje['puntos']}")
            seguir_jugando = False
            break
        
        # Opción de lo que hacer
        while seguir_jugando:
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
