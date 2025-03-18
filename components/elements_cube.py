from intelligent_analysis.decision_for_cruz import*
from intelligent_analysis.intelligent_ordering import*
from components.function_cube import show_cube, movement_of_cube
import copy as cp

def cruz_principial(color):
    cruz = [[color for i in range(3)] for j in range(3)]
    for i in range(0,3,2):
        for j in range(0,3,2):
            cruz[i][j] = 'E'  #las esquinas no nos importan por el momento para formar la cruz
    return cruz

def whiten_face(cara_copy,color):
    #esta funcion nos permitira quitar todos los colores excepto el que se desea acomodar
    #un blanquiamiento de mi cubo para acomodar colores
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                cara_copy[i][j] = cara_copy[i][j]
            elif cara_copy[i][j] != color:
                cara_copy[i][j] = 'E'
    return cara_copy
    

def create_cruz_in_face(cube):
    movimientos_finales = []
    copy_cube = cp.deepcopy(cube)
    #se crea la cruz blanca que es la cara principal de mi cubo
    cruz_blanca = cruz_principial('W')
    #se crea una copia de las caras del cubo y las blanqueamos
    #blanquear es quitar los colores y dejar solo el color blanco 
    caras_blanquedas = []
    for i in range(len(copy_cube)):
        caras_blanquedas.append(copy_cube[i])

    # Blanquear los colores y dejar el color blanco y el centro
    for i in range(len(caras_blanquedas)):
        caras_blanquedas[i] = whiten_face(caras_blanquedas[i], 'W')  # Modificar cada cara individualmente

    #Se crea la logica inteligente para que crea la cruz primero
    #Se busca la mejor jugada a realizar
    profundidad = 4 #son 4 centros para alinear, por lo que su profundida esta en los centros desalineados
    #agregamos un ciclo while hasta que la profundidad sea igual a 0
    while profundidad > 0:
        plays = best_game(caras_blanquedas, cruz_blanca, profundidad)
        for i in range(len(plays)):
            #print(f"La mejor jugada a realizar es {plays[i].__name__} para el cubo original")
            cube = movement_of_cube(plays[i], cube)
            copy_cube = movement_of_cube(plays[i], copy_cube)
        alineados, no_alineados = comparar_cruz(cube[2],cruz_blanca)
        profundidad = no_alineados   
        movimientos_finales.extend(plays)
        if profundidad == 0:
            print(f"---------->>>>>  EL CUBO REALIZO {len(movimientos_finales)} MOVIMIENTOS PARA ARMAR LA CRUZ  <<<<<-------------")
    #fin del ciclo while
    return cube
    ### Ultima modificacion 17/03/2025 12:50 am

def ordenar_cruz(cube):
    #Analizamos la mejor configuracion para poder hacer menos movimientos
    mejor = []
    #Realizamos una copia del cubo original
    copy_cube = cp.deepcopy(cube)
    #Se realizan los 4 tiros ya que este ultimo regresa a su estado inicial para analizar cual tiene mas alineados
    print("Se analizan las 4 posibles ordenamientos")
    for _ in range(4):
        """print(f"Movimiento {_ + 1}")
        show_cube(copy_cube)"""
        mejor.append(analizar_cruz(copy_cube))
        copy_cube = movement_of_cube(move_F_right,copy_cube)
        
    # Obtenemos la mejor configuracion
    # print("La configuracion tiene mas centros alineados es: ", mejor)
    
    # Lo guardamos en una tupla (num alineados ,num rotaciones)
    # Guardamos el que tiene mas alineados y su cantidad de rotaciones
    mejor_alineamiento = (max(mejor) , mejor.index(max(mejor)))
    
    #print("El mejor tiro es: ",mejor_alineamiento)
    #show_cube(copy_cube)
    
    #Si hay una configuracion que ya tiene las 4 centros alineados pero realizo rotaciones
    if mejor_alineamiento[0] == 4:
        #Si tiene movimientos por alinear
        if mejor_alineamiento[1] > 0:
            #Si tiene 3 movimientos, mejor que sea 1 a la izquierda
            if mejor_alineamiento[1] == 3:
                #copy_cube = movement_of_cube(move_F_left,copy_cube)
                cube = movement_of_cube(move_F_left, cube)
                print("Se alineo la cruz principal con un giro a la izquierda")
                return cube
            #Si no tiene 3 movimientos que realice sus movimientos
            else:
                for _ in range(mejor_alineamiento[1]):
                    #copy_cube = movement_of_cube(move_F_right,copy_cube)
                    cube = movement_of_cube(move_F_right,cube)
                print(f"Se alineo la cruz principal con {mejor_alineamiento[1]} movimientos a la derecha")
                return cube
        #Su estado inicial ya esta ordenado
        else:
            print("Ya estaba alineada su cruz principal")
            return cube
    #Hay menos de 4 centros alineados
    else:
        #Si hay 1 o mas movimientos para alinear
        if mejor_alineamiento[1] > 0:
            if mejor_alineamiento[1] == 3:
                #copy_cube = movement_of_cube(move_F_left,copy_cube)
                cube = movement_of_cube(move_F_left,cube)
                print("La mejor configuracion se alinea con uno a la izquierda")
            #Si no realizas los movimientos que hizo anteriormente
            else:
                for _ in range(mejor_alineamiento[1]):
                    #copy_cube = movement_of_cube(move_F_right, copy_cube)
                    cube = movement_of_cube(move_F_right,cube)
                print(f"La mejor configuracion se alineo con {mejor_alineamiento[1]} movimientos a la derecha")
                
            #obtenemos los centros desalineados y alineados        
            alin, des = buscar_caras_adyacentes(cube)
            #copy_cube = reubicar_centros(copy_cube, des, alin)
            cube = reubicar_centros(cube,des, alin)
        #Si no realiza movimientos es que su estado inicial es la mejor configuracion
        else:
            print("Su mejor configuracion ya estaba sin rotarse")
            #Se busca los centros desalineados y alineados
            alin, des = buscar_caras_adyacentes(cube)
            #copy_cube = reubicar_centros(copy_cube, des, alin)
            cube = reubicar_centros(cube,des, alin)
    
    return cube

"""def modificar_esquinas(cube):
    """