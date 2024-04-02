# Description: Implementação de um grafo utilizando matriz de adjacências
# Irá ter o método adicionar vertice e adicionar aresta
# Também irá ter o método getVertice e getAresta
#
import random
class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[]]
        self.tamanho = 0

    def adicionaVertice(self, rotulo):
        self.vertices.append(rotulo)
        self.tamanho += 1
        for i in range(self.tamanho):
            self.matriz[i].append(0)
        self.matriz.append([0] * self.tamanho)

    def adicionaAresta(self, rotulo1, rotulo2, peso):
        i = self.vertices.index(rotulo1)
        j = self.vertices.index(rotulo2)
        self.matriz[i][j] = peso
        self.matriz[j][i] = peso

    def getAresta(self, vertice1, vertice2):
        i = self.vertices.index(vertice1)
        j = self.vertices.index(vertice2)
        return self.matriz[i][j]

    def getVertice(self, rotulo):
        return self.vertices.index(rotulo)

    def printGrafo(self):
        for i in range(self.tamanho):
            print(self.vertices[i], end=": ")
            for j in range(self.tamanho):
                if self.matriz[i][j] != 0:
                    print(self.vertices[j], end=", ")
                    print("Peso: ", self.matriz[i][j], end=" ")
            
    def printMatriz(self):
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                print(self.matriz[i][j], end=" ")
            print()

        return None

def geraGrafoCompleto5():
    grafo = Grafo()
    grafo.adicionaVertice("A")
    grafo.adicionaVertice("B")
    grafo.adicionaVertice("C")
    grafo.adicionaVertice("D")
    grafo.adicionaVertice("E")
    grafo.adicionaAresta("A", "B", 6)
    grafo.adicionaAresta("A", "C", 2)
    grafo.adicionaAresta("A", "D", 1)
    grafo.adicionaAresta("A", "E", 5)
    grafo.adicionaAresta("B", "C", 2)
    grafo.adicionaAresta("B", "D", 7)
    grafo.adicionaAresta("B", "E", 3)
    grafo.adicionaAresta("C", "D", 10)
    grafo.adicionaAresta("C", "E", 4)
    grafo.adicionaAresta("D", "E", 3)

    return grafo

