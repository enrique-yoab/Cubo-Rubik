from components.function_cube import*

def move_F_left(cube):
    #se mueve la cara principal, a la izquierda 0 y el color principal es 2 que es el blanca
    cube = move_face(cube,0,2)
    #se agregan las 4 caras que se modifican al rotar
    #red, blue, green, orange
    #0, 1, 3, 5
    c0, c1, c3, c5 = cube[0], cube[1], cube[3], cube[5]
    
    #obtenemos los renglones afectados de la cara roja
    #obtenemos el renglon afectado de la cara orange
    ren0 = []
    ren5 = []
    ren1 = []
    ren3 = []
    for i in range(2,-1,-1):
        ren0.append(c0[2][i]) #rojo
        ren5.append(c5[0][i]) #naranja
    #obtenemos la columna de la cara azul
    for i in range(len(c3)):
        ren1.append(c1[i][2]) #azul
        ren3.append(c3[i][0]) #verde
    #modificamos la caras
    for i in range(len(c5)):
        c3[i][0] = ren5[i]
        c5[0][i] = ren1[i]
        c1[i][2] = ren0[i]
        c0[2][i] = ren3[i]
    
    #actualizamos las caras
    cube[0] = c0
    cube[1] = c1
    cube[3] = c3
    cube[5] = c5
    
    return cube

def move_R_left(cube):
    #se rota la cara verde ya que ahora es la cara principal
    #se rota a la izquierda 0 y el color es 3 para verde
    cube = move_face(cube,0,3)
    #se agregan las 4 caras que se modifican al rotar
    #red, white, yellow, orange
    #0, 2, 4, 5
    c0, c2, c4, c5 = cube[0], cube[2], cube[4], cube[5]
    
    ren0, ren2, ren4, ren5 = [],[],[],[]
    
    #obtenemos las columandas afectadas white y orange
    for i in range(3):
        ren0.append(c0[i][2])
        ren2.append(c2[i][2])
        
    #obtenemos las columnas afectas pero invertidas red, yellow
    for i in range(2,-1,-1):
        ren4.append(c4[i][0])
        ren5.append(c5[i][2])
        
    #actulizamos las caras
    for i in range(3):
        c0[i][2] = ren4[i]
        c2[i][2] = ren0[i]
        c4[i][0] = ren5[i]
        c5[i][2] = ren2[i]

    cube[0] = c0
    cube[2] = c2
    cube[4] = c4
    cube[5] = c5
    
    return cube
    
def move_U_left(cube):
    #se rota la cara roja ya que ahora es la principal
    #se rota a la izquierda 0 y el color es 0 para rojo
    cube = move_face(cube,0,0)
    
    #se obtienen las 4 caras que se afectan al rotar
    #blue, white, green, yellow
    #1, 2 , 3 , 4
    c1, c2, c3, c4 = cube[1], cube[2], cube[3], cube[4]
    
    ren1, ren2, ren3, ren4 = [],[],[],[]
    
    for i in range(3):
        ren1.append(c1[0][i])
        ren2.append(c2[0][i])
        ren3.append(c3[0][i])
        ren4.append(c4[0][i])
    
    for i in range(3):
        c1[0][i] = ren4[i]
        c2[0][i] = ren1[i]
        c3[0][i] = ren2[i]
        c4[0][i] = ren3[i]
    
    cube[1] = c1
    cube[2] = c2
    cube[3] = c3
    cube[4] = c4
    
    return cube

def move_B_left(cube):
    #se rota la cara amarilla ya que ahora es la principal
    #se rota a la izquierda 0 y el color es 4 para amarillo
    cube = move_face(cube,0,4)
    #se obtienen las 4 caras que afecta le rotamiento
    #red, blue, green, orange
    #0, 1, 3 , 5
    c0, c1, c3, c5= cube[0], cube[1], cube[3], cube[5]
    ren0, ren1, ren3, ren5 = [],[],[],[]
    
    for i in range(3):
        ren0.append(c0[0][i])
        ren5.append(c5[2][i])

    for i in range(2,-1,-1):
        ren1.append(c1[i][0])
        ren3.append(c3[i][2])    
        
    for i in range(3):
        c0[0][i] = ren1[i]
        c1[i][0] = ren5[i]
        c3[i][2] = ren0[i]
        c5[2][i] = ren3[i]
        
    cube[0] = c0
    cube[1] = c1
    cube[3] = c3
    cube[5] = c5
    
    return cube

def move_L_left(cube):
    #se rota la cara azul ya que ahora es la principal
    #se rota a la izquierda 1 y el color es 1 para azul
    cube = move_face(cube,0,1)
    #se obtienen las caras que afectan la rotacion
    #red, white, orange, yellow
    #0,2,4,5
    c0,c2,c4,c5 = cube[0], cube[2], cube[4], cube[5]
    ren0, ren2, ren4, ren5 = [],[],[],[]
    
    for i in range(2,-1,-1):
        ren0.append(c0[i][0])
        ren4.append(c4[i][2])
    
    for i in range(3):
       ren2.append(c2[i][0])
       ren5.append(c5[i][0]) 
       
    for i in range(3):
        c0[i][0] = ren2[i]
        c2[i][0] = ren5[i]
        c4[i][2] = ren0[i]
        c5[i][0] = ren4[i]

    cube[0] = c0
    cube[2] = c2
    cube[4] = c4
    cube[5] = c5
    
    return cube

def move_D_left(cube):
    #se rota la cara naranja ya que ahora es la principal
    #se rota a la izquierda 0 y el color es 5 para naranja
    cube = move_face(cube,0,5)
    #se obtienen las caras afectadas por la rotacion
    #blue, white, green, yellow
    #1, 2, 3, 4
    c1, c2, c3, c4 = cube[1], cube[2], cube[3], cube[4]
    ren1, ren2, ren3, ren4 = [],[],[],[]
    
    for i in range(3):
        ren1.append(c1[2][i])
        ren2.append(c2[2][i])
        ren3.append(c3[2][i])
        ren4.append(c4[2][i])
    
    for i in range(3):
        c1[2][i]=ren2[i]
        c2[2][i]=ren3[i]
        c3[2][i]=ren4[i]
        c4[2][i]=ren1[i]
    
    cube[1] = c1
    cube[2] = c2
    cube[3] = c3
    cube[4] = c4
    
    return cube