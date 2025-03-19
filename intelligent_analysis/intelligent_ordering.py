from components.movements_left import*
from components.movements_right import*
from components.movements_esquina import*
from components.function_cube import show_cube, num_esquinas_alienadas

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
 
 
# ----------------------------------------SECCION DE ESQUINAS----------------------------------------------   
def identificar_esquinas(copy_cube):
    """
    Identifica las esquinas de la primera capa (cara blanca) y la última capa (cara amarilla).
    
    :param copy_cube: Una copia del cubo actual.
    :return: Lista de esquinas frontales y traseras con sus colores.
    """
    # Obtenemos las caras individuales
    cara0, cara1, cara2, cara3, cara4, cara5 = (
        copy_cube[0], copy_cube[1], copy_cube[2], copy_cube[3], copy_cube[4], copy_cube[5]
    )
    
    # Diccionario de esquinas frontales (cara blanca)
    esquinas_frontales = [
        # Esquina frontal superior izquierda (blanca, roja, azul)
        {
            "valor": "FSI", #Frontal Superio Izquierda
            "colores": [cara2[0][0], cara0[2][0], cara1[0][2]]
        },
        # Esquina frontal superior derecha (blanca, roja, verde)
        {
            "valor": "FSD", #Frontal Superior Derecha
            "colores": [cara2[0][2], cara0[2][2], cara3[0][0]]
        },
        # Esquina frontal inferior izquierda (blanca, naranja, azul)
        {
            "valor": "FII", # Frontal Inferio Izquierda
            "colores": [cara2[2][0], cara5[0][0], cara1[2][2]]
        },
        # Esquina frontal inferior derecha (blanca, naranja, verde)
        {
            "valor": "FID", #Frontal Inferior Derecha
            "colores": [cara2[2][2], cara5[0][2], cara3[2][0]]
        }
    ]
    
    # Diccionario de esquinas traseras (cara amarilla)
    esquinas_traseras = [
        # Esquina trasera superior izquierda (amarilla, roja, verde)
        {
            "valor": "TSI", #Trasera Superior Izquierda
            "colores": [cara4[0][0], cara0[0][2], cara3[0][2]]
        },
        # Esquina trasera superior derecha (amarilla, roja, azul)
        {
            "valor": "TSD", #Trasera Superior Derecha
            "colores": [cara4[0][2], cara0[0][0], cara1[0][0]]
        },
        # Esquina trasera inferior izquierda (amarilla, naranja, verde)
        {
            "valor": "TII", #Trasera Inferior Izquierda
            "colores": [cara4[2][0], cara5[2][2], cara3[2][2]]
        },
        # Esquina trasera inferior derecha (amarilla, naranja, azul)
        {
            "valor": "TID", #Trasera Inferior Derecha
            "colores": [cara4[2][2], cara5[2][0], cara1[2][0]]
        }
    ]
    #retornamos el diccionario con las esquinas
    return esquinas_frontales, esquinas_traseras
    
def buscar_esquinas(copy_cube):
    #Se regresa el diccionario
    frontales, traseras = identificar_esquinas(copy_cube)
    """    # Mostrar las esquinas frontales
    print("Esquinas frontales (cara blanca):")
    for esquina in frontales:
        print(f"{esquina['valor']} : {esquina['colores']}")
    
    # Mostrar las esquinas traseras
    print("\nEsquinas traseras (cara amarilla):")
    for esquina in traseras:
        print(f"{esquina['valor']} : {esquina['colores']}")"""
    
    # Buscar esquinas con 'W', 'R' y 'B'
    esquinas_WRB = []
    lado_cara_WRB = []
    for esquina in frontales + traseras:  # Combinar frontales y traseras
        if all(color in esquina['colores'] for color in ['W', 'R', 'B']):
            esquinas_WRB.append(esquina['valor'])
            lado_cara_WRB.append(esquina['colores'])
    
    # print("Las esquinas con 'W', 'R' y 'B' están en : ", esquinas_WRB)
    # print("Sus colores son : ", lado_cara_WRB)
    
    # Buscar esquinas con 'W', 'R', 'G'
    esquinas_WRG = []
    lado_cara_WRG = []
    for esquina in frontales + traseras:  # Combinar frontales y traseras
        if all(color in esquina['colores'] for color in ['W', 'R', 'G']):
            esquinas_WRG.append(esquina['valor'])
            lado_cara_WRG.append(esquina['colores'])
            
    # print("Las esquinas con 'W', 'R' y 'G' están en : ", esquinas_WRG)
    # print("Sus colores son : ", lado_cara_WRG)
    
    # Buscar esquinas con 'W', 'O', 'B'
    esquinas_WOB = []
    lado_cara_WOB = []
    for esquina in frontales + traseras:  # Combinar frontales y traseras
        if all(color in esquina['colores'] for color in ['W', 'O', 'B']):
            esquinas_WOB.append(esquina['valor'])
            lado_cara_WOB.append(esquina['colores'])
            
    # print("Las esquinas con 'W', 'O' y 'B' están en : ", esquinas_WOB)
    # print("Sus colores son : ", lado_cara_WOB)
    
        # Buscar esquinas con 'W', 'O', 'G'
    esquinas_WOG = []
    lado_cara_WOG = []
    for esquina in frontales + traseras:  # Combinar frontales y traseras
        if all(color in esquina['colores'] for color in ['W', 'O', 'G']):
            esquinas_WOG.append(esquina['valor'])
            lado_cara_WOG.append(esquina['colores'])
            
    # print("Las esquinas con 'W', 'O' y 'G' están en : ", esquinas_WOG)
    # print("Sus colores son : ", lado_cara_WOG)
    
    esquinas_totales = esquinas_WRB + esquinas_WRG + esquinas_WOB + esquinas_WOG
    lados_totales = lado_cara_WRB + lado_cara_WRG + lado_cara_WOB + lado_cara_WOG
    
    return esquinas_totales, lados_totales

