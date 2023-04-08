import sys

entrada = sys.stdin.readlines()
n = int(entrada[2].split('n=')[1])
E = {chave: set()  for chave in range(1, n+1)}

for x in entrada[4:]:
    aresta = x.split()
    v1, v2 = (aresta[0], aresta[1].split("\n")[0])
    E[int(v1)].add(int(v2))
    E[int(v2)].add(int(v1))

def visitar(v, E, visitados, componente):

    """
    Esta função recebe como entrada os seguintes parâmetros:
    - v: Vértice do grafo que a função irá acessar os vizinhos
    - E: A lista de adjacências com os vizinhos de cada vértice do grafo
    - visitados: O dicinário com 'n' posições que informa se o vertice Xi foi visitado ou não
    - componentes: O vetor onde serão adicionadas as componentes conexas pertecentes aos viinhos do vertice 'v'

    Ela irá percorrer, de forma recursiva, toda a componente conexa a qual o vertice 'v' está contido.
    """

    visitados[v] = True
    componente.append(v)
    for u in E[v]:
        if not visitados[u]:
            visitar(u, E, visitados, componente)


def achar_componentes(E):
    visitados = {i: False for i in range(1, n+1)}
    componentes = []
    for v in E:
        if not visitados[v]:
            componente = []
            visitar(v, E, visitados, componente)
            componentes.append(sorted(componente))
    return componentes

def printarComponentes(componentes):
    saida = ""
    for c in componentes:
        saida += " ".join(map(str, c)) + '\n'
    print(saida, end="")


componentes = achar_componentes(E)
printarComponentes(componentes)

