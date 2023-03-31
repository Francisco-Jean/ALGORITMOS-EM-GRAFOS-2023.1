E = list(map(str, '''dl
format=edgelist1
n=10
data:
2 9
3 8
5 7
6 9
8 10'''.split("\n")))

E.pop(0)
E.pop(0)
n = E.pop(0)
n = int(n.split("n=")[1])
E.pop(0)                                                  

for x in range(len(E)):
  E[x] = list(map(str, E[x].split(" ")))
vertices = [''] * n

for i in range(n):
  vertices[i] = str(i+1)

saida = ""

while len(vertices) > 0:
  componentes = []
  lista_atual = [vertices.pop(0)]
  while len(lista_atual) > 0:
    for i in E:
      if lista_atual[0] in i:
        v = E.pop(E.index(i))
        v = v[int(not v.index(lista_atual[0]))]
        if v not in lista_atual:
          lista_atual.append(v)
        if v in vertices:
          vertices.pop(vertices.index(v))
    componentes.append(lista_atual.pop(0))

  valores = [int(val) for val in componentes]
  valores.sort()
  for u in valores:
    saida += str(u) + " "
  print(saida.strip())
  saida = ""