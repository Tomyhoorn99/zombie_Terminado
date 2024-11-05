from funciones import configurar_juego, combate, mostrar_historial

def jugar():
    print("¡Bienvenido al juego de combate contra zombies!")
    historial_personajes = []
    
    seguir_jugando = True
    while seguir_jugando:
        # Configurar nuevos personajes para cada partida
        personajes = configurar_juego()
        historial_personajes.extend(personajes)  # Agregar personajes al historial acumulado
        
        # Realizar el turno de combate para cada personaje
        for personaje in personajes:
            print(f"\nTurno de {personaje['nombre']} - Vida: {personaje['vida']} - Puntos: {personaje['puntos']}")
            combate(personaje)
        
        # Preguntar si desea continuar, ver el historial o salir
        while True:
            print("\n¿Qué deseas hacer ahora?")
            print("1: Continuar")
            print("2: Ver Historial")
            print("3: Salir")
            try:
                opcion = int(input("Ingresa el número de la opción: "))
                if opcion == 1:
                    break  # Volver al inicio del bucle para configurar nuevos personajes
                elif opcion == 2:
                    mostrar_historial(historial_personajes)
                elif opcion == 3:
                    mostrar_historial(historial_personajes)  # Mostrar historial final
                    print("¡Gracias por jugar!")
                    seguir_jugando = False
                    break
                else:
                    print("Opción no válida. Por favor elige 1, 2 o 3.")
            except ValueError:
                print("Entrada inválida. Ingresa un número (1, 2 o 3).")

# Iniciar el juego
jugar()
