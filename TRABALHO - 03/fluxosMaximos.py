import sys
import copy
from collections import deque

def fluxoMaximo(E, o, d):
    parente = {}
    fluxo_maximo = 0

    while BFS(E, parente, o, d):
        fluxo_do_caminho = float('inf')
        v = d

        while v != o:
            u = parente[v]
            fluxo_do_caminho = min(fluxo_do_caminho, E[u][v])
            v = u

        fluxo_maximo += fluxo_do_caminho

        v = d
        while v != o:
            u = parente[v]
            E[u][v] -= fluxo_do_caminho
            E[v][u] = E.get(v, {}).get(u, 0) + fluxo_do_caminho
            v = u

    return fluxo_maximo

def BFS(E, parente, o, d):
    lista_visitados = deque()
    lista_visitados.append(o)
    parente.clear()
    parente[o] = -1

    while lista_visitados:
        u = lista_visitados.popleft()

        if u == d:
            return True

        for v, capacidade in E[u].items():
            if v not in parente and capacidade > 0:
                lista_visitados.append(v)
                parente[v] = u

    return False

if __name__ == "__main__":
    entrada = sys.stdin.read().splitlines()
    n = int(entrada[2].split('n=')[1])
    E = {i: {} for i in range(1, n + 1)}

    for x in entrada[4:]:
        aresta = x.split()
        v1, v2, peso = int(aresta[0]), int(aresta[1]), float(aresta[2])
        E[v1][v2] = peso

    o = 1  # Vértice de menor índice
    for d in range(2, n + 1):
        E_copy = copy.deepcopy(E)
        fluxo_maximo = fluxoMaximo(E_copy, o, d)
        fluxo_maximo = int(fluxo_maximo) if fluxo_maximo % 1 == 0 else fluxo_maximo
        print(d, fluxo_maximo)
