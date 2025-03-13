from components.function_cube import show_cube, show_face
from intelligent_analysis.decision_for_cruz import*

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
    copy_cube = cube
    #se crea la cruz blanca que es la cara principal de mi cubo
    cruz_blanca = cruz_principial('W')
    #se crea una copia de las caras del cubo y las blanqueamos
    #blanquear es quitar los colores y dejar solo el color blanco 
    caras_blanquedas = []
    for i in range(len(cube)):
        caras_blanquedas.append(cube[i])

    # Blanquear los colores y dejar el color blanco y el centro
    for i in range(len(caras_blanquedas)):
        caras_blanquedas[i] = whiten_face(caras_blanquedas[i], 'W')  # Modificar cada cara individualmente

    #imprime las caras blanqueadas
    show_face(cruz_blanca)
    print("----------------------Este es el cubo blanqueado----------------------")
    show_cube(caras_blanquedas)
    #Se crea la logica inteligente para que crea la cruz primero
    #Se busca la mejor jugada a realizar
    plays = best_game(copy_cube,caras_blanquedas, cruz_blanca)