#Si esta alineada la esquina con su esquina principal realiza estos movimientos
def esquina_alineada(esquinas, lados):
    movimientos = []
    #Confirmaciones de cada esquina
    #Almacena valores booleanos True o False
    conf_1, conf_2, conf_3, conf_4 = [], [], [], []
    
    ###Esta seccion es para analizar las esquinas alineadas con sus esquinas principales
    ###Con la diferencia de que en la cara blanca este orientada hacia arriba
    for i in range(len(esquinas)):
        extracto = lados[i]
        if esquinas[i] == 'TSD':
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'R' and j == 0:
                    conf_1.append(True)
                elif extracto[j] == 'W' and j == 1:
                    conf_1.append(True)
                elif extracto[j] == 'B' and j == 2:
                    conf_1.append(True)
                else:
                    conf_1.append(False)
            # print(conf_1)
            if all(conf_1):
                print("Esta alineada la primera esquina FSI")
                movimientos = mov_blanco_cara_superior(i)
                break
        elif esquinas[i] == 'TSI':
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'G' and j == 0:
                    conf_2.append(True)
                elif extracto[j] == 'R' and j == 1:
                    conf_2.append(True)
                elif extracto[j] == 'W' and j == 2:
                    conf_2.append(True)
                else:
                    conf_2.append(False)
            # print(conf_2)
            if all(conf_2):
                print("Esta alineada la segunda esquina FSD")
                movimientos = mov_blanco_cara_superior(i)
                break
        elif esquinas[i] == 'TID':
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'B' and j == 0:
                    conf_3.append(True)
                elif extracto[j] == 'O' and j == 1:
                    conf_3.append(True)
                elif extracto[j] == 'W' and j == 2:
                    conf_3.append(True)
                else:
                    conf_3.append(False)
            # print(conf_3)
            if all(conf_3):
                print("Esta alineada la tercera esquina FII")
                movimientos = mov_blanco_cara_superior(i)
                break
        elif esquinas[i] == 'TII':
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'O' and j == 0:
                    conf_4.append(True)
                elif extracto[j] == 'B' and j == 1:
                    conf_4.append(True)
                elif extracto[j] == 'G' and j == 2:
                    conf_4.append(True)
                else:
                    conf_4.append(False)
            # print(conf_4)
            if all(conf_4):
                print("Esta alineada la cuarta esquina FID")
                movimientos = mov_blanco_cara_superior(i)
                break
    
    if len(movimientos):
        #Se retorna los que faltan por ordenar
        sobran = num_esquinas_alienadas(esquinas,lados) 
        return movimientos, sobran
    else:
        #Se limpian
        conf_1 , conf_2, conf_3, conf_4 = [],[],[],[]        
        
        
    ###Esta seccion es para analizar las esquinas alineadas con sus esquinas principales
    ###Con la diferencia de que en la cara blanca este orientada a la derecha
    for i in range(len(esquinas)):
        extracto = lados[i]
        if esquinas[i] == 'TSD':
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'B' and j == 0:
                    conf_1.append(True)
                elif extracto[j] == 'R' and j == 1:
                    conf_1.append(True)
                elif extracto[j] == 'W' and j == 2:
                    conf_1.append(True)
                else:
                    conf_1.append(False)
            # print(conf_1)
            if all(conf_1):
                print("Esta alineada la primera esquina FSI")
                movimientos = mov_blanco_cara_derecha(i)
                break
        elif esquinas[i] == 'TSI':
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'R' and j == 0:
                    conf_2.append(True)
                elif extracto[j] == 'W' and j == 1:
                    conf_2.append(True)
                elif extracto[j] == 'G' and j == 2:
                    conf_2.append(True)
                else:
                    conf_2.append(False)
            # print(conf_2)
            if all(conf_2):
                print("Esta alineada la segunda esquina FSD")
                movimientos = mov_blanco_cara_derecha(i)
                break
        elif esquinas[i] == 'TID': #amarillo, naranja, azul
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'O' and j == 0:
                    conf_3.append(True)
                elif extracto[j] == 'W' and j == 1:
                    conf_3.append(True)
                elif extracto[j] == 'B' and j == 2:
                    conf_3.append(True)
                else:
                    conf_3.append(False)
            # print(conf_3)
            if all(conf_3):
                print("Esta alineada la tercera esquina FII")
                movimientos = mov_blanco_cara_derecha(i)
                break
        elif esquinas[i] == 'TII': #amarilla, naranja, verde
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'G' and j == 0:
                    conf_4.append(True)
                elif extracto[j] == 'O' and j == 1:
                    conf_4.append(True)
                elif extracto[j] == 'W' and j == 2:
                    conf_4.append(True)
                else:
                    conf_4.append(False)
            # print(conf_4)
            if all(conf_4):
                print("Esta alineada la cuarta esquina FID")
                movimientos = mov_blanco_cara_derecha(i)
                break

    if len(movimientos):
        #Se retorna los que faltan por ordenar
        sobran = num_esquinas_alienadas(esquinas,lados) 
        return movimientos, sobran
    else:
        #Se limpian
        conf_1 , conf_2, conf_3, conf_4 = [],[],[],[]   

    ###Esta seccion es para analizar las esquinas alineadas con sus esquinas principales
    ###Con la diferencia de que en la cara blanca este orientada hacia abajo
    
    for i in range(len(esquinas)):
        extracto = lados[i]
        if esquinas[i] == 'TSD': #amarilla, roja, azul
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'W' and j == 0:
                    conf_1.append(True)
                elif extracto[j] == 'B' and j == 1:
                    conf_1.append(True)
                elif extracto[j] == 'R' and j == 2:
                    conf_1.append(True)
                else:
                    conf_1.append(False)
            # print(conf_1)
            if all(conf_1):
                print("Esta alineada la primera esquina FSI")
                movimientos = mov_blanco_cara_trasera(i)
                break
        elif esquinas[i] == 'TSI': #amrailla, roja, verde
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'W' and j == 0:
                    conf_2.append(True)
                elif extracto[j] == 'G' and j == 1:
                    conf_2.append(True)
                elif extracto[j] == 'R' and j == 2:
                    conf_2.append(True)
                else:
                    conf_2.append(False)
            # print(conf_2)
            if all(conf_2):
                print("Esta alineada la segunda esquina FSD")
                movimientos = mov_blanco_cara_trasera(i)
                break
        elif esquinas[i] == 'TID': #amarillo, naranja, azul
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'W' and j == 0:
                    conf_3.append(True)
                elif extracto[j] == 'B' and j == 1:
                    conf_3.append(True)
                elif extracto[j] == 'O' and j == 2:
                    conf_3.append(True)
                else:
                    conf_3.append(False)
            # print(conf_3)
            if all(conf_3):
                print("Esta alineada la tercera esquina FII")
                movimientos = mov_blanco_cara_trasera(i)
                break
        elif esquinas[i] == 'TII': #amarilla, naranja, verde
            for j in range(len(extracto)):
                # print(extracto[j])
                if extracto[j] == 'W' and j == 0:
                    conf_4.append(True)
                elif extracto[j] == 'G' and j == 1:
                    conf_4.append(True)
                elif extracto[j] == 'O' and j == 2:
                    conf_4.append(True)
                else:
                    conf_4.append(False)
            # print(conf_4)
            if all(conf_4):
                print("Esta alineada la cuarta esquina FID")
                movimientos = mov_blanco_cara_trasera(i)
                break
            
    if len(movimientos):
        #Se retorna los que faltan por ordenar
        sobran = num_esquinas_alienadas(esquinas,lados) 
        return movimientos, sobran
    else:
        #Se limpian
        conf_1 , conf_2, conf_3, conf_4 = [],[],[],[]  
        sobran = num_esquinas_alienadas(esquinas, lados)    
        return [], sobran #retorna 10 ya que debe estar la esquina desalineada con su esquina principal

