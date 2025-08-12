import random

class Pila:
    def __init__ (self):
        self.items = []

    def is_empty (self):
        return len(self.items) == 0
    
    def push (self, item):
            self.items.append(item)

    def pop (self):

        if not self.is_empty():
            return self.items.pop(-1)
    
    def size (self):
        return len(self.items)
    
    def peek (self):

        if not self.is_empty():
            return self.items[-1]
        else:
            return -1

        
p0 = Pila()
p1 = Pila()
p2 = Pila()
p3 = Pila()
base = [p0, p1, p2, p3]
mi_set = {0,1,2,3}

n_disks = 4
## goalPila = random.choice(list(mi_set))
goalPila = 3
posteCentro = 2

pilaAux = Pila()

# base[2].push(3)
# base[2].push(1)
# base[2].push(0)
# base[1].push(2)
for i in range(n_disks):
    r = random.randint(0,3)
    base[r].push(n_disks - i - 1)

estadoActual = []

for i in range(n_disks):
    estadoActual.append(-1)

def conocerEstadoActual(estadoActual, base):
    for i in range(3):
        while not base[i].is_empty():
            disco = base[i].pop()
            estadoActual[disco] = i
            pilaAux.push(disco)
        while not pilaAux.is_empty():
            base[i].push(pilaAux.pop())

conocerEstadoActual(estadoActual, base)

def crear_matriz(n):
    matriz = []
    for _ in range(n):
        fila = ['|', '|', '|', '|']
        matriz.append(fila)
    return matriz

matriz = crear_matriz(n_disks)

for i in range(n_disks):
    disco = n_disks - 1 - i
    posicion = estadoActual[disco]
    for j in range(n_disks):
        if matriz[n_disks - 1 - j][posicion] == '|':
            matriz[n_disks - 1 - j][posicion] = disco
            break
        
for i in range(n_disks):
    print(str(matriz[i][0]) + "  " + str(matriz[i][1]) + "  " + str(matriz[i][2]) + "  " + str(matriz[i][3]))
print("__________")

print("Hola")



goalMatrix = []

for i in range(n_disks):
    goalMatrix.append(Pila())

def set_Goal(goal, goalMatrix, tope):
    for i in range(tope):
        goalMatrix[i].push(goal)

def descartarGoal(goalMatrix, disco):
    # print(str(disco))
    goalMatrix[disco].pop()

def comparaGoalStatus(goalMatrix, disco, estadoActual):
    return goalMatrix[disco].peek() == estadoActual[disco]

def get_discoPivote(goalMatrix, n):
    maxLen = goalMatrix[0].size()
    for i in range(1,n):
        if goalMatrix[i].size()<maxLen:
            return i-1
    return n - 1

def goalDeArriba(goalMatrix, estadoActual, disco, mi_set, posteCentro):
    if estadoActual[disco] == posteCentro:
        goal = list(mi_set - {goalMatrix[disco].peek(), estadoActual[disco]})[0]
        return goal
    else:
        goal = list(mi_set - {goalMatrix[disco].peek(), estadoActual[disco], posteCentro})[0]
        return goal
    

def checkDeArriba(estadoActual, goal, tope):
    for i in range(tope):
        if estadoActual[tope - i - 1] != goal:
            return (False, tope - i - 1)
    return (True, -1)

def goalAchieved(estadoActual, goalPila):
    for i in estadoActual:
        if i != goalPila:
            return False
    return True

def det_MaxOut(estadoActual, goalPila, n_disks):
    for i in range(n_disks):
        disco = n_disks - 1 - i
        if estadoActual[disco] != goalPila:
            return disco
        
