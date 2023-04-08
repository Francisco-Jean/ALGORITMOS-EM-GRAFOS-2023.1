import collections
import sys

E = collections.defaultdict(set)
entrada = sys.stdin.readlines()

n = int(entrada[2].split('n=')[1])

for x in entrada[4:]:
    aresta = x.split()
    v1, v2 = (aresta[0], aresta[1].split("\n")[0])
    E[v1].add(v2)

print(E)
V = collections.UserList(str(i) for i in range(1, n+1))
componentes = collections.UserList()
saida = ""
while V:
    fila = collections.deque([V.pop(0)])
    while fila:
        u = fila.popleft()
        if u in E:
            vizinhos = E[u]
            del E[u]
            for v in vizinhos:
                if v in V:
                    V.remove(v)
                    fila.append(v)
                    print(fila)
        componentes.append(u)
    if len(componentes) > 1:
        componentes.sort(key=lambda x: int(x))
        saida += " ".join(map(str, componentes)) + '\n'
    else:
        saida += componentes[0] + '\n'
    componentes.clear()
print(saida, end="")

