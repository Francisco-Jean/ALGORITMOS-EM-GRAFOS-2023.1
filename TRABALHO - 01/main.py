E = []

try:
  while True:
    E.append(list(map(str, input().strip().split(" "))))
except:
  pass

n = int(E[2][0].split("n=")[1])

vertices = [str(i) for i in range(1, n+1)]

saida = ""

componentes = []

while vertices:
  lista_atual = [vertices.pop(0)]
  while lista_atual:
    u = lista_atual.pop()
    for i in range(3,len(E)):
      if E[i] != None and u in E[i]:
        v = E[i][0] if E[i][1] == u else E[i][1]
        E[i] = None
        if v in vertices:
          vertices.remove(v)
        if v not in lista_atual:
          lista_atual.append(v)
    componentes.append(u)

  valores = sorted(map(int, componentes))
  saida += " ".join(map(str, valores)) + "\n"
  componentes.clear()

print(saida.strip())