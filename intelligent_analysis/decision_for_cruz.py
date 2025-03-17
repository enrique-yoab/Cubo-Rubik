from components.movements_right import*
from components.movements_left import*
from components.function_cube import movement_of_cube, move_face
from intelligent_analysis.smart_search_for_cruz import*

#En esta seccion sera para definir la mejor jugada para crear la cruz
#copy_cube es la copia del cubo pero blanqueda 
def best_game(copy_cube, cruz_blanca, faltante):
    # Almacén de las jugadas hechas
    almacen = []

    if depth_search(faltante):
        print("Se formó la cruz")
        return almacen
    else:
        # Se tienen las caras iniciales que tienen los centros
        # Se obtiene el número de jugadas, la cara, la posición del centro y cuántos faltan por alinearse
        jugada, color, lugar, sobrante = search_play(copy_cube, cruz_blanca)
        """print("---------------------------------------" * (len(jugada) + 1))
        print(f"Falta {sobrante} centros por ordenar")
        print("Las jugadas son: ", jugada)
        print("El color de las jugadas son: ", color)
        print("Las posiciones del centro están en: ", lugar)
        print("---------------------------------------" * (len(jugada) + 1))"""

        # Ordenar las jugadas según el orden deseado: caras 0 y 5, luego 1 y 3, y finalmente 4
        orden_caras = [0, 5, 1, 3, 4]  # Orden de prioridad de las caras
        jugadas_ordenadas = []
        colores_ordenados = []
        lugares_ordenados = []

        for cara in orden_caras:
            for i in range(len(color)):
                if color[i] == cara:
                    jugadas_ordenadas.append(jugada[i])
                    colores_ordenados.append(color[i])
                    lugares_ordenados.append(lugar[i])

        # Simular los movimientos en el orden deseado
        movimientos = jugada_clasificada(jugadas_ordenadas, colores_ordenados, lugares_ordenados)
        huecos_disp = centro_disponible(copy_cube[2])

        if jugadas_ordenadas[0] == 1:  # Movimiento para 1 jugada
            print("Movimientos de 1 jugada")
            for i in range(len(jugadas_ordenadas)):
                print("Los centros disponibles son:", huecos_disp)
                principal = centro_principal(colores_ordenados[i], lugares_ordenados[i])
                if principal in huecos_disp:
                    print(f"---- La cara principal del color {colores_ordenados[i]}, de la posición {lugares_ordenados[i]} es: {principal} y está disponible")
                    almacen.append(movimientos[i])
                    huecos_disp.remove(principal)
                else:
                    print("Y no está disponible, busca un lugar disponible y agregamos más movimientos")
                    # Enviamos su movimiento principal ya que solamente es 1
                    # Y estos no tienen su lugar disponible, enviamos los huecos disponibles, el color que analizamos
                    # Y su unico movimiento a realizar
                    mov_extra, huecos_disp = mov_extra_para_uno(movimientos[i], colores_ordenados[i], lugares_ordenados[i], huecos_disp)
                    for k in range(len(mov_extra)):
                        almacen.append(mov_extra[k])
                    print(f"Para el movimiento {i + 1} bloqueado se agregaron {len(mov_extra)}")
                    break #Solo un movimiento

        elif jugadas_ordenadas[0] == 2:  # Movimiento para 2 jugadas
            print("Movimientos de 2 jugadas")
            for i in range(len(jugadas_ordenadas)):
                print("Los centros disponibles son:", huecos_disp)
                principal = centro_principal(colores_ordenados[i], lugares_ordenados[i])
                if principal in huecos_disp:
                    print(f"---- La cara principal del color {colores_ordenados[i]}, de la posición {lugares_ordenados[i]} es: {principal} y está disponible")
                    # Agregar los 2 movimientos principales
                    almacen.append(movimientos[i * 2])       # Primer movimiento
                    almacen.append(movimientos[i * 2 + 1])  # Segundo movimiento
                    huecos_disp.remove(principal)            # Eliminar el centro ocupado
                else:
                    print(f"---- La cara principal del color {colores_ordenados[i]}, de la posición {lugares_ordenados[i]} es: {principal} y NO está disponible")
                    # Agregar movimientos adicionales para liberar el centro principal
                    mov_extra, huecos_disp = mov_extra_para_dos(movimientos[i * 2], movimientos[i * 2 + 1], colores_ordenados[i], lugares_ordenados[i], huecos_disp)
                    for movimiento in mov_extra:
                        almacen.append(movimiento)
                    print(f"---- Movimientos adicionales agregados: {len(mov_extra)}")
                    break #Solo un movimiento

    if len(huecos_disp) == 0:
        print("Formaste la cruz")
    else:
        print("Los huecos disponibles que quedan son:", huecos_disp)
        
    return almacen

