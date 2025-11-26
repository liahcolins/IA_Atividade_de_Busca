# Algoritmo de Busca A (A-Star) em Grafos com NetworkX*
Aluno: Débora Letícia Silva dos Santos, Felipe Portela Aguilar de Oliveira e Liah Renata Colins da Silva

Disciplina: Inteligência Artificial

Professor: Alex Oliveira Barradas Filho

# 1. Introdução

O presente trabalho tem como objetivo demonstrar a aplicação do algoritmo de busca A* (A-Star) para encontrar o caminho de menor custo em um grafo direcionado e ponderado. A implementação foi desenvolvida em Python, utilizando a biblioteca NetworkX para a estruturação do grafo e execução do algoritmo, e a biblioteca Matplotlib para a visualização gráfica dos nós, arestas e do caminho encontrado.

Diferente de abordagens baseadas em grades físicas (grids), este projeto foca na abstração de nós e arestas (como cidades conectadas por estradas), onde cada conexão possui um peso (custo real) e cada nó possui uma heurística associada.

# 2. Modelagem do Problema

2.1 Definição do Cenário O problema consiste em encontrar a rota ótima entre um Nó Inicial (A) e um Nó Objetivo (E) em um grafo pré-definido.

2.2 Estrutura do Grafo O ambiente é modelado como um grafo direcionado, composto por:

Nós (Vértices): 5 nós rotulados de 'A' a 'E'.

Arestas (Conexões): Ligações direcionadas entre os nós, onde cada aresta possui um atributo de peso representando o custo real do deslocamento. Por exemplo, mover de A para B tem custo 5.

2.3 Função de Avaliação A* O algoritmo utiliza a função f(n) = g(n) + h(n), onde:

g(n): É o custo real acumulado do nó inicial até o nó atual (soma dos pesos das arestas percorridas).

h(n): É a heurística, ou seja, a estimativa do nó atual até o objetivo.

Neste projeto, os valores heurísticos foram definidos de forma fixa (tabelada) para simular o conhecimento prévio da distância até o destino. A tabela utilizada define que a distância estimada de A é 11, de B é 6, de C é 7, de D é 3, e de E é 0 (pois é o objetivo).

# 3. Implementação

3.1 Bibliotecas Utilizadas Foram utilizadas a biblioteca NetworkX, para criação da estrutura de dados do grafo e para o cálculo do caminho (utilizando a função nativa astar_path), e a biblioteca Matplotlib, para plotar o grafo visualmente e permitir a identificação dos elementos por cores.

3.2 Lógica do Código O código opera em três etapas principais. Primeiro, ocorre a construção, onde o grafo é montado adicionando as arestas ponderadas. Em seguida, a busca é realizada executando a função do NetworkX, que recebe como parâmetro uma função customizada de heurística que retorna os valores pré-configurados.

Por fim, ocorre a visualização. O nó de início é colorido de verde, o destino de vermelho, e os demais de azul claro. As arestas que compõem a solução ótima são destacadas com uma linha mais grossa na cor azul, enquanto as rotas descartadas permanecem em cinza. O gráfico exibe também os custos das arestas e as heurísticas dos nós.

# 4. Como Executar

Para reproduzir o experimento, é necessário ter a linguagem Python instalada no computador. Além disso, é preciso instalar as bibliotecas "networkx" e "matplotlib" através do gerenciador de pacotes do Python (pip).

Após a instalação das dependências, basta executar o script principal.

# 5. Resultados Esperados

Ao executar o código, o sistema apresentará dois resultados. No console ou terminal, será impressa a sequência de nós visitados (Caminho Ótimo: A, C, D, E) e o Custo Total da distância (que neste caso é 13). Simultaneamente, uma janela gráfica será aberta exibindo o desenho do grafo com a rota sugerida destacada em azul.

# 6. Conclusão

A implementação demonstrou com sucesso o uso da biblioteca NetworkX para resolver problemas de pathfinding. A visualização gerada facilitou o entendimento de como o algoritmo prioriza certas rotas baseando-se na soma do custo real com a estimativa heurística, validando a teoria de busca informada estudada na disciplina.