def moverDisco(goalMatrix, estadoActual, disco, base, posteCentro, n_disks):
    if estadoActual[disco] == posteCentro:
        base[goalMatrix[disco].peek()].push(base[estadoActual[disco]].pop())
        estadoActual[disco] = goalMatrix[disco].pop()
    else:
        base[posteCentro].push(base[estadoActual[disco]].pop())
        estadoActual[disco] = posteCentro
        
        matriz = crear_matriz(n_disks)

        for i in range(n_disks):
            disk = n_disks - 1 - i
            posicion = estadoActual[disk]
            for j in range(n_disks):
                if matriz[n_disks - 1 - j][posicion] == '|':
                    matriz[n_disks - 1 - j][posicion] = disk
                    break
                
        for i in range(n_disks):
            print(str(matriz[i][0]) + "  " + str(matriz[i][1]) + "  " + str(matriz[i][2]) + "  " + str(matriz[i][3]))
        print("__________")
        print("Central")
        base[goalMatrix[disco].peek()].push(base[estadoActual[disco]].pop())
        estadoActual[disco] = goalMatrix[disco].pop()

def imprimir_goalMatrix(goalMatrix, n_disks):
    for i in range(n_disks):
        print(str(goalMatrix[i].size()))
        pila_copia = Pila()
        while not goalMatrix[i].is_empty():
            pila_copia.push(goalMatrix[i].pop())
        print("Fila " + str(i) + " Largo [" + str(pila_copia.size()) + "]:", end="")
        while not pila_copia.is_empty():
            elemento = pila_copia.pop()
            print(" " + str(elemento), end="")
            goalMatrix[i].push(elemento)            
        print("")




while not goalAchieved(estadoActual, goalPila):
#    input("Presiona Enter para continuar...")
#    imprimir_goalMatrix(goalMatrix, n_disks)
    
    pivote = get_discoPivote(goalMatrix, n_disks)
#    print("El largo de fila 0 es : "+ str(goalMatrix[0].size()))
#    print("El pivote es : "+str(pivote))
#    print("El largo de fila pivote es : "+ str(goalMatrix[pivote].size()))
#    if pivote < n_disks - 1:
#        print("Y el largo de la siguiente es: "+ str(goalMatrix[pivote + 1].size()))

#    print("Estado actual:")
#    for i in estadoActual:
#        print(str(i))
    
    if goalMatrix[0].size() != 0:
        while comparaGoalStatus(goalMatrix, pivote, estadoActual):
            descartarGoal(goalMatrix, pivote)
            pivote = pivote - 1
        
    
    if pivote < 0:
        continue
    elif pivote > 0:
        if goalMatrix[0].size() == 0:
            set_Goal(goalPila, goalMatrix, n_disks)
            continue
        else:
            goal = goalDeArriba(goalMatrix, estadoActual, pivote, mi_set, posteCentro)
            inPlace, distinto = checkDeArriba(estadoActual, goal, pivote)
            if not inPlace:
                set_Goal(goal, goalMatrix, distinto + 1)
                continue
    
    moverDisco(goalMatrix, estadoActual, pivote, base, posteCentro, n_disks)

    matriz2 = crear_matriz(n_disks)

    for i in range(n_disks):
        disco = n_disks - 1 - i
        posicion = estadoActual[disco]
        for j in range(n_disks):
            if matriz2[n_disks - 1 - j][posicion] == '|':
                matriz2[n_disks - 1 - j][posicion] = disco
                break
            
    for i in range(n_disks):
        print(str(matriz2[i][0]) + "  " + str(matriz2[i][1]) + "  " + str(matriz2[i][2]) + "  " + str(matriz2[i][3]))
    print("__________")
    print("Objetivo")
#    print("Medio")

matriz2 = crear_matriz(n_disks)

for i in range(n_disks):
    disco = n_disks - 1 - i
    posicion = estadoActual[disco]
    for j in range(n_disks):
        if matriz2[n_disks - 1 - j][posicion] == '|':
            matriz2[n_disks - 1 - j][posicion] = disco
            break
        
for i in range(n_disks):
    print(str(matriz2[i][0]) + "  " + str(matriz2[i][1]) + "  " + str(matriz2[i][2]) + "  " + str(matriz2[i][3]))
print("__________")

# print("Adios")