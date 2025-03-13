from components.movements_right import*
from components.movements_left import*
from intelligent_analysis.smart_search_for_cruz import*

def depth_search(centros_faltantes):
    if centros_faltantes > 0:
        return 0  #sigue haciendo movimiento
    else:
        return 1  #ya no hagas movimientos

#En esta seccion sera para definir la mejor jugada para crear la cruz
#cube aqui es la copia del cubo que viene de la funcion create_cruz_in face
#y copy_cube es la copia del cubo pero blanqueda 
def best_game(cube, copy_cube, cruz_blanca):
    #Se tienen las 4 caras iniciales que tiene los centro
    #Se obtine el numero de jugadas, la cara, la posicion del centro y cuantos faltan por alinearse
    jugada, color, lugar, faltante = search_play(copy_cube, cruz_blanca)
    print(f"falta {faltante} centros por ordenar")
    print("Las jugadas son: ", jugada)
    print("El color de las jugadas son: ", color)
    #superior = 0, inferior = 1, primera columna = 2, ultima columa = 3
    print("las posiciones del centro estan en: ", lugar)
    #debemos simular el tiro
    #-------------------------------------------------------------------
    ###ultima actualizacion 11/03/2025 a las 12:19 am
    
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
    #Ya sea el primer renglon y la primera columa, y la ultima columa y el ultimo renglon
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

def min_tiro(pesos, categorias, posiciones): 
    mejores, color, pos= [],[],[]
    for i in range(len(pesos)):
        valor = pesos[i]
        if valor == 1 and categorias[i] != 2:
            mejores.append(valor)
            color.append(categorias[i])
            pos.append(posiciones[i])
    return mejores, color, pos

def max_tiro(pesos, categorias, posiciones):
    peores, color, pos= [],[],[]
    for i in range(len(pesos)):
        valor = pesos[i]
        if valor == 2 and categorias[i] != 2:
            peores.append(valor)
            color.append(categorias[i])
            pos.append(posiciones[i])
    return peores, color, pos