from components.movements_right import*
from components.movements_left import*
from components.function_cube import movement_of_cube, move_face
from intelligent_analysis.smart_search_for_cruz import*

#En esta seccion sera para definir la mejor jugada para crear la cruz
#cube aqui es la copia del cubo que viene de la funcion create_cruz_in face
#y copy_cube es la copia del cubo pero blanqueda 
def best_game(cube, copy_cube, cruz_blanca):
    #almacen de las jugadas hechas
    almacen = []
    #Se tienen las 4 caras iniciales que tiene los centro
    #Se obtine el numero de jugadas, la cara, la posicion del centro y cuantos faltan por alinearse
    jugada, color, lugar, faltante = search_play(copy_cube, cruz_blanca)
    if depth_search(faltante):
        print("Se formo la cruz")
        return almacen
    else:
        huecos_disp = centro_disponible(copy_cube[2])
        print(f"falta {faltante} centros por ordenar")
        print("Las jugadas son: ", jugada)
        print("El color de las jugadas son: ", color)
        #columna superior = 0, columna inferior = 1, primera columna = 2, ultima columa = 3
        print("las posiciones del centro estan en: ", lugar)
        #debemos simular el tiro
        print("Los centros disponibles son :", huecos_disp)
        movimientos = jugada_clasificada(jugada, color, lugar)
        #tenemos que hacer los movimientos disponibles con los lugares disponibles
        #En este paso debe hacer un movimiento extra para mover la cara principal y alinearlo
        #Si es que esta ocupado su lugar en el centro que le corresponde
        for i in range(len(jugada)):
            principal = centro_principal(color[i],lugar[i])
            print(f"La cara principal del color {color[i]}, de la posicion {lugar[i]} es: {principal}")
            if principal in huecos_disp:
                print("Y esta disponible")
                if len(jugada) == 1:
                    almacen.append(movimientos[i])
                    return almacen
            else:
                print("Y no esta disponible")
        """if jugada[0] == 1:
            correjido = jugada_un_movimiento(movimientos, color, lugar, huecos_disp)
            almacen = almacen + correjido
        """
        return almacen

def jugada_un_movimiento(movimiento, color, lugar, disponibles):
    jugada_extra = []  # Lista para almacenar movimientos adicionales


    # Devolvemos la lista de movimientos adicionales
    return jugada_extra
            

#esta funcion ya recibe el cubo blanqueado
def search_play(copy_cube, cruz_roja):
    #buscamos los centros y el cubo esta blanqueado
    #blanquear es quitar los colores y dejar solo el color rojo 
    #quitamos duplicados para evitar comparaciones de mas
    centros = quit_duplicate(search_for_the_center(copy_cube))
    #imprimimos los centros    
    for i in range(len(centros)):
        print(f"Esta es la cara {i} que tiene en sus centros a W") 
        show_face(centros[i])
    #buscamos las mejor jugada con base a cuantos movimientos, posicion
    #y el peso que tiene
    #y la categoria es el color de la cara donde esta el juego    
    pesos, categorias, posiciones = possible_plays(centros, cruz_roja)
    print(str(pesos) + (" <--Este son los pesos"))
    print(str(categorias) + (" <--Este son los colores"))
    print(str(posiciones) + (" <--Esta son las posiciones"))
    #-------------------------------------------------------------------------
    #Creamos la logica para poder realizar los movimientos con base a la posicion en la que se encuentran 
    #crearemos un condicion que almacene el indice de cara y en donde se encuentra W
    #Ya sea el primer renglon,la primera columa, la ultima columa y el ultimo renglon
    #cada uno tendra una bandera para saber cual es cada uno
    #obtenemos los centros que falta a alinear, lo hacemos en for porque la cara principal puede estar donde sea
    for i in range(len(categorias)):
        if categorias[i] == 2:
            faltante = pesos[i]
        
    movimientos, color, lugar = min_tiro(pesos, categorias, posiciones)
    if not movimientos:
        movimientos , color, lugar = max_tiro(pesos, categorias, posiciones)
    #Retornamos los mejores movimientos osea los que nada mas se hace 1 movimientos
    #Y si no hay retornamos los de 2 movimientos (movimientos)
    #Retornamos la cara en la que esta el centro a acomodar (color)
    #Retornamos la posicion en la que esta el centro (lugar)
    #retornamos el numero de centros a alinear (faltante)
    return movimientos, color, lugar, faltante

