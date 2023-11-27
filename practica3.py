import copy
import random
import math
import numpy as np

numParticulas = 5
numIteraciones = 50
a = 0.8
b1 = 0.7
b2 = 1
valorMin = -5
valorMax = 5
velocidades = np.zeros((numParticulas,2))
'''gbestVal = math.inf
gbest = np.zeros((1,2))
pbestVal = np.full((numParticulas),np.inf)
pbest = np.zeros((numParticulas,2))'''

def crearParticulasIniciales():
    particulas = []
    for _ in range(numParticulas):
        particula = []
        particula.append(random.uniform(valorMin,valorMax))
        particula.append(random.uniform(valorMin, valorMax))
        particulas.append(particula)
    print(particulas)
    return particulas

def evaluarParticulas(particulas):
    particulasEvaluadas = []
    for particula in particulas:
        x = particula[0]
        y = particula[1]
        evaluacion = x**2+y**2+(25*(math.sin(x)+math.sin(y)))
        particulasEvaluadas.append(evaluacion)
    print(particulasEvaluadas)
    return particulasEvaluadas

def actualizarPbest(pBest,pBestVal,pBestActual,pBestActualVal):
    for i in range(len(pBest)):
        if pBestActualVal[i] < pBestVal[i]:
            pBest[i] = pBestActual[i]
            pBestVal[i] = pBestActualVal[i]

    return pBestActual,pBestActualVal

def actualizarGBest(gBest,gBestVal,gBestActual,gBestActualVal):
    if gBestActualVal < gBestVal:
        gBestActual = gBest
        gBestActualVal = gBestVal

    return gBestActual,gBestActualVal

def calcularVelocidades(particulas,pbest,gbest,velocidades):
    for p in range(len(particulas)):
        for componentes in range(len(particulas[0])):
            r1 = random.uniform(0,1)
            r2 = random.uniform(0,1)
            velocidades[p][componentes] = a*velocidades[p][componentes] + b1*r1*(pbest[p][componentes]-particulas[p][componentes]) + b2*r2*(gbest[componentes]-particulas[p][componentes])
    return velocidades

def actualizarParticulas(particulas,velocidades):
    for i in range(len(particulas)):
        for j in range(len(particulas[0])):
            particulas[i][j] = particulas[i][j]+velocidades[i][j]
    return particulas

def comprobarRestriccion(particulas):
    for i in range(len(particulas)):
        for j in range(len(particulas[0])):
            if particulas[i][j] < valorMin:
                particulas[i][j] = valorMin
            if particulas[i][j] > valorMax:
                particulas[i][j] = valorMax
    return particulas



            

particulasIniciales = crearParticulasIniciales()
pbestVal = evaluarParticulas(particulasIniciales)
pbest = copy.deepcopy(particulasIniciales)
gbestVal = min(pbestVal)
gbestIndex = pbestVal.index(min(pbestVal))
gbest= pbest[gbestIndex]
print(gbest)
print(gbestVal)

for i in range(5):
    velocidades = calcularVelocidades(particulasIniciales,pbest,gbest,velocidades)
    particulasIniciales = actualizarParticulas(particulasIniciales,velocidades)
    pbestActual = copy.deepcopy(particulasIniciales)
    pbestActualVal = evaluarParticulas(particulasIniciales)
    pbest, pbestVal = actualizarPbest(pbest,pbestVal,pbestActual,pbestActualVal)
    gbestAcualVal = min(pbestVal)
    gbestIndex = pbestVal.index(min(pbestVal))
    gbestActual = pbest[gbestIndex]
    gbest,gbestVal = actualizarGBest(gbest,gbestVal,gbestActual,gbestAcualVal)
    print(velocidades)
    print(particulasIniciales)

