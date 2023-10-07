import random

capacidad = 30
precios = [10,8,12,6,3,2,2]
pesos = [4,2,5,5,2,1.5,1]
nombres = ['Decoy Detonators','Love Potion','Extendable Ears', 'Skiving Snackbox','Fever Fudge','Puking Pastilles','Nosebleed Nougat']

def crearPrimerGeneracion():
    generacion = []
    for i in range(10):
        generacion.append(creaciondeCromosoma())
    return generacion

def creaciondeCromosoma():
    cromosoma = [0,0,0,0,0,0,0]
    condicion = True
    while condicion:
        for i in range(7):
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
    print(pAcum)
    return pAcum

def seleccionPadres(poblacion,pAcum):



poblacionInicial = crearPrimerGeneracion()
print(poblacionInicial)
obtenerPselAcum(poblacionInicial)
