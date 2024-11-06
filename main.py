from funciones import configurar_juego, combate, mostrar_historial

def jugar():
    print("¡Bienvenido al juego de combate contra zombies!")
    historial_personajes = []
    
    seguir_jugando = True
    while seguir_jugando:
        # Configurar nuevos personajes para cada partida
        personajes = configurar_juego()
        
        # Agregar cada personaje al historial acumulado uno por uno
        for personaje in personajes:
            historial_personajes.append(personaje)
        
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


"""

1 - Inicio en el archivo "main":

A - Cuando ejecutas el código, se llama a la función jugar(), y se muestra el mensaje de bienvenida: 
"¡Bienvenido al juego de combate contra zombies!".

B - Se crea una lista vacía llamada historial_personajes que acumulará los personajes creados en cada partida.

-----------------------------------------------------------------------------------------------------------------------

2 - Bucle principal (while seguir_jugando):

A - Este bucle permite que el juego se repita hasta que el jugador elija salir. La variable seguir_jugando controla si 
se debe continuar o terminar el juego.

-----------------------------------------------------------------------------------------------------------------------

3 -Configuración de personajes (configurar_juego):

A - Se llama a la función configurar_juego() para crear nuevos personajes.

B - En configurar_juego, el usuario ingresa el número de personajes (entre 1 y 4) que quiere en el juego. 
Se valida que el número esté en el rango.

C - Luego, para cada personaje:
Se le pide el nombre y la cantidad de vida (entre 1 y 100), asegurando que el valor esté dentro de este rango.

Se elige un arma de la lista (pistola, escopeta, ametralladora), descontando el costo del arma (en puntos) de un 
total inicial de 100 puntos. Esto se hace restando el costo del arma de los puntos disponibles para cada personaje.

Cada personaje se almacena en un diccionario con sus atributos (nombre, vida, puntos iniciales y arma) y 
se agrega a la lista personajes, que se retorna al final de la función.
De vuelta en jugar, la lista de personajes de la partida actual se agrega a historial_personajes.

-----------------------------------------------------------------------------------------------------------------------

4 - Turnos de combate (combate):

A - Para cada personaje configurado, se inicia su turno de combate llamando a la función combate(personaje).

B - En combate, se simula un disparo al azar en una zona de impacto (cabeza, pecho, o piernas) seleccionada aleatoriamente, 
y se determina los puntos ganados en base a esa área (usando el diccionario impacto_puntos).

C - Se incrementan los puntos del personaje con los puntos obtenidos del disparo, y se muestra un mensaje 
indicando el impacto y los puntos ganados.

-----------------------------------------------------------------------------------------------------------------------

5 - Opciones después del turno de combate:

A - Después de que cada personaje complete su turno, el jugador elige una de las siguientes opciones:

Continuar (1): reinicia el bucle y vuelve a la configuración de nuevos personajes.

Ver Historial (2): muestra el historial de todos los personajes creados hasta el momento usando mostrar_historial(historial_personajes).

Salir (3): termina el juego, muestra el historial final y da el mensaje de despedida "¡Gracias por jugar!".

Cada opción es validada para asegurar que el jugador ingrese un número correcto (1, 2 o 3).

-----------------------------------------------------------------------------------------------------------------------

6 - Fin del juego:

A - Si el jugador elige "Salir", el juego termina y se muestra el historial final de los personajes.

"""