def mov_extra_para_dos(movimiento1, movimiento2, color, lugar, lugares_disponibles):
    """
    Define los movimientos extra para las posiciones disponibles cuando los movimientos principales estan bloqueados
    """
    movimientos_extra = []
    principal = centro_principal(color, lugar)
    print(f"La cara principal del color {color}, de la posicion {lugar} es: {principal} y no esta disponible")
    
    for (i, j) in lugares_disponibles:
        if color == 0: #Cara roja
            #Centro principal (1,2) #Ultima Columna
            if lugar == 0: #renglon superior
                if i == 0 and j == 1: #Centro del renglon superior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                    
                elif i == 2 and j == 1: #Centro del renglon inferior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                    
                elif i == 1 and j == 0: #Centro de la primera columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
            #centro principal (1,0) #Primera Columna
            elif lugar == 1: #renglon inferior
                if i == 0 and j == 1: #Centro del renglon superior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                    
                elif i == 2 and j == 1: #Centro del renglon inferior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #Centro de la ultima columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
        elif color == 1:
            #Centro principal (2,1) #renglon inferior
            if lugar == 2: #Primera Columna
                if i == 1 and j == 2: #Centro en la ultima columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_L_right)
                    lugares_disponibles.remove((i,j))
                elif i == 0 and j == 1: #Centro en el renglon superior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_L_right)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 0: #Centro en la primera columna
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_L_right)
                    lugares_disponibles.remove((i,j))
            #Centro principal (0,1) #renglon superior
            elif lugar == 3: #Ultima columna
                if i == 1 and j == 0: #Centro en la primera columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #Centro en la ultima columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                elif i == 2 and j == 1: #Centro en el renglon inferior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                    
        elif color == 3: #Cara verde
            #Centro principal (0,1) renglon superior
            if lugar == 2: #Primera columna
                if i == 1 and j == 0: #El centro en la primera columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #El centro en la ultima columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                elif i == 2 and j == 1: #El centro en el renglon inferior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right) 
                    lugares_disponibles.remove((i,j))
                        
            #Centro principal (2,1) #Renglon inferior
            elif lugar == 3: #Ultima columna
                if i == 1 and j == 0: #El centro en la primera columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_R_left)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #El centro en la ultima columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 0 and j == 1: #El centro en el renglon superior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_R_left)
                    lugares_disponibles.remove((i,j))
                
        elif color == 5: #Cara naranja
            #centro principal (1,2) #ultima columna
            if lugar == 0: #renglon superior
                if i == 2 and j == 1 : #El centro en el renglon inferior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                elif i == 0 and j == 1 : #El centro en el renglon superior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 0 : #El centro en la primera columna
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
            #Centro principal (1,0) #primera columna
            elif lugar == 1: #columna inferior
                if i == 2 and j == 1: #El centro en el renglon inferior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 0 and j == 1: #El centro en el renglon superior
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #El centro en la ultima columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_D_left)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                    
        elif color == 4: #Cara amarillo
            #Centro principal (0,1) renglon superior
            if lugar == 0: #Renglon superior
                if  i == 1 and j == 0 : #El centro en la primera columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #El centro en la ultima columna
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                elif i == 2 and j == 1: #el centro en el renglon inferior
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
            #Centro principal (2,1) #Renglon inferior
            elif lugar == 1: #Renglon inferior
                if i == 1 and j == 0 : #El centro en la primera columna
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #El centro en la ultima columna 
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 0 and j == 1: #El centro en el renglon superior
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
            #Centro principal (1,2) #Ultima columna
            elif lugar == 2: #Primera columna
                if i == 0 and j == 1: #El centro en el renglon superior
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 2 and j == 1: #El centro en el renglon inferior
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_R_right)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 0: #El centro en la primera columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
            #Centro principal (1,0) #Primera columna
            elif lugar == 3:#Ultima columna
                if i == 0 and j == 1: #El centro en el renglon superior
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_right)
                    lugares_disponibles.remove((i,j))
                elif i == 2 and j == 1: #El centro en el renglon inferior
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))
                elif i == 1 and j == 2: #El centro en la ultima columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento1)
                    movimientos_extra.append(movimiento2)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    lugares_disponibles.remove((i,j))

    #Retornamos la lista de movimientos extras
    return movimientos_extra, lugares_disponibles

