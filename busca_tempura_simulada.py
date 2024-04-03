
import copy
import math
import random

import numpy as np

from grafo_matriz_adjacencias import Grafo , geraGrafoCompleto10 , geraGrafoCidades


TEMP_INICIAL = 100
ALPHA = 0.9999



class No:
    def __init__(self, estado):
        self.estado = estado
        self.heuristica = 0
        self.estadoIndex = []

def fazEstadoIndex(estado, grafo):
    estadoIndex = []
    for cidade in estado:
        index = grafo.getVertice(cidade)
        estadoIndex.append(index)
    return estadoIndex

def heuristica(estado , grafo):
    # estado será uma STRING contendo a sequência de vértices tendo A como origem e destino
    # o valor da heurística será a soma dos pesos das arestas do caminho
    # a função retorna o valor da heurística
    atual = estado[0]
    heuristica = 0
    for i in range(1, len(estado)):
        proximo = estado[i]
        heuristica += grafo.getAresta(atual, proximo)
        atual = proximo
    return heuristica


def escalonamento(tempo):
    return TEMP_INICIAL * (ALPHA ** tempo)

def sucessor_aleatorio(no):
    noAux = copy.deepcopy(no)
    posCidade = random.randint(1, no.estado.__len__() -2)
    cidade = noAux.estado[posCidade]
    noAux.estado.remove(cidade)

    posAleatoria = random.randint(1, noAux.estado.__len__() -2)
    if posAleatoria == posCidade:
        posAleatoria = random.randint(1, noAux.estado.__len__() -2)
    noAux.estado.insert(posAleatoria, cidade) 

    return noAux

def calcular_probabilidade(delta_E, temperatura):
    # Calcular o valor de e elevado a delta_E dividido pela temperatura
    return math.exp(delta_E / temperatura)

def busca_tempera_simulada(problema , grafo, limite, arquivo):
    atual = No(problema)
    atual.heuristica = heuristica(atual.estado , grafo)
    atual.estadoIndex = fazEstadoIndex(atual.estado, grafo)
    menor  = atual.heuristica
    menorEstado = copy.deepcopy(atual)
    for i in range(limite):
        arquivo.write(f"{i} | {menor} | {atual.heuristica} | {atual.estadoIndex}\n")
        
        temp = escalonamento(i) 
        if temp == 0 or atual.heuristica < menor:
            menorEstado = copy.deepcopy(atual)
            menor = atual.heuristica
        proximo = sucessor_aleatorio(atual)
        #print(proximo.estado)
        proximo.heuristica = heuristica(proximo.estado, grafo)
        proximo.estadoIndex = fazEstadoIndex(proximo.estado, grafo)
        #print("heuristica de proximo: ", proximo.heuristica)    
        DeltaE =  atual.heuristica - proximo.heuristica 
        if DeltaE > 0: 
            atual = proximo
        else:
            # Calcular a probabilidade de aceitar o estado 
            # Se a probabilidade for maior que um número aleatório, aceitar o estado
            probabilidade = calcular_probabilidade(DeltaE, temp)
            numero_aleatorio = random.random()
            if probabilidade > numero_aleatorio:
                atual = proximo
    return menorEstado



def main():
    grafo = geraGrafoCidades("grafo64.txt")
    individuo = [
    "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1", "i1", "j1", "k1", "l1", "m1", "n1", "o1", "p1", "q1", "r1", "s1", "t1",
    "u1", "v1", "w1", "x1", "y1", "z1", "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2", "i2", "j2", "k2", "l2", "m2", "n2",
    "o2", "p2", "q2", "r2", "s2", "t2", "u2", "v2", "w2", "x2", "y2", "z2", "a3", "b3", "c3", "d3", "e3", "g3", "h3", "i3",
    "j3", "k3", "l3", "m3" , "a1"
]



    # faça um geração de individuos aleatórios
    melhor = None
    menor = 999999999

    coordenadas = [
    (78, 95), (45, 11), (91, 73), (38, 18), (73, 3), (20, 71), (43, 1), (2, 27), (62, 68), (74, 5),
    (15, 31), (18, 50), (90, 64), (66, 81), (56, 48), (38, 84), (41, 43), (52, 19), (56, 37), (99, 24),
    (87, 70), (47, 27), (64, 66), (53, 36), (51, 96), (2, 74), (96, 10), (24, 27), (73, 81), (22, 28),
    (83, 24), (73, 98), (84, 7), (54, 12), (76, 6), (1, 83), (33, 45), (8, 87), (94, 65), (18, 58),
    (52, 88), (40, 25), (82, 7), (52, 63), (87, 79), (79, 9), (50, 38), (66, 81), (96, 35), (2, 80),
    (58, 82), (87, 63), (54, 88), (41, 100), (37, 70), (88, 72), (76, 57), (7, 24), (99, 95), (24, 48),
    (17, 69), (77, 24), (35, 59), (44, 51)]

    resultados = np.zeros(10)
    for i in range(10):
        with open(f'teste_{i}.txt', 'w') as arquivo:
            individuo = copy.deepcopy(individuo)
            cidade = individuo[0]
            individuo.remove(cidade)
            individuo.remove(cidade)
            random.shuffle(individuo)
            individuo.insert(0, cidade)
            individuo.append(cidade)
            arquivo.write(f"{grafo.vertices.__len__()} cidades\n")
            arquivo.write(f"{coordenadas}\n")
            resultado = busca_tempera_simulada(individuo, grafo, 100000 , arquivo)
            resultados[i] = resultado.heuristica
            #print(resultado.heuristica)
            if resultado.heuristica < menor:
                menor = resultado.heuristica
                melhor = resultado
    print(menor)
    print(resultados.max())
    print(resultados.mean())
        

    
    #print (heuristica(atual, grafo))
    #print("O menor caminho é: ", melhor.estado)
    #print ("O valor da heurística é: ", melhor.heuristica)
    """while True:
        sucessor = sucessor_aleatorio(No(atual))
        print("O valor de sucessor é: ", sucessor.estado)"""


    return 0


if __name__ == '__main__':
    main()