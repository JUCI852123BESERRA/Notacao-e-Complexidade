import heapq # Necessário para otimizar o Dijkstra

class Grafo:
    """
    Implementa um grafo usando Lista de Adjacência.
    Representação: {vertice: [(vizinho, peso), ...]}
    """
    def __init__(self):
        self.adj = {} # Lista de Adjacência

    def adicionar_vertice(self, vertice):
        """Adiciona um novo vértice (bairro) se não existir."""
        if vertice not in self.adj:
            self.adj[vertice] = []

    def adicionar_aresta(self, origem, destino, peso=1, direcionado=False):
        """
        Adiciona uma aresta ponderada.
        Complexidade: O(1)
        """
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.adj[origem].append((destino, peso))
        
        if not direcionado:
            self.adj[destino].append((origem, peso))

    # --- Busca em Largura (BFS) ---
    def bfs(self, inicio):
        """
        Busca em Largura (BFS).
        Complexidade: O(V + E).
        """
        if inicio not in self.adj:
            return "Vértice inicial não encontrado."

        visitados = set()
        fila = [inicio] # Usando lista como Fila (pop(0))
        caminho = []

        visitados.add(inicio)

        while fila:
            vertice = fila.pop(0)
            caminho.append(vertice)
            
            # Percorre vizinhos
            for vizinho, _ in self.adj.get(vertice, []):
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        
        return caminho

    # --- Busca em Profundidade (DFS) ---
    def dfs(self, inicio):
        """
        Busca em Profundidade (DFS). Implementação recursiva (usa pilha implícita).
        Complexidade: O(V + E).
        """
        if inicio not in self.adj:
            return "Vértice inicial não encontrado."

        visitados = set()
        caminho = []

        def _dfs_recursivo(vertice):
            visitados.add(vertice)
            caminho.append(vertice)

            for vizinho, _ in self.adj.get(vertice, []):
                if vizinho not in visitados:
                    _dfs_recursivo(vizinho)

        _dfs_recursivo(inicio)
        return caminho
    
    # --- Caminho Mínimo (Dijkstra) ---
    def dijkstra(self, inicio, fim):
        """
        Calcula o caminho de custo mínimo entre dois vértices.
        Complexidade: O(E log V) (E = arestas, V = vértices).
        """
        if inicio not in self.adj or fim not in self.adj:
            return float('inf'), []

        # Fila de Prioridade: (custo, vertice)
        fila_prioridade = [(0, inicio)] 
        
        # Distâncias: {vertice: custo}
        distancias = {vertice: float('inf') for vertice in self.adj}
        distancias[inicio] = 0
        
        # Predecessores: {vertice: anterior} para reconstruir o caminho
        predecessores = {}

        while fila_prioridade:
            custo_atual, vertice_atual = heapq.heappop(fila_prioridade)

            # Otimização: se já encontramos um caminho mais longo, ignoramos
            if custo_atual > distancias[vertice_atual]:
                continue
            
            # Se chegou ao destino
            if vertice_atual == fim:
                break

            # Percorre vizinhos
            for vizinho, peso in self.adj.get(vertice_atual, []):
                novo_custo = custo_atual + peso
                
                if novo_custo < distancias[vizinho]:
                    distancias[vizinho] = novo_custo
                    predecessores[vizinho] = vertice_atual
                    heapq.heappush(fila_prioridade, (novo_custo, vizinho))

        # Reconstruir o caminho
        caminho = []
        vertice = fim
        while vertice in predecessores:
            caminho.append(vertice)
            vertice = predecessores[vertice]
        caminho.append(inicio)
        caminho.reverse()

        return distancias[fim], caminho