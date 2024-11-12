import random

# Constantes
puntos_iniciales = 30
max_vida = 150

# Clases de personajes con vida predeterminada
clases = {
    1: ("Novato", 120),  # Más vida
    2: ("Superviviente", 80),  # Vida media
    3: ("Soy Leyenda", 50)  # Menos vida
}

# Armas y sus puntos
armas = {
    1: ("pistola", 0),  # Básico
    2: ("subfusible", 30),  # Intermedio
    3: ("escopeta", 50),  # Avanzado
    4: ("ametralladora", 100)  # Mayor
}

# Áreas de impacto con sus puntos para los jugadores
puntos_impacto = {
    "cabeza": 100,
    "pecho": 50,
    "piernas": 30
}

# Áreas de impacto y daño para ataques del zombie
ataques = {
    "mordisco": 30,
    "arañazo": 20,
    "golpe": 15
}



def obtener_numero(mensaje, min_val, max_val):
    """Solicita un número entero dentro de un rango definido.

    Args:
        mensaje (str): Mensaje para solicitar la entrada.
        min_val (int): Valor mínimo aceptado.
        max_val (int): Valor máximo aceptado.

    Returns:
        int: El número ingresado dentro del rango.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Por favor, ingresa un número entre {min_val} y {max_val}.")
        except ValueError:
            print("ERROR. Por favor ingresa un número.")



def elegir_clase_personaje():
    """Permite al jugador elegir una clase de personaje.

    Returns:
        tuple: Clase y vida predeterminada del personaje.
    """
    print("\nElige la dificultad de tu personaje:")
    print("1: Novato (Vida: 150)")
    print("2: Superviviente (Vida: 80)")
    print("3: Soy Leyenda (Vida: 50)")
    while True:
        clase_opcion = obtener_numero("Ingresa 1 para Novato, 2 para Superviviente o 3 para Soy Leyenda: ", 1, 3)
        if clase_opcion in clases:
            clase, vida = clases[clase_opcion]
            return clase, vida



def configurar_personaje():
    """Configura el personaje con nombre, clase, y arma inicial.

    Returns:
        dict: Datos del personaje, incluyendo nombre, clase, vida, puntos, y arma.
    """
    print("🧟‍♂️💀 Configuración de Superviviente Iniciada 💀🧟‍♂️")
    nombre = input("Nombre del personaje: ")
    
    clase, vida = elegir_clase_personaje()
    
    print(f"\nElige un arma: tienes {puntos_iniciales} puntos.")
    for num, (arma, costo) in armas.items():
        print(f"{num}: {arma.capitalize()} (Costo en puntos: {costo})")

    while True:
        arma_opcion = obtener_numero("Ingresa el número del arma: ", 1, 4)
        arma, costo_arma = armas[arma_opcion]
        
        if puntos_iniciales >= costo_arma:
            puntos = puntos_iniciales - costo_arma
            return {
                "nombre": nombre,
                "clase": clase,
                "vida": vida,
                "puntos": puntos,
                "arma": arma
            }
        else:
            print("No tienes suficientes puntos para esta arma. Elige otra.")



def comprar(personaje):
    """Permite al personaje comprar un arma o vendas.

    Args:
        personaje (dict): Información del personaje con puntos y vida.
    """
    print("\n¿Qué deseas comprar?")
    print("1: Comprar otra arma")
    print("2: Comprar vendas")
    print("3: No comprar nada")

    opcion = obtener_numero("Ingresa 1 para comprar arma, 2 para comprar vendas o 3 para no comprar: ", 1, 3)

    if opcion == 1:
        print(f"\nElige un arma: tienes {personaje['puntos']} puntos:")
        for num, (arma, puntos) in armas.items():
            print(f"{num}: {arma.capitalize()} (Costo en puntos: {puntos})")
        
        arma_opcion = obtener_numero("Ingresa el número del arma: ", 1, len(armas))
        arma, costo_arma = armas[arma_opcion]
        
        if personaje['puntos'] >= costo_arma:
            personaje['puntos'] -= costo_arma
            personaje['arma'] = arma
            print(f"\nHas comprado la {arma} y ahora tienes {personaje['puntos']} puntos restantes.")
        else:
            print("\nNo tienes suficientes puntos para comprar esta arma.")
    
    elif opcion == 2:
        print(f"\nElige la cantidad de curación que deseas, tienes: {personaje['vida']} vida")
        print("1: 10 puntos de vida (Costo: 20 puntos)")
        print("2: 20 puntos de vida (Costo: 40 puntos)")
        print("3: 30 puntos de vida (Costo: 60 puntos)")

        curacion_opcion = obtener_numero("Ingresa el número de la cantidad de curación: ", 1, 3)
        curacion_valores = {1: (10, 20), 2: (20, 40), 3: (30, 60)}
        curacion, costo_vendas = curacion_valores[curacion_opcion]

        if personaje['puntos'] >= costo_vendas:
            personaje['vida'] += curacion
            if personaje['vida'] > max_vida:
                personaje['vida'] = max_vida
            personaje['puntos'] -= costo_vendas
            print(f"\nHas comprado vendas. Tu vida se ha incrementado en {curacion} puntos.")
            print(f"Ahora tienes {personaje['vida']} de vida y {personaje['puntos']} puntos restantes.")
        else:
            print("\nNo tienes suficientes puntos para comprar estas vendas.")



def combate(personaje):
    """Simula un combate donde el personaje obtiene puntos de impacto.

    Args:
        personaje (dict): Datos del personaje.
    """
    impacto = random.choice(list(puntos_impacto.keys()))
    puntos_ganados = puntos_impacto[impacto]
    personaje['puntos'] += puntos_ganados
    
    print(f"\n{personaje['nombre']} dispara con {personaje['arma']} y hace un disparo en el/la {impacto} del zombie.")
    print(f"Ganas {puntos_ganados} puntos.")



def ataque_zombie(personaje):
    """Realiza un ataque de un zombie al personaje, reduciendo su vida.

    Args:
        personaje (dict): Datos del personaje.
    """
    ataque = random.choice(list(ataques.keys()))
    danio = ataques[ataque]
    personaje['vida'] -= danio

    print(f"¡El zombie ataca a {personaje['nombre']} con un {ataque} y causa {danio} de daño!")
    if personaje['vida'] <= 0:
        personaje['vida'] = 0
        print(f"{personaje['nombre']} ha sido derrotado por el zombie.")



def mostrar_historial(historial_personajes):
    """Muestra el historial de personajes.

    Args:
        historial_personajes (list): Lista de personajes jugados.
    """
    print("\nHistorial de los jugadores:")
    for personaje in historial_personajes:
        print(f"Nombre: {personaje['nombre']}, Clase: {personaje['clase']}, Vida: {personaje['vida']}, Arma: {personaje['arma']}, Puntos Finales: {personaje['puntos']}")



def guardar_historial(historial):
    """Guarda el historial de personajes en un archivo de texto.

    Args:
        historial (list): Lista de personajes jugados.
    """
    with open("historial_juego.txt", "a") as file:
        for personaje in historial:
            file.write(f"{personaje['nombre']}, {personaje['clase']}, Vida: {personaje['vida']}, Arma: {personaje['arma']}, Puntos finales: {personaje['puntos']}, zombies eliminados: {personaje['zombies_eliminados']}\n")
    print("\nHistorial guardado en 'historial_juego.txt'.")



def jugar():
    """Ejecuta el flujo principal del juego."""
    print("¡Bienvenido al juego de combate contra zombies!")
    historial_personajes = []
    seguir_jugando = True
    
    while seguir_jugando:
        personaje = configurar_personaje()
        personaje['zombies_eliminados'] = 0
        historial_personajes.append(personaje)
        
        while True:
            print(f"\nTurno de {personaje['nombre']} - Clase: {personaje['clase']} - Vida: {personaje['vida']} - Puntos: {personaje['puntos']}")
            combate(personaje)
            personaje['zombies_eliminados'] += 1
            ataque_zombie(personaje)
            
            if personaje['vida'] <= 0:
                print(f"\n{personaje['nombre']} ha sido derrotado. Fin del juego.")
                seguir_jugando = input("¿Quieres seguir jugando? (si/no): ").strip().lower() == "si"
                if not seguir_jugando:
                    guardar_historial(historial_personajes)
                    print("¡Gracias por jugar!")
                break
            
            print("\n¿Qué deseas hacer ahora?")
            print("1: Continuar jugando con el mismo personaje")
            print("2: Ver Historial")
            print("3: Comprar (arma o vendas)")
            print("4: Salir del juego")
            
            opcion = int(input("Ingresa el número de la opción: "))
            
            if opcion == 1:
                continue
            elif opcion == 2:
                mostrar_historial(historial_personajes)
            elif opcion == 3:
                comprar(personaje)
            elif opcion == 4:
                guardar_historial(historial_personajes)
                print("¡Gracias por jugar!")
                seguir_jugando = False
                break
