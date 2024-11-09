"""
PROPÓSITO GENERAL DEL CÓDIGO:
El código implementa un juego de combate básico entre un personaje y un zombie. El jugador puede configurar su 
personaje, atacar al zombie, defenderse de sus ataques, y realizar compras para mejorar su estado.

DESCRIPCIÓN DE LOS ARCHIVOS:

1. FUNCIONES2_0.PY:
    Este archivo contiene las funciones que definen el funcionamiento básico del juego, como la configuración de 
    personajes, el sistema de combate, y las compras.

2. MAIN.PY:
    Contiene la función principal que controla el flujo del juego.

EXPLICACIÓN DE FUNCIONES2_0.PY:

A - CONSTANTES Y DICCIONARIOS:
    Estos contienen los valores iniciales, como los tipos de personajes, las armas disponibles, y las áreas de impacto.

B - FUNCIONES CLAVE:

    - obtener_numero: Esta función valida entradas numéricas para evitar errores si el usuario ingresa valores no válidos.

    - elegir_clase_personaje: Permite al usuario seleccionar la clase del personaje y retorna la clase seleccionada con su vida inicial.

    - configurar_personaje: Crea un personaje, permitiendo elegir nombre, clase y arma. También deduce puntos de 
    acuerdo con el arma elegida y devuelve un diccionario con la información del personaje.

    - comprar: Permite al jugador comprar una nueva arma o vendas para curarse, actualizando los puntos del personaje y 
    su vida, si se han adquirido vendas.

    - combate y ataque_zombie: Simulan el ataque del personaje al zombie y viceversa. Los puntos se ajustan 
    de acuerdo con el impacto y el daño recibido.

    - mostrar_historial: Muestra un resumen de los personajes que han jugado, incluyendo su nombre, clase, vida, arma 
    y puntos finales.

EXPLICACIÓN DE MAIN.PY:

A - FLUJO DE LA FUNCIÓN JUGAR:
    La función organiza el ciclo de juego, permitiendo al usuario realizar varias acciones como combatir, ver el 
    historial, o comprar armas.

B - CICLO DE JUEGO:
    Permite que el juego continúe mientras el personaje esté vivo y el jugador quiera seguir jugando.

C - OPCIONES DEL JUGADOR:
    Después de cada turno, el jugador puede:
        - Continuar jugando con el mismo personaje.
        - Ver el historial de personajes.
        - Comprar armas o vendas.
        - Salir del juego, mostrando el historial y terminando la partida.


RESUMEN FINAL:
Ambos archivos trabajan juntos para simular el ciclo del juego: `funciones2_0.py` establece las funciones 
necesarias para el combate y el progreso del personaje, mientras que `main.py` gestiona la experiencia del 
jugador mediante el flujo principal del juego.
"""
