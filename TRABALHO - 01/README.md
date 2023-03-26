
<strong>Disciplina: </strong>CK0111 - Algoritmos em Grafos 

<strong>Prazo de Entrega: </strong>12/04/2023 



### Trabalho 1 - Componentes Conexas

Escreva um programa que receba um grafo não-direcionado e que escreva as suas componentes conexas. Uma _componente conexa_ é um conjunto maximal de vértices ligados por caminhos no grafo. Assim, por exemplo, se a entrada for (no formato explicado adiante) o grafo

    2--9--6

    3--8--10

    5--7

    1     4

então a saída, conforme o formato explicado adiante, deve ser

    1
    2 6 9
    3 8 10
    4
    5 7


#### Formato da Entrada

A entrada, recebida através da entrada padrão, estará no formato [UCINET DL](https://gephi.org/users/supported-graph-formats/ucinet-dl-format/), lista de arestas ("edgelist1"), sem rótulos para os vértices e sem pesos para as arestas, conforme o seguinte exemplo, que é uma representação para o grafo acima:

    dl
    format=edgelist1
    n=10
    data:
    2 9
    3 8
    5 7
    6 9
    8 10

Observe que, no formato acima, os vértices são numerados a partir de 1.


#### Formato da Saída

A saída, fornecida através da saída padrão, tem que estar no formato ilustrado pelo seguinte exemplo, que é a saída esperada para a entrada acima:

    1
    2 6 9
    3 8 10
    4
    5 7

Mais precisamente:

1. Deve ser impressa uma componente conexa por linha.
2. Em cada linha, os vértices devem aparecer em ordem crescente, separados por um espaço em branco, mas sem um espaço em branco após o último vértice.
3. A primeira linha deve ser a da componente conexa do vértice 1. A segunda linha deve ser a da componente conexa do vértice 2, exceto se ele já tiver aparecido na componente conexa do vértice 1, e assim sucessivamente, ou seja: cada uma das outras linhas contém os vértices da componente conexa do vértice de menor rótulo que não tenha aparecido nas componentes listadas em linhas anteriores.


#### Importante:

1. A saída não precisa ser escrita toda de uma vez, ou seja, você pode gerar a saída *em partes*. O que importa é que a saída gerada pela execução do seu programa, *se considerada como um todo*, esteja no formato indicado acima.

2. Veja o arquivo `exemplos.zip` e as orientações enviadas pelo SIGAA sobre como usar as instâncias e soluções presentes nesse arquivo para testar o seu código.</textarea><div class="insertMarkdown ng-binding" ng-bind-html="html"><h3 id="trabalho1componentesconexas">Trabalho 1 - Componentes Conexas</h3>

<p>Escreva um programa que receba um grafo não-direcionado e que escreva as suas componentes conexas. Uma <em>componente conexa</em> é um conjunto maximal de vértices ligados por caminhos no grafo. Assim, por exemplo, se a entrada for (no formato explicado adiante) o grafo</p>

<pre class="markdown-pre"><code class="hljs sql">2<span class="hljs-comment">--9--6</span>

3<span class="hljs-comment">--8--10</span>

5<span class="hljs-comment">--7</span>

1     4
</code></pre>

<p>então a saída, conforme o formato explicado adiante, deve ser</p>

<pre class="markdown-pre"><code class="hljs">1
2 6 9
3 8 10
4
5 7
</code></pre>

<h4 id="formatodaentrada">Formato da Entrada</h4>

<p>A entrada, recebida através da entrada padrão, estará no formato <a href="https://gephi.org/users/supported-graph-formats/ucinet-dl-format/">UCINET DL</a>, lista de arestas ("edgelist1"), sem rótulos para os vértices e sem pesos para as arestas, conforme o seguinte exemplo, que é uma representação para o grafo acima:</p>

<pre class="markdown-pre"><code class="hljs makefile">dl
<span class="hljs-constant">format</span>=edgelist1
<span class="hljs-constant">n</span>=10
<span class="hljs-title">data:</span>
2 9
3 8
5 7
6 9
8 10
</code></pre>

<p>Observe que, no formato acima, os vértices são numerados a partir de 1.</p>

<h4 id="formatodasada">Formato da Saída</h4>

<p>A saída, fornecida através da saída padrão, tem que estar no formato ilustrado pelo seguinte exemplo, que é a saída esperada para a entrada acima:</p>

<pre class="markdown-pre"><code class="hljs">1
2 6 9
3 8 10
4
5 7
</code></pre>

<p>Mais precisamente:</p>

<ol>
<li>Deve ser impressa uma componente conexa por linha.</li>

<li>Em cada linha, os vértices devem aparecer em ordem crescente, separados por um espaço em branco, mas sem um espaço em branco após o último vértice.</li>

<li>A primeira linha deve ser a da componente conexa do vértice 1. A segunda linha deve ser a da componente conexa do vértice 2, exceto se ele já tiver aparecido na componente conexa do vértice 1, e assim sucessivamente, ou seja: cada uma das outras linhas contém os vértices da componente conexa do vértice de menor rótulo que não tenha aparecido nas componentes listadas em linhas anteriores.</li>
</ol>

<h4 id="importante">Importante:</h4>

<ol>
<li><p>A saída não precisa ser escrita toda de uma vez, ou seja, você pode gerar a saída <em>em partes</em>. O que importa é que a saída gerada pela execução do seu programa, <em>se considerada como um todo</em>, esteja no formato indicado acima.</p></li>

<li><p>Veja o arquivo <code>exemplos.zip</code> e as orientações enviadas pelo SIGAA sobre como usar as instâncias e soluções presentes nesse arquivo para testar o seu código.</p></li>
</ol></div>
                            </div>
                                            </div>
                    <br>
                    <a href="#" ng-show="descr==1" ng-click="descr=0;$event.preventDefault();" class="btn btn-color-two btn-sm">Esconder Descrição</a>                    <a href="#" ng-show="descr==0" ng-click="descr=1;$event.preventDefault();" class="btn btn-color-two btn-sm ng-hide">Ver Descrição</a>                    <br>
                                            <br><strong>Arquivos:</strong>                        <ul class="nav nav-pills">
                                                    <li class="active">
                                <a href="/ExerciseFiles/fileDownload/13100">exemplos.zip</a>                            </li>
                                                </ul>
                                                                <br><strong>Este exercício aceita os seguintes tipos de arquivos:</strong>                        <ul class="nav nav-pills">
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">Haskell</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">C++</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">Fortran</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">Pascal</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">Java 8</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">C</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">Python 3</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">Octave</span>
                            </li>
                                                    <li style="margin-right: 3px;">
                                <span class="label label-info">R statistical software</span>
                            </li>
                                                </ul>
                        <br>
<strong>Atenção: </strong>Para ser corretamente corrigido, seu código, se entregue em um único arquivo .java:
<ul>
    <li>não pode definir um pacote específico;</li>
    <li>não pode definir nenhuma classe pública;</li>
    <li>deve, obrigatoriamente, definir uma classe <strong>"Main"</strong> com o método "main" que será chamado para começar a execução.</li>
</ul>
Isso ocorre pelas características da linguagem Java, se você tem alguma dúvida, entre em contato com support@run.codes.                                                                                </div>