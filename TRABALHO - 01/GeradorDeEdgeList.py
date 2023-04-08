import random


#n = random.randint(10, 10000)
n = 100000
print(n)

if n < 500:
    teto = 2
elif n < 5000:
    teto = 4
else:
    teto = 8

edges = f"dl\nformat=edgelist1\nn={n}\ndata:\n"

vetor = [0] * (n + 1)

for i in range(1, n + 1):
    vetor[i] = i

while len(vetor) > 0:
    escolha = 1
    for x in range(random.randint(1,teto)):
        escolha = random.randint(0, escolha)
        if not escolha:
            break
    if escolha:
        pai = vetor.pop(0)
        valor = random.randint(0, random.randint(0, random.randint(0, len(vetor))))
        valor = random.randint(0,valor)
        valores = random.sample(vetor, valor)
        for x in range(valor):
            edges += str(pai) + " " + str(valores[x]) + "\n"
            vetor.remove(valores[x])
    else:
        vetor.pop(0)


with open("teste.in", "w") as arquivo:
    arquivo.write(edges)  


    