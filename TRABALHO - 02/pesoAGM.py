import sys
import time

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
    rep = [x for x in range(n+1)]
    comp = [None] * n
    for u in range(n):
        primeiro = Vertice(u, None)
        ultimo = primeiro
        comp[u] = Componente(primeiro,ultimo,1)
    while contarArestas != n-1:
        aresta = L.pop(0)
        u = aresta[0]
        v = aresta[1]
        if rep[u] != rep[v]:
            contarArestas += 1
            pesoAGM += aresta[2]
            x = rep[u]
            y = rep[v]
            if comp[x].tamanho < comp[y].tamanho:
                cp_x = x
                x = y
                y = cp_x
            z = comp[y].primeiro
            comp[x].ultimo.proximo = z
            comp[x].ultimo = comp[y].ultimo
            comp[x].tamanho = comp[x].tamanho + comp[y].tamanho
            while z != None:
                rep[z.valor] = x
                z = z.proximo
    return pesoAGM


if __name__ == "__main__":
    entrada = sys.stdin.readlines()
    n = int(entrada[2].split('n=')[1])

    Grafo = []
    for x in entrada[4:]:
        aresta = x.split(" ")
        v1 = int(aresta[0]) - 1
        v2 = int(aresta[1]) - 1
        peso = float(aresta[2].split("\n")[0])
        Grafo.append([v1,v2,peso])
    tamanho = calcularPesoAGM(Grafo,n)
    print(f"{tamanho:.3f}")