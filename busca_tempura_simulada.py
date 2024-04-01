
import copy
import math
import random

from grafo_matriz_adjacencias import Grafo , geraGrafoCompleto5



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
    # gera um sucessor aleatório que altera a ordem de dois vértices
    i = random.randint(1, no.estado.__len__()-2)
    j = random.randint(1,  no.estado.__len__()-2)
    #print("O valor de i é: ", i, "O valor de j é: ", j)
    while i == j:
        j = random.randint(1,  no.estado.__len__()-2)
    # troca os vértices i e j sabendo que no.estado é uma string mas não altera o tamanho da string
    vertice1 = noAux.estado[i]
    vertice2 = noAux.estado[j]
    noAux.estado = noAux.estado[:i] + vertice2 + noAux.estado[i+1:]
    noAux.estado = noAux.estado[:j] + vertice1 + noAux.estado[j+1:]

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
    grafo = geraGrafoCompleto5()
    atual = "ABEDCA"
    #print (heuristica(atual, grafo))
    resultado = busca_tempera_simulada(atual, grafo,1000)
    print("O menor caminho é: ", resultado.estado)
    print ("O valor da heurística é: ", resultado.heuristica)
    """while True:
        sucessor = sucessor_aleatorio(No(atual))
        print("O valor de sucessor é: ", sucessor.estado)"""


    return 0


if __name__ == '__main__':
    main()