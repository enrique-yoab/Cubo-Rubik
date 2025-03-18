from components.movements_left import*
from components.movements_right import*

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
    centros_cruz = [       # (centro blanco), (centro caras)
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
    # Obtenemos las caras individuales para saber que color adyacente tienen
    caras_desalineadas = []
    cara_0, cara_1, cara_2, cara_3, cara_5 = copy_cube[0], copy_cube[1], copy_cube[2], copy_cube[3], copy_cube[5]
    """print("Observamos los centros desalineados")
    print(desalineados)
    show_cube(copy_cube)"""
    #Categorizamos renglon superior = 0, renglon inferior = 1, primera columna = 2, ultima columna = 3
    #Se observa que cada lado tiene una cara por lo que podemos identificar que movimientos realizar y acomodarlo a su cara correspondiente
    primera_columna, ultima_columna, renglon_inferior, renglon_superior = None, None, None, None
    for centro_blanco, cara in desalineados:
        # Primera columna CARA BLANCA , Ultima columna CARA AZUL
        if centro_blanco == (1,0) and cara == (1,2):
            primera_columna = cara_1[1][2] # Obtenemos el color de la cara adyacente
                
        # Ultima columna cara BLANCA , Primera columna CARA VERDE
        elif centro_blanco == (1,2) and cara == (1,0): 
            ultima_columna = cara_3[1][0] # Obtenemos el color de la cara adyacente
                
        # Renglon inferior CARA BLANCA , Renglon superior CARA NARANJA
        elif centro_blanco == (2,1) and cara == (0,1):
            renglon_inferior = cara_5[0][1] # Obtenemos el color de la CARA adyacente
                
        # Renglon superior CARA BLANCA , Renglon inferior CARA ROJA
        elif centro_blanco == (0,1) and cara == (2,1):
            renglon_superior = cara_0[2][1] # Obtenemos el color de la cara adyacente
    
    #Los nombres de renglo, y columna son de la cara blanca, al tener el color podemos saber a donde moverlo
    caras_desalineadas.append(renglon_superior)  #indice 0
    caras_desalineadas.append(renglon_inferior)  #indice 1
    caras_desalineadas.append(primera_columna)   #indice 2
    caras_desalineadas.append(ultima_columna)    #indice 3
    jugada = acomoda(copy_cube,caras_desalineadas)
    print(f"El numero de jugadas es {len(jugada)}")
    for i in range(len(jugada)):
        copy_cube = movement_of_cube(jugada[i],copy_cube)
        
    return copy_cube
    
def acomoda(copy_cube, caras_desalineadas):
    print("Las caras desalineadas son ", caras_desalineadas)
    # i = 0 , renglon superior
    # i = 1 , renglon inferior
    # i = 2 , primera columna
    # i = 3 , ultima columna
    posible_mov = []
    posicion = []
    color = []
    for i in range(len(caras_desalineadas)):
        cara_adyacente = caras_desalineadas[i]
        if cara_adyacente is not None:
            posicion.append(i)
            color.append(cara_adyacente)
    
    print(posicion)
    print(color)
    
    if len(posicion) == 2: #Si son 2 movimientos
        if posicion[0] == 0 and posicion[1] == 1 : # Renglon superior, Renglon inferior
            if color[0] == 'O' and color[1] == 'R':
                posible_mov.append(move_U_right)
                posible_mov.append(move_F_right)
                posible_mov.append(move_F_right)
                posible_mov.append(move_U_left)
                posible_mov.append(move_F_left)
                posible_mov.append(move_F_left)
                return posible_mov
        elif posicion[0] == 0 and posicion[1] == 2 : # Renglon superior, primera columna
            if color[0] == 'B' and color[1] == 'R':
                posible_mov.append(move_U_right)
                posible_mov.append(move_F_right)
                posible_mov.append(move_U_left)
                posible_mov.append(move_F_left)
                posible_mov.append(move_U_right)
                return posible_mov
        elif posicion[0] == 0 and posicion[1] == 3 : # Renglon superior , ultima columna
            if color[0] == 'G' and color[1] == 'R':
                posible_mov.append(move_U_left)
                posible_mov.append(move_F_left)
                posible_mov.append(move_U_right)
                posible_mov.append(move_F_right)
                posible_mov.append(move_U_left)
                return posible_mov
        elif posicion[0] == 1 and posicion[1] == 2: # Renglon inferior, primera columna
            if color[0] == 'B' and color[1] == 'O':
                posible_mov.append(move_L_left)
                posible_mov.append(move_F_right)
                posible_mov.append(move_L_right)
                posible_mov.append(move_F_left)
                posible_mov.append(move_L_left)
                return posible_mov
        elif posicion[0] == 1 and posicion[1] == 3: # Renglon inferior, ultima columna
            if color[0] == 'G' and color[1] == 'O':
                posible_mov.append(move_R_right)
                posible_mov.append(move_F_left)
                posible_mov.append(move_R_left)
                posible_mov.append(move_F_right)
                posible_mov.append(move_R_right)
                return posible_mov
        elif posicion[0] == 2 and posicion[1] == 3 : #Primera Columna, ultima columna
            if color[0] == 'G' and color[1] == 'B':
                posible_mov.append(move_R_right)
                posible_mov.append(move_F_left)
                posible_mov.append(move_F_left)
                posible_mov.append(move_R_left)
                posible_mov.append(move_F_right)
                posible_mov.append(move_F_right)
                posible_mov.append(move_R_right)
                return posible_mov
    else:
        print("Fueron 3 centros desalineados no hay movimiento para eso")
        
