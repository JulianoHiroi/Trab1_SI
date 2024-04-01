
from grafo_matriz_adjacencias import Grafo , geraGrafoCompleto5 , geraGrafoCompleto10 , listaAleatoria , geraGrafoCidades
import copy
import random

PROBABILIDADE_MUTACAO = 0.2

class No:
    def __init__(self, estado , grafo):
        self.estado = estado
        self.funcao_adaptativa = funcao_adaptação(self, grafo)
        self.probabilidade = 0
        

def funcao_adaptação(no , grafo):
    # estado será uma lista de string que contém o nome das cidades 
    # o valor da função adaptativa será a soma dos pesos das arestas do caminho
    # a função retorna o valor da função adaptativa
    atual = no.estado[0]
    funcao_adaptativa = 0
    for i in range(1, no.estado.__len__()   ):
        proximo = no.estado[i]
        funcao_adaptativa += grafo.getAresta(atual, proximo)
        atual = proximo
    return funcao_adaptativa

def selecao_aleatoria(populacao):
    # A seleção aleatório irá fazer a soma de todas as funções adaptativas dos nos da população 
    # e escolher um nó aleatório com base na probabilidade de cada nó
    # a probabilidade é feita a partir da subtração da soma das funções adaptativas pelo valor da função adaptativa do nó
    # a função retorna o nó escolhido
    soma = 0
    for i in range(len(populacao)):
        soma += populacao[i].funcao_adaptativa
    somaProbabilidade = 0
    for i in range(len(populacao)):
        populacao[i].probabilidade = soma - populacao[i].funcao_adaptativa
        somaProbabilidade += populacao[i].probabilidade
    probabilidade = []
    for i in range(len(populacao)):
        probabilidade.append(populacao[i].probabilidade / somaProbabilidade)
    acumulado = 0
    r = random.random()
    for i in range ( len(populacao)):
        acumulado = acumulado + probabilidade[i]
        if acumulado >= r:
            return populacao[i]
    
    


def cruzamento(x, y , grafo):
    # o cruzamento irá escolher um ponto aleatório e trocar os genes dos pais
    # a troca irá ocorrer pegando todo o gene do pai x até o ponto escolhido e o resto do gene do pai y
    # sendo os genes restantes do pai y em ordem que aparecem no pai y
    # a função retorna o filho gerado
    filho = copy.deepcopy(x)
    ponto = random.randint(1, x.estado.__len__() -2)
    geneNovo = []
    for i in range(1 , ponto):
        geneNovo.append(x.estado[i])
    for i in range(1, x.estado.__len__() - 1):
        if y.estado[i] not in geneNovo:
            geneNovo.append(y.estado[i])
    # adiciona no gene novo na primeira posição o estado na posição 1 do pai x
    geneNovo.insert(0, x.estado[0])
    # adiciona no gene novo na última posição o estado na última posição do pai x
    geneNovo.append(x.estado[x.estado.__len__() - 1])
    filho.estado = geneNovo
    filho.funcao_adaptativa = funcao_adaptação(filho, grafo)
    return filho
    
def mutacao(filho, grafo):
    # escolhe um gene aleatório para mutar
    gene = random.randint(1, filho.estado.__len__() -2)
    #print ("Gene: ", gene)
    cidade = filho.estado[gene]
    #print ("Cidade: ", cidade)
    geneNovo = copy.deepcopy(filho.estado)
    geneNovo.remove(cidade)

    posAleatoria = random.randint(1, geneNovo.__len__() -2)
    if posAleatoria == gene:
        posAleatoria = random.randint(1, geneNovo.__len__() -2)
    geneNovo.insert(posAleatoria, cidade)
    # gera um novo gene aleatório

    # substitui o gene antigo pelo novo
    filho.estado = geneNovo
    #filho.funcao_adaptativa = funcao_adaptação(filho, grafo)
    return filho


def algoritmo_genetico(populacao, grafo , limite):
    melhor = None
    menor = 999999999
    while limite > 0:
        limite = limite - 1
        nova_populacao = []      
        for i in range ( len(populacao)):
            x = selecao_aleatoria(populacao)
            y = selecao_aleatoria(populacao)
            filho = cruzamento(x, y, grafo)
            if(PROBABILIDADE_MUTACAO > random.random()):
                filho = mutacao(filho , grafo)
            
            if (filho.funcao_adaptativa < menor):
                menor = filho.funcao_adaptativa
                melhor = filho
            nova_populacao.append(filho)
        populacao = nova_populacao
    
    return melhor

def criarPopulacaoInicial(grafo, tamanho):
    populacao = []
    for i in range(tamanho):
        individuo = listaAleatoria("Arad")
        no = No(individuo, grafo)
        populacao.append(no)
    return populacao

def main():
    grafo = geraGrafoCidades("grafo.txt")
    populacao = criarPopulacaoInicial(grafo, 4)

    melhor = None
    menor = 999999999
    for i in range(100):
        solucao = algoritmo_genetico(populacao, grafo, 100)
        if solucao.funcao_adaptativa < menor:
            menor = solucao.funcao_adaptativa
            melhor = solucao

    print(melhor.estado)
    print(melhor.funcao_adaptativa)
if __name__ == "__main__":
    main()
