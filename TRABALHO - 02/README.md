
<strong>Disciplina: </strong>CK0111 - Algoritmos em Grafos <br><br>
<strong>Prazo de Entrega: </strong>03/06/2023 



### Trabalho 2 - Árvore Geradora Mínima

Escreva um programa que compute o peso de uma Árvore Geradora Mínima do grafo recebido como entrada.


#### Formato da Entrada

A entrada, recebida através da [entrada padrão](https://en.wikipedia.org/wiki/Standard_streams), estará no formato [UCINET DL](https://gephi.org/users/supported-graph-formats/ucinet-dl-format/), lista de arestas ("edgelist1"), sem rótulos para os vértices mas com pesos para as arestas, conforme o seguinte exemplo:

    dl
    format=edgelist1
    n=4
    data:
    2 4 -61.500
    1 3 83.750
    1 2 -29.500
    3 4 78.000
    2 3 5.125

Observe que, no formato acima, os vértices são numerados a partir de 1.


#### Formato da Saída

A saída, fornecida através da [saída padrão](https://en.wikipedia.org/wiki/Standard_streams), tem que estar no formato ilustrado pelo seguinte exemplo, que é a saída esperada para a entrada acima:

    -85.875

Ou seja, a saída deve possuir apenas uma linha, que possuirá apenas um número: o peso da AGM, escrito COM EXATAMENTE 3 CASAS DECIMAIS.


#### Importante:

Veja o arquivo `trabalho_2_entradas_e_saidas_para_teste.zip` e as orientações enviadas pelo SIGAA sobre como usar as instâncias e soluções presentes nesse arquivo para testar o seu código. Num terminal do Linux, esses arquivos podem ser utilizados para fazer um teste automático da seguinte forma:

    cat 0.in | ./meu_programa &gt;minha_saida.out
    diff -s minha_saida.out 0.out</textarea><div class="insertMarkdown ng-binding" ng-bind-html="html"><h3 id="trabalho2rvoregeradoramnima">Trabalho 2 - Árvore Geradora Mínima</h3>
