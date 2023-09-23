ratio = 1
# Sugerido: para 1 contratar 4
import copy

def generador_tablas(dias, ratio):
    tabla = [[0 for dia in range(dias)] for enfermero in range(4*ratio)]

    # permutar hacia atras
    config = ["D", "N", "L", "L"]

    #se parte de la primera columna
    for columna in range(dias):
        for i in range(len(config)):
            tabla[i][columna] = config[i]
        config.append(config.pop(0))
            
    return tabla

def imprimir_tabla(tabla):
    for fila in tabla:
        print(' | '.join(fila))

tabla = generador_tablas(5, 1)
imprimir_tabla(tabla)

