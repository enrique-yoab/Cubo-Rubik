from components.function_cube import show_cube, show_face
from components.movements_left import*
from components.movements_right import*
def comparate_cruz(copy_cube, cruz):
    print

def search_for_the_center(copy_cube):
    #se crea un arreglo temporal que me almacenara la cara donde se encuentre el centro para armar la cruz
    faces = []
    centros = ((0,1),(1,0),(1,2),(2,1))
    for n in range(len(copy_cube)):
        buscando = copy_cube[n]
        for i, j in centros:
            if buscando[i][j] =='W':
                faces.append(buscando)
    #agregamos al final la cara principa, y mas adelante borramos el duplicado
    faces.append(copy_cube[2])        
    return faces
    
#esta funcion recibe las que caras que son afectadas
#la cruz blanca para comparar
#Y las categoriza para buscar la mejor jugadas
def possible_plays(faces, cruz_roja):
    peso, categoria, posicion = [], [], []  # Listas para acumular pesos, categorías y posiciones

    # Mapeo de colores a categorías
    color_to_category = {
        'R': 0,  # rojo
        'B': 1,  # azul
        'W': 2,  # blanco
        'G': 3,  # verde
        'Y': 4,  # amarillo
        'O': 5   # naranja
    }

    for i in range(len(faces)):
        temporal = faces[i]
        color_centro = temporal[1][1]  # Obtener el color del centro de la cara
        if color_centro != 'W':  # Si el centro no es blanco
            posicion_roja = play_position(temporal)  # Obtener posiciones de centros rojos
            if color_centro in color_to_category:
                cat = color_to_category[color_centro]
                posicion.extend(posicion_roja)  # Acumular posiciones
                peso_jugada = play_peso(posicion_roja, cat)  # Calcular pesos
                peso.extend(peso_jugada)  # Acumular pesos
                categoria.extend([cat] * len(peso_jugada))  # Acumular categorías
        else:
            alineados, faltante = comparar_cruz(temporal,cruz_roja)
            #se regresa los valores que coinciden y los que faltan para completar la cruz
            posicion.append(alineados)  #los que esten alineados
            peso.append(faltante)       #los que estan desalineados
            categoria.append(2)
    return peso, categoria, posicion  # Devolver listas completas

#esta funcion cataloga los centros encontrados en los renglones
#superior = 0, inferior = 1, primera columna = 2, ultima columa = 3
def play_position(face):
    posiciones = []
    posiciones_validar = (
        ((0,1),0), # renglon superior
        ((2,1),1), # renglon inferior
        ((1,0),2), # primera columna
        ((1,2),3)  # ultima columna
    )
    for (i,j), valor in posiciones_validar:
        if face[i][j] == 'W':
            posiciones.append(valor)
    return posiciones

#esta funcion nos servira para dar un peso a los renglones y columnas, para cada cara sera diferente, el peso
def play_peso(posicion_jugada, categoria):
    peso_jugada = []
    #red = 0 , blue = 1 , white = 2 , green = 3 , yellow = 4 , orange = 5
    #superior = 0, inferior = 1, primera columna = 2, ultima columa = 3
    for i in range(len(posicion_jugada)):
        #renglones superior e inferior
        if (categoria == 0 or categoria == 5 or categoria == 4) and (posicion_jugada[i] == 0 or posicion_jugada[i] == 1):
            peso_jugada.append(2) #dos movimientos para acomodarlo en la cruz
        #columna primera y ultima
        elif (categoria == 0 or categoria == 5) and (posicion_jugada[i] == 2 or posicion_jugada[i] == 3):
            peso_jugada.append(1) #1 movimiento para acomodarlo en la cruz
        #renglones superiores
        elif (categoria == 1 or categoria == 3) and (posicion_jugada[i] == 0 or posicion_jugada[i] == 1):
            peso_jugada.append(1) #un movimiento para acomodarlo en la cruz
        #columna primera y ultima
        elif (categoria == 1 or categoria == 3 or categoria == 4) and (posicion_jugada[i] == 2 or posicion_jugada[i] == 3):
            peso_jugada.append(2) #2 movimientos para acomodarlo en la cruz
            
    return peso_jugada
###ultima modificacion peso jugada

#esta funcion quitara los duplicados, de las matricez que tienen en su centro a W
def quit_duplicate(faces):
    recortado = []
    for cara in faces:
        if cara not in recortado:
            recortado.append(cara)
    return recortado

