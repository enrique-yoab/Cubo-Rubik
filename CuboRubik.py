from components.function_cube import*
from components.movements_right import*
from components.movements_left import*
from components.elements_cube import*
import random

def random_cube(cube, num):
    print(f"-----------------------Aproximadamente {num} veces-------------------\n")
    right_movement = [move_F_right,move_R_right,move_U_right, move_B_right, move_L_right, move_D_right]
    left_movement = [move_F_left,move_R_left,move_U_left, move_B_left, move_L_left, move_D_left]
    all_movement = right_movement + left_movement
    for i in range(num):
        funcion_random = random.choice(all_movement)
        cube = movement_of_cube(funcion_random,cube)
        #esta linea de codigo te muestra los n movimientos que hace
        #print(f"Se ejecuto la funcion {funcion_random.__name__}")
    return cube


"""CODIGO QUE EJECUTA TODAS LAS FUNCIONES"""
clean_screen()
print("----------------BIENVENIDO AL SIMULADOR DEL CUBO RUBIK--------------\n")
cubo_rubik = crear_cubo()
show_cube(cubo_rubik)
print("\n-----------------------Se revuelve el cubo-------------------------\n")
cubo_rubik = random_cube(cubo_rubik,1000)
show_cube(cubo_rubik)
print("\n----------------------Creamos la Cruz Blanca-------------------------\n")
cubo_rubik = create_cruz_in_face(cubo_rubik)
