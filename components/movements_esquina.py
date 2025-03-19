from components.movements_left import *
from components.movements_right import *

def mov_blanco_cara_superior(esquina):
    mover = []
    if esquina == 0:
        mover.extend([move_U_right, move_B_right, move_U_left])
    elif esquina == 1:
        mover.extend([move_R_right, move_B_right, move_R_left])
    elif esquina == 2:
        mover.extend([move_L_right, move_B_right, move_L_left])
    elif esquina == 3:
        mover.extend([move_D_right, move_B_right, move_D_left])
    return mover

def mov_blanco_cara_derecha(esquina):
    mover = []
    if esquina == 0:
        mover.extend([move_L_left, move_B_left, move_L_right])
    elif esquina == 1:
        mover.extend([move_U_left, move_B_left, move_U_right])
    elif esquina == 2:
        mover.extend([move_D_left, move_B_left, move_D_right])
    elif esquina == 3:
        mover.extend([move_R_left, move_B_left, move_R_right])
    return mover

def mov_blanco_cara_trasera(esquina):
    mover = []
    if esquina == 0:
        mover.extend([move_L_left, move_B_right, move_B_right, move_L_right, move_B_right, move_L_left, move_B_left, move_L_right])
    elif esquina == 1:
        mover.extend([move_U_left, move_B_right, move_B_right, move_U_right, move_B_right, move_U_left, move_B_left, move_U_right])
    elif esquina == 2:
        mover.extend([move_D_left, move_B_right, move_B_right, move_D_right, move_B_right, move_D_left, move_B_left, move_D_right])
    elif esquina == 3:
        mover.extend([move_R_left, move_B_right, move_B_right, move_R_right, move_B_right, move_R_left, move_B_left, move_R_right])
    return mover