def jugada_clasificada(pesos, categoria, posicion):
    #pesos = 1, 2   <---numero de movimientos
    #categoria = 0 ... 5  <----color de las caras
    #posicion = 0  <---renglon superior
    #posicion = 1  <---renglon inferior
    #posicion = 2  <---primera columna
    #posicion = 3  <---ultima columna
    tiro = []
    for i in range(len(pesos)):
        if pesos[i] == 1: #si es un movimiento
            if categoria[i] == 0: #cara roja
                if posicion[i] == 2: #primera columna
                    tiro.append(move_L_right)
                elif posicion[i] == 3: #ultima columna
                    tiro.append(move_R_left)
                    
            elif categoria[i] == 1: #cara azul
                if posicion[i] == 0: #primer renglon
                    tiro.append(move_U_left)
                elif posicion[i] == 1: #ultimo renglon
                    tiro.append(move_D_right)
                    
            elif categoria[i] == 3: #cara verde
                if posicion[i] == 0: #primer renglon
                    tiro.append(move_U_right)
                elif posicion[i] == 1: #ultimo renglon
                    tiro.append(move_D_left)
                    
            elif categoria[i] == 5:  #cara naranja
                if posicion[i] == 2: #primera columna
                    tiro.append(move_L_left)
                elif posicion[i] == 3: #ultima columna
                    tiro.append(move_R_right)
                    
        elif pesos[i] == 2: #si son dos movimientos
            if categoria[i] == 0: #cara roja
                tiro.append(move_U_right) #se mueve a la derecha para alinearlo a la cruz
                if posicion[i] == 0: #renglon superior
                    tiro.append(move_R_left)
                elif posicion[i] == 1: #renglon inferior
                    tiro.append(move_L_right)
                    
            elif categoria[i] == 1:# cara azul
                tiro.append(move_L_left) #se mueve a la izquierda para alinearlo a la cruz
                if posicion[i] == 2 : # primera columna
                    tiro.append(move_D_right)
                elif posicion[i] == 3 : # ultima columna
                    tiro.append(move_U_left)
                    
            elif categoria[i] == 3 : # cara verde
                tiro.append(move_R_right) #se mueve a la derecha para alinearlo a la cruz
                if posicion[i] == 2 : #primera columna
                    tiro.append(move_U_right)
                elif posicion[i] == 3 : #ultima columna
                    tiro.append(move_D_left)
                    
            elif categoria[i] == 4 : #cara amarilla
                if posicion[i] == 0 : #renglon superior
                    tiro.append(move_U_right)
                    tiro.append(move_U_right)
                elif posicion[i] == 1 : #renglon inferior
                    tiro.append(move_D_left)
                    tiro.append(move_D_left)
                elif posicion[i] == 2 : #primera columna 
                    tiro.append(move_R_left)
                    tiro.append(move_R_left)
                elif posicion[i] == 3 : #ultima columna 
                    tiro.append(move_L_right)
                    tiro.append(move_L_right)
                    
            elif categoria[i] == 5: #cara naranja
                tiro.append(move_D_right) #se mueve a la derecha para alinearlo a la cruz
                if posicion[i] == 0: #renglon superior
                    tiro.append(move_R_right)
                elif posicion[i] == 1: #renglon inferior
                    tiro.append(move_L_left)
                    
    return tiro

def centro_principal(color, lugar): 
    centros_por_jugada = (
        #((color, lugar),(renglon, columna))
        #centros principales para las jugadas de la cara roja
        ((0,0),(1,2)), 
        ((0,1),(1,0)),
        ((0,2),(1,0)),
        ((0,3),(1,2)),
        #centros principales para las jugadas de la cara azul
        ((1,0),(0,1)),
        ((1,1),(2,1)),
        ((1,2),(2,1)),
        ((1,3),(0,1)),
        #centros principales para las jugadas de la cara verde
        ((3,0),(0,1)),
        ((3,1),(2,1)),
        ((3,2),(0,1)),
        ((3,3),(2,1)),
        #centros principales para las jugadas de la cara naranja
        ((4,0),(0,1)),
        ((4,1),(2,1)),
        ((4,2),(1,2)),
        ((4,3),(1,0)),
        #centros principales para las jugadas de la cara amarilla
        ((5,0),(1,2)),
        ((5,1),(1,0)),
        ((5,2),(0,1)),
        ((5,3),(1,2)),
    )
    for jugada in centros_por_jugada:
        if jugada[0] == (color, lugar):
            return jugada[1]
        