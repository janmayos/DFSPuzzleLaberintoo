# Representación del laberinto

# 0 = camino, 1 = pared
def generar_laberinto():

    maze = [
        [1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ]

    return maze



# Posición de inicio y salida
start = (0, 1)  # Coordenadas (fila, columna) de inicio
end = (3, 4)    # Coordenadas (fila, columna) de salida