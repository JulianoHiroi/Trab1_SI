
import random

class Grafo :
    def __init__(self) :
        self.vertices = []

    def adicionaVertice(self, rotulo) :
        self.vertices.append(Vertice(rotulo))
    
    def adicionaAresta(self, rotulo1, rotulo2, peso) :
        v1 = self.getVertice(rotulo1)
        v2 = self.getVertice(rotulo2)
        v1.adicionaVizinho(v2, peso)
        v2.adicionaVizinho(v1, peso)

    def getAresta(self, vertice1, vertice2) :
        for vizinho in vertice1.vizinhos:
            if vizinho.vizinho == vertice2:
                return vizinho
        return None
    def getVertice(self, rotulo) :
        for vertice in self.vertices :
            if vertice.rotulo == rotulo :
                return vertice
            
    def printGrafo(self):
        for vertice in self.vertices:
            print(vertice.rotulo, end=": ")
            for vizinho in vertice.vizinhos:
                print(vizinho, end=", ")
            print()
        
        return None


class Vertice :
    def __init__(self, rotulo) :
        self.rotulo = rotulo
        self.vizinhos = []

    def adicionaVizinho(self, vizinho , peso) :
        self.vizinhos.append(Vizinho(peso, vizinho))

    def __str__(self) :
        return self.rotulo
    
class Vizinho :
    def __init__(self, peso, vizinho) :
        self.peso = peso
        self.vizinho = vizinho


    def __str__(self) :
        return str(self.vizinho) + " (" + str(self.peso) + ")"
    
def geraGrafoCompletoAleatorio(): 
    # função gera um grafo completo com 10 elementos e pesos aleatórios
    grafo = Grafo()
    for i in range(10):
        grafo.adicionaVertice(str(i))
    for i in range(10):
        for j in range(i+1, 10):
            grafo.adicionaAresta(str(i), str(j), random.randint(1, 10))
    return grafo

def geraGrafoCompleto10():
    # função gera um grafo completo com 10 elementos definidos por letras em maiuscula e pesos variados mas fixos
    grafo = Grafo()
    for i in range(10):
        grafo.adicionaVertice(chr(65+i))
    for i in range(10):
        for j in range(i+1, 10):
            grafo.adicionaAresta(chr(65+i), chr(65+j), i+j)
    return grafo
def geraGrafoCompleto5():
    # função gera um grafo completo com 5 elementos definidos por letras em maiuscula e pesos variados mas fixos
    grafo = Grafo()
    A = Vertice("A")
    B = Vertice("B")
    C = Vertice("C")
    D = Vertice("D")
    E = Vertice("E")
    grafo.vertices.append(A)
    grafo.vertices.append(B)
    grafo.vertices.append(C)
    grafo.vertices.append(D)
    grafo.vertices.append(E)
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

def main():
    grafo = geraGrafoCompleto5()
    grafo.printGrafo()
    return

if __name__ == "__main__":
    main()

