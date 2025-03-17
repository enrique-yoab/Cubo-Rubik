from components.function_cube import show_cube, show_face
from intelligent_analysis.decision_for_cruz import*
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

    #imprime las caras blanqueadas
    show_face(cruz_blanca)
    print("----------------------Este es el cubo blanqueado----------------------")
    show_cube(caras_blanquedas)
    #Se crea la logica inteligente para que crea la cruz primero
    #Se busca la mejor jugada a realizar
    profundidad = 4 #son 4 centros para alinear, por lo que su profundida esta en los centros desalineados
    #agregamos un ciclo while hasta que la profundidad sea igual a 0
    while profundidad > 0:
        plays = best_game(caras_blanquedas, cruz_blanca, profundidad)
        for i in range(len(plays)):
            print(f"La mejor jugada a realizar es {plays[i].__name__} para el cubo original")
            cube = movement_of_cube(plays[i], cube)
            copy_cube = movement_of_cube(plays[i], copy_cube)
        alineados, no_alineados = comparar_cruz(cube[2],cruz_blanca)
        profundidad = no_alineados   
        print(f"faltan {no_alineados} por ordenar y {alineados} estan ordenados") 
        movimientos_finales.extend(plays)
        if profundidad == 0:
            print("El cubo tiene la cruz")
            show_cube(cube)
    #fin del ciclo while
    return cube
    ### Ultima modificacion 17/03/2025 12:50 am
