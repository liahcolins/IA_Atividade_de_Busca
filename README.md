# Algoritmo de Busca $A^{*}$ para Navegação em Grade com Obstáculos

Aluno: Débora Letícia Silva dos Santos, Felipe Portela Aguilar de Oliveira e Liah Renata Colins da Silva

Disciplina: Inteligência Artificial

Professor: Alex Oliveira Barradas Filho

# 1. Introdução

O presente trabalho tem como objetivo modelar um problema de pathfinding em um ambiente de grade 2D com obstáculos e implementar a solução de caminho ótimo utilizando o algoritmo de busca $A^{*}$  (A-star). A implementação foi desenvolvida em Python, empregando a biblioteca Pygame para a simulação visual, além de NetworkX e Matplotlib para a geração gráfica do resultado final.

O algoritmo  $A^{*}$ foi selecionado por sua eficiência em desviar de obstáculos enquanto minimiza o custo total do trajeto, tornando-o uma escolha robusta e amplamente utilizada em problemas de busca de caminhos.

# 2. Modelagem do Problema

## 2.1 Definição do Problema

O problema consiste em encontrar a rota de menor custo entre um ponto inicial (coordenada $x, y$) e um ponto objetivo em uma grade de tamanho fixo ($600 \times 600$ pixels), contornando um conjunto de obstáculos fixos definidos no código.

## 2.2 Estrutura do Ambiente

O ambiente foi modelado como uma grade discreta onde:

Nós: Representam as coordenadas $(x, y)$ acessíveis na tela, espaçadas por um tamanho de bloco de 20 pixels.

Movimentos: São permitidos movimentos ortogonais (Cima, Baixo, Esquerda, Direita).

Obstáculos: Conjunto de coordenadas intransponíveis (paredes e barreiras).

## 2.3 Função de Avaliação $A^{*}$

O algoritmo utiliza a função de custo padrão $f(n) = g(n) + h(n)$, onde:

$g(n)$: Custo real do passo (neste código, cada movimento tem custo 1).

$h(n)$: Heurística calculada pela Distância de Manhattan, ideal para grades onde o movimento diagonal não é permitido.

# 3. Implementação e Resultados

## 3.1 Ambiente de Desenvolvimento

O código-fonte foi desenvolvido em Python. A lógica de busca utiliza a estrutura de dados heapq (fila de prioridade) para eficiência, enquanto a visualização é dividida entre Pygame (simulação dinâmica) e Matplotlib/NetworkX (geração de imagem estática do grafo).

## 3.2 Estrutura do Código

A solução implementada difere do uso nativo de bibliotecas de grafos, optando por uma implementação manual do algoritmo para maior controle sobre a grade. As principais funções são:

Função Heurística (distancia_manhattan):

Calcula a estimativa de custo restante utilizando a fórmula $|x_1 - x_2| + |y_1 - y_2|$. Esta função guia o algoritmo em direção ao objetivo.

Algoritmo A (a_star_busca):*

Esta é a função central. Em vez de usar uma função pronta do NetworkX para a busca, o algoritmo foi implementado manualmente:

Utiliza uma lista fronteira gerenciada por heapq.heappush e heapq.heappop para expandir sempre o nó com menor custo $f$.

Mantém dicionários g_score e veio_de para rastrear o custo atual e reconstruir o caminho final.

Verifica colisões comparando as coordenadas vizinhas com o conjunto obstaculos_fixos.

Visualização e Exportação (salvar_grafo_png):

Após o cálculo do caminho, esta função utiliza nx.grid_2d_graph para criar uma representação visual dos nós visitados e obstáculos, salvando o resultado final como uma imagem PNG através do matplotlib.pyplot.

## 3.3 Demonstração e Solução

Ao executar o script (loop_jogo), o sistema realiza os seguintes passos:

Calcula a rota entre o Início $(40, 40)$ e o Objetivo $(540, 540)$.

Exibe a simulação da "Cobra" percorrendo o caminho na janela do Pygame.

Gera um arquivo de imagem (snake_caminho_grafo.png) ilustrando o grafo.

Output do Console:

Gerando imagem do grafo... Aguarde.

Rota encontrada! [N] passos.
SUCESSO! O gráfico foi salvo como 'snake_caminho_grafo.png' na pasta do projeto.

# 4. Análise Crítica e Conclusão

## 4.1 Limitações da Implementação

A implementação atual utiliza uma grade uniforme. A função distancia_manhattan é perfeitamente adequada para movimentos em 4 direções, mas se movimentos diagonais fossem permitidos, seria necessário alterar a heurística para a Distância Euclidiana ou Chebyshev para manter a admissibilidade.

## 4.2 Conclusão

O trabalho implementou com sucesso o algoritmo $A^{*}$ "do zero", sem depender de funções de busca prontas ("caixa preta"), demonstrando o entendimento da lógica de filas de prioridade e custos heurísticos. A integração com o Pygame permitiu validar visualmente que o agente desvia corretamente das paredes e obstáculos configurados.
