
from grafo_matriz_adjacencias import Grafo , geraGrafoCompleto5 , geraGrafoCompleto10 , listaAleatoria
import copy
import random

PROBABILIDADE_MUTACAO = 0.1

class No:
    def __init__(self, estado , grafo):
        self.estado = estado
        self.funcao_adaptativa = funcao_adaptação(self, grafo)

def funcao_adaptação(no , grafo):
    # estado será uma lista de string que contém o nome das cidades 
    # o valor da função adaptativa será a soma dos pesos das arestas do caminho
    # a função retorna o valor da função adaptativa
    atual = no.estado[0]
    funcao_adaptativa = 0
    for i in range(1, len(no.estado)):
        proximo = no.estado[i]
        funcao_adaptativa += grafo.getAresta(atual, proximo)
        atual = proximo
    return funcao_adaptativa

def selecao_aleatoria(populacao,grafo):
    soma = 0   
    return None

def cruzamento(x, y):
    # escolhe um ponto de corte aleatório
    corte = random.randint(2, x.estado.__len__()-2)
    geneNovo = x.estado[:corte] + y.estado[corte:]
    print ("O gene novo é: ", geneNovo)
    filho = No(geneNovo)
    return filho

    
def mutacao(filho):
    # escolhe um gene aleatório para mutar
    gene = random.randint(0, filho.estado.__len__() -1)
    # gera um novo gene aleatório
    novoGene = random.randint(0, filho.estado.__len__() -1)
    if filho.estado[gene] == novoGene:
        novoGene = random.randint(0, filho.estado.__len__() -1)
    # substitui o gene antigo pelo novo
    filho.estado[gene] = novoGene
    return filho


def algoritmo_genetico(populacao , limite):
    
    while limite > 0:
        limite = limite - 1
        nova_populacao = []
        for i in range ( len(populacao)):
            x = selecao_aleatoria(populacao)
            y = selecao_aleatoria(populacao)
            filho = cruzamento(x, y)
            if(PROBABILIDADE_MUTACAO > random.random()):
                filho = mutacao(filho)
            if (filho.funcao_adaptativa == 28):
                return filho
            nova_populacao.append(filho)
            populacao = nova_populacao
        
    return None

def main():
    grafo = geraGrafoCompleto10()
    populacao = []
    for i in range(10):
        aux = No(listaAleatoria("Arad"), grafo)
        populacao.append(aux)
        print(aux.estado)

    filho = cruzamento(populacao[0], populacao[1])
    print(filho.estado)

if __name__ == "__main__":
    main()