def alinear_esquina(esquina, lados, esquina_a_mover):
    rotar = []
    if esquina_a_mover == 0:  # Se debe alinear a la esquina TSD
        orden = ['W', 'R', 'B']
        if esquina == "FSI":  # Frontal Superior Izquierda (Cara blanca)
            if lados == orden:
                print("Ya se ordeno FSI")
                return 1, []
            else:
                rotar.append(move_L_left)
                rotar.append(move_B_right)
                rotar.append(move_L_right)
                return 0, rotar
        elif esquina == "FSD":  # Frontal Superios Derecha (Cara blanca)
            rotar.append(move_R_right)
            rotar.append(move_B_right)
            rotar.append(move_R_left)
            return 0, rotar
        elif esquina == "FII":  # Frontal Inferior Izquierda (Cara blanca)
            rotar.append(move_L_right)
            rotar.append(move_B_left)
            rotar.append(move_L_left)
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "FID":  # Frontal Inferior Derecha (Cara blanca)
            rotar.append(move_R_left)
            rotar.append(move_B_right)
            rotar.append(move_R_right)
            rotar.append(move_B_right)
            return 0, rotar
        elif esquina == "TSI":  # Trasera Superior Izquierda (Cara amarilla)
            rotar.append(move_B_right)
            return 0, rotar
        elif esquina == "TII":  # Trasera Inferior Izquierda (Cara amarilla)
            rotar.append(move_B_left)
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "TID":  # Trasera Inferior Derecha (Cara amarilla)
            rotar.append(move_B_left)
            return 0, rotar

    elif esquina_a_mover == 1:  # Se debe alinear a TSI
        orden = ['W', 'R', 'G']
        if esquina == "FSD":  # Frontal Superior Derecha
            if lados == orden:
                print("Ya esta ordenada FSD")
                return 1, []
            else:
                rotar.append(move_R_right)
                rotar.append(move_B_right)
                rotar.append(move_R_left)
                rotar.append(move_B_left)
                return 0, rotar
        elif esquina == "FSI":  # Frontal superior Izquierda
            rotar.append(move_L_left)
            rotar.append(move_B_left)
            rotar.append(move_L_right)
            return 0, rotar
        elif esquina == "FID":
            rotar.append(move_L_right)
            rotar.append(move_B_left)
            rotar.append(move_B_left)
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "FII":
            rotar.append(move_R_left)
            rotar.append(move_B_right)
            rotar.append(move_B_right)
            rotar.append(move_B_right)
            return 0, rotar
        elif esquina == "TSD":
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "TID":
            rotar.append(move_B_left)
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "TII":
            rotar.append(move_B_right)
            return 0, rotar

    elif esquina_a_mover == 2:  # Se debe alinear a TID
        if esquina == "FII":
            orden = ['W', 'O', 'B']
            if lados == orden:
                print("Ya esta alineado FSD")
                return 1, []
            else:
                rotar.append(move_L_right)
                rotar.append(move_B_left)
                rotar.append(move_L_left)
                return 0, rotar
        elif esquina == "FSI":
            rotar.append(move_L_left)
            rotar.append(move_B_right)
            rotar.append(move_L_right)
            rotar.append(move_B_right)
            return 0, rotar
        elif esquina == "FSD":
            rotar.append(move_R_right)
            rotar.append(move_B_right)
            rotar.append(move_B_left)
            rotar.append(move_B_right)
            return 0, rotar
        elif esquina == "FID":
            rotar.append(move_R_left)
            rotar.append(move_B_left)
            rotar.append(move_R_right)
            return 0, rotar
        elif esquina == "TSD":
            rotar.append(move_B_right)
            return 0, rotar
        elif esquina == "TSI":
            rotar.append(move_B_right)
            rotar.append(move_B_right)
            return 0, rotar
        elif esquina == "TII":
            rotar.append(move_B_left)
            return 0, rotar

    elif esquina_a_mover == 3:  # Se debe alinear a TII
        if esquina == "FID":
            orden = ['W', 'O', 'G']
            if lados == orden:
                return 1, []
            else:
                rotar.append(move_R_left)
                rotar.append(move_B_right)
                rotar.append(move_R_right)
                return 0, rotar
        elif esquina == "FSI":
            rotar.append(move_L_left)
            rotar.append(move_B_left)
            rotar.append(move_L_right)
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "FSD":
            rotar.append(move_R_right)
            rotar.append(move_B_left)
            rotar.append(move_R_left)
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "FII":
            rotar.append(move_L_right)
            rotar.append(move_B_right)
            rotar.append(move_L_left)
            return 0, rotar
        elif esquina == "TSI":
            rotar.append(move_B_left)
            return 0, rotar
        elif esquina == "TSD":
            rotar.append(move_B_left)
            rotar.append(move_B_left)
        elif esquina == "TID":
            rotar.append(move_B_right)
            return 0, rotar