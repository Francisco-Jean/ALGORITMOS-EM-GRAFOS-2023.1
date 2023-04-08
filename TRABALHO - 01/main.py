E = {}
try:
  while True:
    aresta = input().split(" ")
    if len(aresta) == 2:
      if aresta[0] in E:
        E[int(aresta[0])].add(int(aresta[1]))
      else:
        E[aresta[0]] = {aresta[1]}
except Exception as e:
  print("Erro: ", e)
  
print(E)

n = int(E[2][0].split("n=")[1])
V = [i for i in range(1, n+1)]
saida = ""
componentes = []
while V:
  lista_atual = [V.pop(0)]
  while lista_atual:
    u = lista_atual.pop()
    for i in range(3,len(E)):
      if E[i] != '' and u in E[i]:
        w = E[i][0] if E[i][1] == u else E[i][1]
        E[i] = ''
        if w in V:
          V.remove(w)
        if w not in lista_atual:
          lista_atual.append(w)
    componentes.append(u)
  componentes.sort(key=lambda x: int(x))
  saida += " ".join(map(str, componentes)) + "\n"
  componentes.clear()
print(saida, end="")
