import os

def clean_screen():
    """Limpia la terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def show_cube(cubo):
    """
    Imprime el cubo de Rubik en la terminal con una disposición similar al cubo de 2D
    """

    # Cara blanca (arriba)
    print(3*"         " + " ".join(cubo[0][0]))
    print(3*"         " + " ".join(cubo[0][1]))
    print(3*"         " + " ".join(cubo[0][2]))
    print()

    # Caras azul, roja, verde y naranja (medio)
    for i in range(3):
        fila = 19*" " + " ".join(cubo[1][i]) + "   " + \
               " ".join(cubo[2][i]) + "   " + \
               " ".join(cubo[3][i]) + "   " + \
               " ".join(cubo[4][i])
        print(fila)
    print()

    # Cara amarilla (abajo)
    print(3*"         " + " ".join(cubo[5][0]))
    print(3*"         " + " ".join(cubo[5][1]))
    print(3*"         " + " ".join(cubo[5][2]))

def crear_cruz(color):
    cara = [[color for i in range(3)] for j in range(3)]
    return cara
                    
def crear_cubo():
    cubo = []
    #white, blue, red, green, orange, yellow
    #0 , 1 , 2 , 3 , 4 , 5
    colores = ["R", "B", "W", "G", "Y", "O"]
    for i in range (6):
        cubo.append(crear_cruz(colores[i]))
    return cubo

def move_face(cube, movimiento, color):
    #La cara principal es la blanca
    #se obtiene la cara que estoy viendo o movere
    cara = cube[color]
    #se obtienen los colores de las orillas, esquinas y centros
    esquinas = [cara[0][0], cara[0][2], cara[2][2], cara[2][0]]
    centros  = [cara[0][1], cara[1][2], cara[2][1], cara[1][0]]
    #si el movimiento es 1 es a la derecha
    if movimiento == 1:
        cara[0][2]=esquinas[0]
        cara[2][2]=esquinas[1]
        cara[2][0]=esquinas[2]
        cara[0][0]=esquinas[3]
        
        cara[1][2]= centros[0]
        cara[2][1]= centros[1]
        cara[1][0]= centros[2]
        cara[0][1]= centros[3]
        cube[color] = cara
        return cube
    elif movimiento == 0: # si es 0 es a la izquierda
        cara[0][2]=esquinas[2]
        cara[2][2]=esquinas[3]
        cara[2][0]=esquinas[0]
        cara[0][0]=esquinas[1]
        
        cara[1][2]= centros[2]
        cara[2][1]= centros[3]
        cara[1][0]= centros[0]
        cara[0][1]= centros[1]
        cube[color]=cara
        return cube
    else : 
        print("No existe ese movimiento")

#funcion que llama las funciones de cada movimiento
def movement_of_cube(funcion, cube):
    return funcion(cube)

def show_face(face):
    for i in range(len(face)):
        print("\t\t\t[",end="")
        for j in range(len(face[0])):
            print(face[i][j], end=" ")
        print("]")
    print()

def num_esquinas_alienadas(esquinas, lados):
    desordenado = 0
    for i in range(len(esquinas)):
        if esquinas[i] == "FSI":
            orden = ['W', 'R', 'B']
        elif esquinas[i] == "FSD":
            orden = ['W', 'R', 'G']
        elif esquinas[i] == "FII":
            orden = ['W', 'O', 'B']
        elif esquinas[i] == "FID":
            orden = ['W', 'O', 'G']
        else:
            desordenado += 1
            continue  # Saltar esquinas desconocidas
            
        if lados[i] != orden:
            desordenado += 1
        

    return desordenado