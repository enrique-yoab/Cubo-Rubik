from components.function_cube import show_cube

def analizar_cruz(copy_cube):
    alineados = []
    centros_cruz = [   # (centro blanco), (centro caras)
        ((1, 0), (1, 2)),  # (Centro blanco), (centro azul)
        ((0, 1), (2, 1)),  # (centro blanco), (centro rojo)
        ((1, 2), (1, 0)),  # (Centro blanco), (centro verde)
        ((2, 1), (0, 1))   # (Centro blanco), (Centro naranja)
    ]
    # Obtenemos las caras individuales para saber si están alineados sus centros
    cara_0, cara_1, cara_2, cara_3, cara_5 = copy_cube[0], copy_cube[1], copy_cube[2], copy_cube[3], copy_cube[5]

    for ((i, j), (k, m)) in centros_cruz:
        color_blanco = cara_2[i][j]  # Centro de la cara blanca
        if (i, j) == (1, 0):  # Cara azul (1)
            color_adyacente = cara_1[k][m]
            color_esperado = 'B'
        elif (i, j) == (0, 1):  # Cara roja (0)
            color_adyacente = cara_0[k][m]
            color_esperado = 'R'
        elif (i, j) == (1, 2):  # Cara verde (3)
            color_adyacente = cara_3[k][m]
            color_esperado = 'G'
        elif (i, j) == (2, 1):  # Cara naranja (5)
            color_adyacente = cara_5[k][m]
            color_esperado = 'O'

        if color_blanco == 'W' and color_adyacente == color_esperado:
            alineados.append(((i, j), (k, m)))  # Almacenar coordenadas de los centros alineados
        else:
            continue

    if alineados:  # Verificar si la lista no está vacía
        return len(alineados)
    else:
        # No hay centros alineados
        return 0
    
    
def buscar_caras_adyacentes(copy_cube):
    alienados = []
    desalineado = []
    centros_cruz = [   # (centro blanco), (centro caras)
        ((1, 0), (1, 2)),  # (Centro blanco), (centro azul)
        ((0, 1), (2, 1)),  # (centro blanco), (centro rojo)
        ((1, 2), (1, 0)),  # (Centro blanco), (centro verde)
        ((2, 1), (0, 1))   # (Centro blanco), (Centro naranja)
    ]
    # Obtenemos las caras individuales para saber si están alineados sus centros
    cara_0, cara_1, cara_2, cara_3, cara_5 = copy_cube[0], copy_cube[1], copy_cube[2], copy_cube[3], copy_cube[5]

    for ((i, j), (k, m)) in centros_cruz:
        color_blanco = cara_2[i][j]  # Centro de la cara blanca
        if (i, j) == (1, 0):  # Cara azul (1)
            color_adyacente = cara_1[k][m]
            color_esperado = 'B'
        elif (i, j) == (0, 1):  # Cara roja (0)
            color_adyacente = cara_0[k][m]
            color_esperado = 'R'
        elif (i, j) == (1, 2):  # Cara verde (3)
            color_adyacente = cara_3[k][m]
            color_esperado = 'G'
        elif (i, j) == (2, 1):  # Cara naranja (5)
            color_adyacente = cara_5[k][m]
            color_esperado = 'O'

        if color_blanco == 'W' and color_adyacente == color_esperado:
            alienados.append(((i, j), (k, m)))  # Almacenar coordenadas de los centros alineados
        else:
            desalineado.append(((i, j), (k, m)))  # Almacenar coordenadas de los centros no alineados

    return alienados, desalineado

def reubicar_centros(copy_cube, desalineados, alineados):
    """ centros_cruz = [   # (centro blanco), (centro caras)
        ((1, 0), (1, 2)),  # (Centro blanco), (centro azul)
        ((0, 1), (2, 1)),  # (centro blanco), (centro rojo)
        ((1, 2), (1, 0)),  # (Centro blanco), (centro verde)
        ((2, 1), (0, 1))   # (Centro blanco), (Centro naranja) ]
    """
    print("Observamos los centros desalineados")
    print(desalineados)
    show_cube(copy_cube)
    