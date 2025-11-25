import networkx as nx
import matplotlib.pyplot as plt # Importa a biblioteca para plotagem

# --- Configurações Iniciais ---
START_NODE = 'A' # Nó de partida
GOAL_NODE = 'E'  # Nó de destino

# --- 1. Definição do Grafo ---
G = nx.DiGraph() 

# 2. Adicionar Arestas com os Pesos (Distâncias Reais - Custo g(n))
arestas = [
    # Rotas de A (com simetria)
    ('A', 'B', 5), ('A', 'C', 2),
    # Rotas de B (com simetria)
    ('B', 'D', 4), ('B', 'A', 5), 
    # Rotas de C (com simetria)
    ('C', 'D', 8), ('C', 'E', 10),
    ('C', 'A', 2), 
    # Rotas de D (com simetria)
    ('D', 'E', 3), ('D', 'B', 4), 
    ('D', 'C', 8), 
    # Rotas de E (com simetria)
    ('E', 'C', 10), ('E', 'D', 3)  
]

G.add_weighted_edges_from(arestas)

# --- 3. Função Heurística (h(n)) ---
def heuristica_para_E(u, v):
    """
    Retorna a heurística h(n) (custo estimado) do nó 'u' até o nó destino 'E'.
    O argumento 'v' (destino) é ignorado, pois o destino é fixo neste problema.
    """
    # Valores h(n) definidos para o nosso mapa
    heuristics = {
        'A': 11, 'B': 6, 'C': 7,
        'D': 3,  'E': 0
    }
    return heuristics.get(u, float('inf')) 

# --- 4. Execução do Algoritmo A* ---
if __name__ == '__main__':
    print(f"--- Busca A* em Grafo de Cidades (Visual) ---")
    print(f"Início: {START_NODE}, Destino: {GOAL_NODE}\n")
    
    path = None
    cost = None

    try:
        # Encontra o caminho mais curto usando A*
        path = nx.astar_path(
            G, source=START_NODE, target=GOAL_NODE, 
            heuristic=heuristica_para_E, weight='weight'
        )

        # Calcula o custo total do caminho
        cost = nx.astar_path_length(
            G, source=START_NODE, target=GOAL_NODE, 
            heuristic=heuristica_para_E, weight='weight'
        )
        
        print(f"Solução Encontrada pelo A*:")
        print(f"Caminho Ótimo: {' -> '.join(path)}")
        print(f"Custo Total (Distância): {cost}")
        
    except nx.NetworkXNoPath:
        print(f"Erro: Não foi encontrado um caminho entre {START_NODE} e {GOAL_NODE}.")
    except nx.NodeNotFound:
        print("Erro: Um dos nós (origem ou destino) não existe no grafo.")

    # --- 5. Visualização do Grafo e do Caminho ---
    if path and cost is not None:
        # 5.1. Definir Posições (Layout Fixo para Visualização Limpa)
        pos = {
            'A': (0, 0),
            'B': (2, 2),
            'C': (2, -2),
            'D': (4, 1),
            'E': (6, 0)
        }

        # 5.2. Configurar Elementos Visuais
        
        # Cores dos nós (Início verde, Fim vermelho, Outros azul claro)
        node_colors = ['lightblue' if n not in [START_NODE, GOAL_NODE] else ('green' if n == START_NODE else 'red') for n in G.nodes()]
        
        # Identificar as arestas que compõem o caminho ótimo
        path_edges = list(zip(path[:-1], path[1:]))
        
        # Cores e Larguras das arestas (Caminho ótimo azul, Outras cinza)
        edge_colors = ['blue' if edge in path_edges or tuple(reversed(edge)) in path_edges else 'gray' for edge in G.edges()]
        edge_widths = [3 if edge in path_edges or tuple(reversed(edge)) in path_edges else 1 for edge in G.edges()]

        # 5.3. Desenhar o Grafo
        plt.figure(figsize=(12, 7))
        plt.title(f"Busca A*: Caminho Ótimo {START_NODE} -> {GOAL_NODE} | Custo: {cost}", fontsize=14)

        # Desenhar os nós
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000)
        
        # Desenhar as arestas
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths, alpha=0.7, arrows=True, arrowsize=20)
        
        # Desenhar rótulos (nomes) dos nós
        nx.draw_networkx_labels(G, pos, font_size=16, font_color='black')
        
        # Adicionar rótulos dos pesos das arestas (Custo g(n))
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='dimgray', font_size=12)
        
        # Adicionar rótulos de Heurística (h(n)) ao lado dos nós 
        # (Ajuste de posição para não sobrepor o nome do nó)
        heuristic_labels = {
            'A': 'H=11', 'B': 'H=6', 'C': 'H=7',
            'D': 'H=3',  'E': 'H=0'
        }
        
        # Cria um novo dicionário de posições ajustadas para os rótulos H
        h_pos = {k: (v[0] + 0.1, v[1] - 0.3) for k, v in pos.items()} 
        nx.draw_networkx_labels(G, h_pos, labels=heuristic_labels, font_color='blue', font_size=12, bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

        
        plt.axis('off') # Remover eixos do Matplotlib
        plt.show() # Mostrar o gráfico