import sys

# Função para implementar o algoritmo de Prim
def prim(grafo):
    n = len(grafo)  # Número de vértices no grafo
    chave = [sys.maxsize] * n  # Armazena o menor peso de cada vértice
    pai = [-1] * n  # Armazena o vértice anterior no caminho para a árvore geradora mínima
    visitado = [False] * n  # Marca os vértices já incluídos na MST
    
    chave[0] = 0  # O primeiro vértice começa com chave 0 para ser escolhido primeiro
    
    for _ in range(n):
        # Encontra o vértice com a chave mínima que ainda não foi visitado
        u = min_key(chave, visitado)
        
        visitado[u] = True  # Marca o vértice u como visitado
        
        # Atualiza os valores das chaves para os vizinhos de u
        for v in range(n):
            if grafo[u][v] != 0 and not visitado[v] and grafo[u][v] < chave[v]:
                chave[v] = grafo[u][v]
                pai[v] = u
    
    # Exibe a árvore geradora mínima
    print_mst(pai, grafo)

# Função auxiliar para encontrar o vértice com a chave mínima
def min_key(chave, visitado):
    min_val = sys.maxsize
    min_index = -1
    
    for v in range(len(chave)):
        if chave[v] < min_val and not visitado[v]:
            min_val = chave[v]
            min_index = v
    
    return min_index

# Função para exibir a árvore geradora mínima
def print_mst(pai, grafo):
    print("Arestas da árvore geradora mínima:")
    for i in range(1, len(grafo)):
        print(f"Vértice {i} - Vértice {pai[i]} com peso {grafo[i][pai[i]]}")

# Exemplo de uso do algoritmo de Prim
# Grafo representado por uma matriz de adjacência
grafo = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim(grafo)
