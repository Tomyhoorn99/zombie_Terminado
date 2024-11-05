import random

# Armas y sus puntos
armas = {
    1: ("pistola", 30),
    2: ("escopeta", 50),
    3: ("ametralladora", 100)
}

# Áreas de impacto con sus puntos
impacto_puntos = {
    "cabeza": 100,
    "pecho": 50,
    "piernas": 30
}


# Función para configurar personajes
def configurar_juego():
    while True:
        try:
            num_personajes = int(input("¿Con cuantos personajes desea jugar? (1 a 4): "))
            if 1 <= num_personajes <= 4:
                break
            else:
                print("Por favor, ingresa un numero entre 1 y 4.")
        except ValueError:
            print("ERROR. Por favor ingresa un numero.")
    
    personajes = []
    for i in range(num_personajes):
        print(f"\nConfigurando personaje {i+1}:")
        nombre = input("Nombre del personaje: ")
        
        # Validar la vida entre 1 y 100
        while True:
            try:
                vida = int(input("Cantidad de vida (1 a 100): "))
                if 1 <= vida <= 100:
                    break
                else:
                    print("Por favor, ingresa un numero entre 1 y 100.")
            except ValueError:
                print("ERROR. Por favor ingresa un numero.")
        
        # Elegir el arma y descontar sus puntos del total inicial
        while True:
            try:
                print("Elige un arma:")
                for num, (arma, puntos) in armas.items():
                    print(f"{num}: {arma.capitalize()} (Costo en puntos: {puntos})")
                arma_opcion = int(input("Ingresa el numero del arma: "))
                if arma_opcion in armas:
                    arma, costo_arma = armas[arma_opcion]
                    puntos_iniciales = 100 - costo_arma  # Descontar el costo del arma de los puntos iniciales
                    break
                else:
                    print("Opción no válida. Elige entre 1, 2 o 3.")
            except ValueError:
                print("ERROR. Ingresa un numero.")
        
        # Crear personaje con puntos descontados segun el arma elegida
        personaje = {
            "nombre": nombre,
            "vida": vida,
            "puntos": puntos_iniciales,
            "arma": arma
        }
        personajes.append(personaje)
    
    return personajes



# Función de combate
def combate(personaje):
    impacto = random.choice(list(impacto_puntos.keys()))
    puntos_ganados = impacto_puntos[impacto]
    
    print(f"\n{personaje['nombre']} dispara con {personaje['arma']} y hace un disparo en el/la {impacto} del zombie.")
    print(f"Ganas {puntos_ganados} puntos.")
    
    personaje['puntos'] += puntos_ganados



# Función para mostrar el historial de personajes
def mostrar_historial(historial_personajes):
    print("\nHistorial de los jugadores:")
    for personaje in historial_personajes:
        print(f"Nombre: {personaje['nombre']}, Vida: {personaje['vida']}, Arma: {personaje['arma']}, Puntos Finales: {personaje['puntos']}")
