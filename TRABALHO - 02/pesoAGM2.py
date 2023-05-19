import sys

class ConjuntoRepresentantes:
    def __init__(self, n):
        self.parente = list(range(n))
        self.tamanho = [0] * n

    def achar(self, x):
        if self.parente[x] != x:
            self.parente[x] = self.achar(self.parente[x])
        return self.parente[x]

    def unir(self, x, y):
        x_parente = self.achar(x)
        y_parente = self.achar(y)

        if x_parente == y_parente:
            return

        if self.tamanho[x_parente] < self.tamanho[y_parente]:
            self.parente[x_parente] = y_parente
        elif self.tamanho[x_parente] > self.tamanho[y_parente]:
            self.parente[y_parente] = x_parente
        else:
            self.parente[y_parente] = x_parente
            self.tamanho[x_parente] += 1


def calcularPesoAGM(Grafo, n):
    Grafo.sort(key=lambda x: x[2])  # Ordena as arestas em ordem crescente de peso
    representantes = ConjuntoRepresentantes(n)
    tamanho_minimo = 0
    m = 0

    for u, v, tamanho in Grafo:
        if m == n - 1:
            break

        if representantes.achar(u) != representantes.achar(v):
            representantes.unir(u, v)
            tamanho_minimo += tamanho
            m += 1

    return tamanho_minimo


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    n = int(lines[2].split('=')[1])

    Grafo = []
    for line in lines[4:]:
        v1, v2, tamanho = map(float, line.split())
        v1 = int(v1) -1
        v2 = int(v2) -1
        Grafo.append((v1, v2, tamanho))

    tamanho_minimo = calcularPesoAGM(Grafo, n)
    print(f"{tamanho_minimo:.3f}")
