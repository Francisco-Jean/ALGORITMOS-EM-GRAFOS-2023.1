import sys

class ConjuntoRepresentantes:
    def __init__(self, n):
        self.representante = [i for i in range(n)]
        self.tamanho = [0] * n

    def find(self, x):
        if self.representante[x] != x:
            self.representante[x] = self.find(self.representante[x])
        return self.representante[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.tamanho[x_root] < self.tamanho[y_root]:
            self.representante[x_root] = y_root
        elif self.tamanho[x_root] > self.tamanho[y_root]:
            self.representante[y_root] = x_root
        else:
            self.representante[y_root] = x_root
            self.tamanho[x_root] += 1


class Vertice:
    def __init__(self, valor, proximo):
        self.valor = valor
        self.proximo = proximo

class Componente:
    def __init__(self, primeiro, ultimo, tamanho):
        self.primeiro = primeiro
        self.ultimo = ultimo
        self.tamanho = tamanho

def ordenarArestas(Grafo):
    if len(Grafo) <= 1:
        return Grafo
    else:
        pivo = Grafo[-1]
        menor = [x for x in Grafo[:-1] if x[2] <= pivo[2]]
        maior = [x for x in Grafo[:-1] if x[2] > pivo[2]]
        return ordenarArestas(menor) + [pivo] + ordenarArestas(maior)

def calcularPesoAGM(G,n):
    L = ordenarArestas(G)
    contarArestas = 0
    pesoAGM = 0
    rep = ConjuntoRepresentantes(n)
  
    '''
    comp = [None] * n
    for u in range(n):
        primeiro = Vertice(u, None)
        ultimo = primeiro
        comp[u] = Componente(primeiro,ultimo,1)*/
    '''
  
    while contarArestas != n-1:
        aresta = L.pop(0)
        u = aresta[0]
        v = aresta[1]
        rep_u = rep.find(u)
        rep_v = rep.find(v)
        if rep_u != rep_v:
            contarArestas += 1
            pesoAGM += aresta[2]
            rep.union(rep_u,rep_v)
    return pesoAGM


if __name__ == "__main__":
    entrada = sys.stdin.readlines()
    n = int(entrada[2].split('n=')[1])

    Grafo = []
    for x in entrada[4:]:
        aresta = x.split(" ")
        v1 = int(aresta[0])
        v2 = int(aresta[1])
        peso = float(aresta[2].split("\n")[0])
        Grafo.append([v1,v2,peso])
    tamanho = calcularPesoAGM(Grafo,n)
    print(f"{tamanho:.3f}")