#este bloque define los movimientos extra para las posiciones disponibles
#ya que su movimiento principal esta bloqueado por otro centro
#este es solo para los que realizan 1 solo movimiento
def mov_extra_para_uno(movimiento, color, lugar, lugares_disponibles):
    """
    Define los movimientos extra para las posiciones disponibles cuando el movimiento principal está bloqueado.
    """
    movimientos_extra = []
    principal = centro_principal(color, lugar)
    print(f"La cara principal del color {color}, de la posicion {lugar} es: {principal} y no esta disponible")

    for (i, j) in lugares_disponibles:
        # Las caras roja (0) y naranja (5) tienen sus centros principales en la misma posición, por lo que comparten la misma lógica.
        # Usamos break para detener el bucle una vez que se encuentra una posición disponible.
        if color == 0 or color == 5:  # Cara roja o Cara Naranja
            #(1,0) centro principal
            if lugar == 2:  # Primera columna
                if i == 0 and j == 1:  # Centro del renglón superior
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_right)
                    break
                elif i == 2 and j == 1:  # Centro del renglón inferior
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_left)
                    break
                elif i == 1 and j == 2:  # Centro en la última columna
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    break
            #(1,2) centro principal
            elif lugar == 3:  # Última columna
                if i == 0 and j == 1:  # Centro del renglón superior
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_left)
                    break
                elif i == 2 and j == 1:  # Centro del renglón inferior
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_right)
                    break
                elif i == 1 and j == 0:  # Centro en la primera columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    break

        # Las caras azul (1) y verde (3) tienen sus centros principales en la misma posición, por lo que comparten la misma lógica.
        elif color == 1 or color == 3:  # Cara azul o Cara Verde 
            #(0,1) centro principal
            if lugar == 0:  # Renglón superior
                if i == 1 and j == 0:  # Centro en la primera columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_left)
                    break
                elif i == 1 and j == 2:  # Centro en la última columna
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_right)
                    break
                elif i == 2 and j == 1:  # Centro en el renglón inferior
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    break
            #(2,1) centro principal
            elif lugar == 1:  # Renglón inferior
                if i == 1 and j == 0:  # Centro en la primera columna
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_right)
                    break
                elif i == 1 and j == 2:  # Centro en la última columna
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_left)
                    break
                elif i == 0 and j == 1:  # Centro en el renglón superior
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(move_F_left)
                    movimientos_extra.append(movimiento)
                    movimientos_extra.append(move_F_right)
                    movimientos_extra.append(move_F_right)
                    break
    #borro la posicion que encontro y regresa a su estado original
    lugares_disponibles.remove((i,j))
    # Agregamos el movimiento original al final

    # Devolvemos la lista de movimientos adicionales
    return movimientos_extra, lugares_disponibles
            

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
    """print(str(pesos) + (" <--Este son los pesos"))
    print(str(categorias) + (" <--Este son los colores"))
    print(str(posiciones) + (" <--Esta son las posiciones"))"""
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
        