
import copy
import math
import random

from grafo_matriz_adjacencias import Grafo , geraGrafoCompleto10



TAMANHO = 8
TEMP_INICIAL = 1000
ALPHA = 0.99



class No:
    def __init__(self, estado):
        self.estado = estado
        self.heuristica = 0

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

def busca_tempera_simulada(problema , grafo, limite):
    atual = No(problema)
    atual.heuristica = heuristica(atual.estado , grafo)
    menor  = atual.heuristica
    menorEstado = copy.deepcopy(atual)
    for i in range(limite):
        temp = escalonamento(i) 
        if temp == 0 or atual.heuristica < menor:
            menorEstado = copy.deepcopy(atual)
        proximo = sucessor_aleatorio(atual)
        #print(proximo.estado)
        proximo.heuristica = heuristica(proximo.estado, grafo)
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
    grafo = geraGrafoCompleto10()
    individuo = ['Arad', 'Timisoara' , 'Rimnicu Vilcea', 'Lugoj', 'Zerind', 'Fagaras', 'Oradea', 'Pitesti', 'Mehadia', 'Sibiu', 'Arad']


    # faça um geração de individuos aleatórios
    melhor = None
    menor = 999999999
    for i in range(1):
        individuo = copy.deepcopy(individuo)
        cidade = individuo[0]
        individuo.remove(cidade)
        individuo.remove(cidade)
        random.shuffle(individuo)
        individuo.insert(0, cidade)
        individuo.append(cidade)

        resultado = busca_tempera_simulada(individuo, grafo,1000)
        if resultado.heuristica < menor:
            menor = resultado.heuristica
            melhor = resultado

        #print(heuristica(individuo, grafo))

    
    #print (heuristica(atual, grafo))
    print("O menor caminho é: ", melhor.estado)
    print ("O valor da heurística é: ", melhor.heuristica)
    """while True:
        sucessor = sucessor_aleatorio(No(atual))
        print("O valor de sucessor é: ", sucessor.estado)"""


    return 0


if __name__ == '__main__':
    main()