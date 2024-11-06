import random

# Constantes
puntos_iniciales = 100
max_vida = 150

# Clases de personajes con vida predeterminada
clases = {
    1: ("tanque", 150),  # Más vida
    2: ("dps", 80)       # Menos vida
}

# Armas y sus puntos
armas = {
    1: ("pistola", 30),
    2: ("escopeta", 50),
    3: ("ametralladora", 100)
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

# Función para obtener un número entero dentro de un rango
def obtener_numero(mensaje, min_val, max_val):
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Por favor, ingresa un número entre {min_val} y {max_val}.")
        except ValueError:
            print("ERROR. Por favor ingresa un número.")

# Función para elegir clase del personaje
def elegir_clase_personaje():
    print("\nElige la clase de tu personaje:")
    print("1: Tanque (Vida: 150)")
    print("2: DPS (Vida: 80)")
    
    while True:
        clase_opcion = obtener_numero("Ingresa 1 para Tanque o 2 para DPS: ", 1, 2)
        if clase_opcion in clases:
            clase, vida = clases[clase_opcion]
            return clase, vida

# Función para configurar al personaje
def configurar_personaje():
    print("---Configurando personaje---")
    nombre = input("Nombre del personaje: ")
    
    # Elegir clase y vida predeterminada
    clase, vida = elegir_clase_personaje()
    
    print("Elige un arma:")
    for num, (arma, puntos) in armas.items():
        print(f"{num}: {arma.capitalize()} (Costo en puntos: {puntos})")
    arma_opcion = obtener_numero("Ingresa el número del arma: ", 1, 3)
    
    arma, costo_arma = armas[arma_opcion]
    puntos = puntos_iniciales - costo_arma

    return {
        "nombre": nombre,
        "clase": clase,
        "vida": vida,
        "puntos": puntos,
        "arma": arma
    }

# Función de compra de objetos (arma o vendas)
def comprar(personaje):
    print("\n¿Qué deseas comprar?")
    print("1: Comprar otra arma")
    print("2: Comprar vendas ")
    print("3: No comprar nada")

    opcion = obtener_numero("Ingresa 1 para comprar arma, 2 para comprar vendas o 3 para no comprar: ", 1, 3)

    if opcion == 1:
        print("\nElige un arma:")
        for num, (arma, puntos) in armas.items():
            print(f"{num}: {arma.capitalize()} (Costo en puntos: {puntos})")
        
        arma_opcion = obtener_numero("Ingresa el número del arma: ", 1, len(armas))
        arma, costo_arma = armas[arma_opcion]
        
        if personaje['puntos'] >= costo_arma:
            personaje['puntos'] -= costo_arma
            personaje['arma'] = arma  # Equipar nueva arma
            print(f"\nHas comprado la {arma} y ahora tienes {personaje['puntos']} puntos restantes.")
        else:
            print("\nNo tienes suficientes puntos para comprar esta arma.")

    elif opcion == 2:
        print("\nElige la cantidad de curación que deseas:")
        print("1: 10 puntos de vida (Costo: 20 puntos)")
        print("2: 20 puntos de vida (Costo: 40 puntos)")
        print("3: 30 puntos de vida (Costo: 60 puntos)")

        curacion_opcion = obtener_numero("Ingresa el número de la cantidad de curación: ", 1, 3)
        curacion_valores = {1: (10, 20), 2: (20, 40), 3: (30, 60)}
        curacion, costo_vendas = curacion_valores[curacion_opcion]

        if personaje['puntos'] >= costo_vendas:
            personaje['vida'] += curacion
            if personaje['vida'] > max_vida:
                personaje['vida'] = max_vida  # No exceder la vida máxima
            personaje['puntos'] -= costo_vendas
            print(f"\nHas comprado vendas. Tu vida se ha incrementado en {curacion} puntos.")
            print(f"Ahora tienes {personaje['vida']} de vida y {personaje['puntos']} puntos restantes.")
        else:
            print("\nNo tienes suficientes puntos para comprar estas vendas.")

# Función de combate para un personaje
def combate(personaje):
    impacto = random.choice(list(puntos_impacto.keys()))
    puntos_ganados = puntos_impacto[impacto]
    personaje['puntos'] += puntos_ganados
    
    print(f"\n{personaje['nombre']} dispara con {personaje['arma']} y hace un disparo en el/la {impacto} del zombie.")
    print(f"Ganas {puntos_ganados} puntos.")

# Función para ataque del zombie
def ataque_zombie(personaje):
    ataque = random.choice(list(ataques.keys()))
    danio = ataques[ataque]
    personaje['vida'] -= danio

    print(f"¡El zombie ataca a {personaje['nombre']} con un {ataque} y causa {danio} de daño!")
    if personaje['vida'] <= 0:
        personaje['vida'] = 0  # Asegurarse de que la vida no sea negativa
        print(f"{personaje['nombre']} ha sido derrotado por el zombie.")

# Función para mostrar el historial de personajes
def mostrar_historial(historial_personajes):
    print("\nHistorial de los jugadores:")
    for personaje in historial_personajes:
        print(f"Nombre: {personaje['nombre']}, Clase: {personaje['clase']}, Vida: {personaje['vida']}, Arma: {personaje['arma']}, Puntos Finales: {personaje['puntos']}")
