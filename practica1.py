import random

capacidad = 30
precios = [10,8,12,6,3,2,2]
pesos = [4,2,5,5,2,1.5,1]
nombres = ['Decoy Detonators','Love Potion','Extendable Ears', 'Skiving Snackbox','Fever Fudge','Puking Pastilles','Nosebleed Nougat']
pm = 0.10
pCruza = 0.85
generaciones = 50

def crearPrimerGeneracion():
    generacion = []
    for i in range(10):
        generacion.append(creaciondeCromosoma())
    return generacion

def creaciondeCromosoma():
    condicion = True
    while condicion:
        cromosoma = [0,0,0,0,0,0,0]
        for i in range(len(cromosoma)):
            if i == 1:
                cromosoma[i] = random.randint(3,10)
            elif i == 3:
                cromosoma[i] = random.randint(2,10)
            else:
                cromosoma[i] = random.randint(0,10)
        condicion = comprobarPeso(cromosoma)
    return cromosoma

def comprobarPeso(cromosoma):
    pesoTotal = 0
    for i in range(7):
        pesoTotal = pesoTotal + pesos[i]*cromosoma[i]
    if pesoTotal > capacidad:
        return True
    else:
        return False

def obtencionPrecio(cromosoma):
    precioTotal = 0
    for i in range(len(cromosoma)):
        precioTotal = precioTotal+cromosoma[i]*precios[i]
    return precioTotal

def probabilidadSeleccion(precios):
    total = sum(precios)
    pSel = []
    for i in precios:
        pSel.append(i/total)
    return pSel

def obtenerPselAcum(poblacion):
    funcion = []
    for i in poblacion:
        funcion.append(obtencionPrecio(i))
    psel = probabilidadSeleccion(funcion)
    pAcum = []
    for i in range(len(psel)):
        if i == 0:
            pAcum.append(psel[i])
        else:
            pAcum.append(psel[i]+pAcum[i-1])
    #print(pAcum)
    return pAcum

def seleccionPadres(poblacion,pAcum):
    padres = []
    aleatorio = random.randint(0,1000)
    aleatorio = aleatorio/1000
    for i in range(len(pAcum)):
        if pAcum[i]>= aleatorio:
            selec = i
            #print(aleatorio)
           # print(f'Se selecciono el padre{i}\n')
            padres.append(poblacion[i])
            break
    loop = True
    while loop:
        aleatorio = random.randint(0,1000)
        aleatorio = aleatorio/1000
        for i in range(len(pAcum)):
            if pAcum[i]>= aleatorio:
                if i == selec:
                    break
                else:
                    #print(aleatorio)
                   # print(f'Se selecciono el padre{i}\n')
                    padres.append(poblacion[i])
                    loop = False
                    break
    return padres

def cruza(padres):
    hijos = []
    hijo1 = []
    hijo2 = []
    cromosomaDeCruza = []
    for i in range(len(padres[0])):
        aleatorio = (random.randint(0,10))/10
        cromosomaDeCruza.append(aleatorio)
        if aleatorio <= 0.5:
            hijo1.append(padres[0][i])
            hijo2.append(padres[1][i])
        else:
            hijo1.append(padres[1][i])
            hijo2.append(padres[0][i])
    #print(cromosomaDeCruza)
    hijos.append(hijo1)
    hijos.append(hijo2)
    return hijos

def mutacion(cromosoma):
    condicion = True
    pm = 0.1
    cromosomaMutacion = []
    for x in cromosoma:
        cromosomaMutacion.append((random.randint(0,100))/100)
    while condicion:
        cromosomaAux = cromosoma
        for j in range(len(cromosoma)):
            if cromosomaMutacion[j] < pm:
                if j == 1:
                    cromosomaAux[j] = random.randint(3,10)
                elif j == 3:
                    cromosomaAux[j] = random.randint(2,10)
                else:
                    cromosomaAux[j] = random.randint(0,10)
        condicion = comprobarPeso(cromosomaAux)

    #print(cromosomaMutacion)
    #print(cromosomaAux)
    return cromosomaAux
    
def reemplazoPadreMasDebil(hijos,padres):
    selec = []
    precios = []
    selec.append(hijos[0])
    selec.append(hijos[1])
    selec.append(padres[0])
    selec.append(padres[1])
    sobrevivientes = []
    for i in selec:
        precios.append(obtencionPrecio(i))
    for i in range(2):
        max = 0
        indice = 0
        for x in range(len(precios)):
            if precios[x] > max:
                max = precios[x]
                indice = x
        sobrevivientes.append(selec[indice])
        selec.pop(indice)
        precios.pop(indice)
    return(sobrevivientes)
        
    

def proceso(poblacion):
    for i in range(generaciones):
        poblacionNueva = []
        pacum = obtenerPselAcum(poblacion)
        for j in range(5):
            padres = seleccionPadres(poblacion,pacum)
            probCruza = (random.randint(0,100))/100
            if probCruza > pCruza:
                poblacionNueva.append(mutacion(padres[0]))
                poblacionNueva.append(mutacion(padres[1]))
            else:
                condicion1 = True
                condicion2 = True
                hijos = cruza(padres)
                condicion1 = comprobarPeso(hijos[0])
                condicion2 = comprobarPeso(hijos[1])
                while condicion1 or condicion2:
                    padres = seleccionPadres(poblacion,pacum)
                    hijos = cruza(padres)
                    condicion1 = comprobarPeso(hijos[0])
                    condicion2 = comprobarPeso(hijos[1])
                sobrevivientes = reemplazoPadreMasDebil(hijos,padres)
                poblacionNueva.append(mutacion(sobrevivientes[0]))
                poblacionNueva.append(mutacion(sobrevivientes[1]))
        poblacion = poblacionNueva
        #print(f'Generacion {i}')
        #print(poblacion)
    return poblacion



poblacionInicial = crearPrimerGeneracion()
print('Resultados Pob inicial')
for x in poblacionInicial:
    print(x)
    print(obtencionPrecio(x))
#print(poblacionInicial)
pobFinal = proceso(poblacionInicial)
print('Resultados')
for x in pobFinal:
    print(x)
    print(obtencionPrecio(x))
#pacum = obtenerPselAcum(poblacionInicial)
#padres = seleccionPadres(poblacionInicial,pacum)
#print(padres)
#hijos = cruza(padres)
#print('hijos')
#print(hijos)
#print('mutacion')
#mutacion(hijos[0])
#reemplazoPadreMasDebil(hijos,padres)

