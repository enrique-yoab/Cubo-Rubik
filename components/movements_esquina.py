from components.movements_left import*
from components.movements_right import*

def mov_blanco_cara_superior(esquina):
    mover = []
    if esquina == 0:
        mover.append(move_U_right)
        mover.append(move_B_right)
        mover.append(move_U_left)
    elif esquina == 1:
        mover.append(move_R_right)
        mover.append(move_B_right)
        mover.append(move_R_left)
    elif esquina == 2:
        mover.append(move_L_right)
        mover.append(move_B_right)
        mover.append(move_L_left)
    elif esquina == 3:
        mover.append(move_D_right)
        mover.append(move_B_right)
        mover.append(move_D_left)
    return mover

def mov_blanco_cara_derecha(esquina):
    mover = []
    if esquina == 0:
        mover.append(move_L_left)
        mover.append(move_B_left)
        mover.append(move_L_right)
    elif esquina == 1:
        mover.append(move_U_left)
        mover.append(move_B_left)
        mover.append(move_U_right)
    elif esquina == 2:
        mover.append(move_D_left)
        mover.append(move_B_left)
        mover.append(move_D_right)
    elif esquina == 3:
        mover.append(move_R_left)
        mover.append(move_B_left)
        mover.append(move_R_right)
        
    return mover

def mov_blanco_cara_trasera(esquina, lado):
    mover = []