def geraGrafoCompleto10():
    grafo = Grafo()
    grafo.adicionaVertice("Arad")
    grafo.adicionaVertice("Zerind")
    grafo.adicionaVertice("Oradea")
    grafo.adicionaVertice("Sibiu")
    grafo.adicionaVertice("Fagaras")
    grafo.adicionaVertice("Rimnicu")
    grafo.adicionaVertice("Pitesti")
    grafo.adicionaVertice("Timisoara")
    grafo.adicionaVertice("Lugoj")
    grafo.adicionaVertice("Mehadia")
    #faça um grafo completo com 10 vértices

    grafo.adicionaAresta("Arad", "Zerind", 75)
    grafo.adicionaAresta("Arad", "Oradea", 71 )
    grafo.adicionaAresta("Arad", "Sibiu", 140 )
    grafo.adicionaAresta("Arad", "Fagaras", 99 )
    grafo.adicionaAresta("Arad", "Rimnicu", 80 )
    grafo.adicionaAresta("Arad", "Pitesti", 97 )
    grafo.adicionaAresta("Arad", "Timisoara", 118 )
    grafo.adicionaAresta("Arad", "Lugoj", 111 )
    grafo.adicionaAresta("Arad", "Mehadia", 70 )
    grafo.adicionaAresta("Zerind", "Oradea", 71 )
    grafo.adicionaAresta("Zerind", "Sibiu", 140 )
    grafo.adicionaAresta("Zerind", "Fagaras", 99 )
    grafo.adicionaAresta("Zerind", "Rimnicu", 80 )
    grafo.adicionaAresta("Zerind", "Pitesti", 97 )
    grafo.adicionaAresta("Zerind", "Timisoara", 118 )
    grafo.adicionaAresta("Zerind", "Lugoj", 111 )
    grafo.adicionaAresta("Zerind", "Mehadia", 70 )
    grafo.adicionaAresta("Oradea", "Sibiu", 151 )
    grafo.adicionaAresta("Oradea", "Fagaras", 211 )
    grafo.adicionaAresta("Oradea", "Rimnicu", 151 )
    grafo.adicionaAresta("Oradea", "Pitesti", 160 )
    grafo.adicionaAresta("Oradea", "Timisoara", 140 )
    grafo.adicionaAresta("Oradea", "Lugoj", 120 )
    grafo.adicionaAresta("Oradea", "Mehadia", 75 )
    grafo.adicionaAresta("Sibiu", "Fagaras", 99 )
    grafo.adicionaAresta("Sibiu", "Rimnicu", 80 )
    grafo.adicionaAresta("Sibiu", "Pitesti", 97 )
    grafo.adicionaAresta("Sibiu", "Timisoara", 118 )
    grafo.adicionaAresta("Sibiu", "Lugoj", 111 )
    grafo.adicionaAresta("Sibiu", "Mehadia", 70 )
    grafo.adicionaAresta("Fagaras", "Rimnicu", 80 )
    grafo.adicionaAresta("Fagaras", "Pitesti", 97 )
    grafo.adicionaAresta("Fagaras", "Timisoara", 118 )
    grafo.adicionaAresta("Fagaras", "Lugoj", 111 )
    grafo.adicionaAresta("Fagaras", "Mehadia", 70 )
    grafo.adicionaAresta("Rimnicu", "Pitesti", 97 )
    grafo.adicionaAresta("Rimnicu", "Timisoara", 118 )
    grafo.adicionaAresta("Rimnicu", "Lugoj", 111 )
    grafo.adicionaAresta("Rimnicu", "Mehadia", 70 )
    grafo.adicionaAresta("Pitesti", "Timisoara", 118 )
    grafo.adicionaAresta("Pitesti", "Lugoj", 111 )
    grafo.adicionaAresta("Pitesti", "Mehadia", 70 )
    grafo.adicionaAresta("Timisoara", "Lugoj", 111 )
    grafo.adicionaAresta("Timisoara", "Mehadia", 70 )
    grafo.adicionaAresta("Lugoj", "Mehadia", 70 )

    return grafo

def listaAleatoria( cidade ):
# retorna uma lista de 11 elementos aleatórios com as cidades de Arad, Zerind, Oradea, Sibiu, Fagaras, Rimnicu, Pitesti, Timisoara, Lugoj, Mehadia
# sendo o ultimo elemento e o primeiro tem que ser igual a alguma cidade definida pelo parametro passado
    lista = ["Arad", "Zerind", "Oradea", "Sibiu", "Fagaras", "Rimnicu", "Pitesti", "Timisoara", "Lugoj", "Mehadia"]  
    # tira cidade de lista
    lista.remove(cidade)
    random.shuffle(lista)
    lista.insert(0, cidade)
    lista.append(cidade)
    return lista


# função que pegue um arquivo e calcule o custo do caminho
# a função deve receber o nome do arquivo
# o arquivo deve ter em cada linha o nome de uma cidade e a ponto cartesiano que ela está localizada (x, y)
# O formato do arquivo é : cidade x y
# A função deve retornar uma instancia de grafo que os vertices são as cidades e as arestas são o custo do caminho para outras cidades, logo o grafo é completo
def geraGrafoCidades( arquivo ):
    grafo = Grafo()
    posições = []
    with open(arquivo, "r") as f:
        for linha in f:
            cidade, x, y = linha.split()
            posições.append((cidade, int(x), int(y)))
            grafo.adicionaVertice(cidade)
    for i in range(len(posições)):
        for j in range(len(posições)):
            if i != j:
                x1, y1 = posições[i][1], posições[i][2]
                x2, y2 = posições[j][1], posições[j][2]
                peso = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                grafo.adicionaAresta(posições[i][0], posições[j][0], peso)
            
    f.close()
    return grafo


def main():
    grade = geraGrafoCidades("grafo.txt")
    grade.printMatriz()


if __name__ == "__main__":
    main()
