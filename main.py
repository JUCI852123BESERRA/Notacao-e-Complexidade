from arvore_avl import ArvoreAVL
from grafo import Grafo
import sys

# --- Estrutura da Cidade ---
class Cidade:
    def __init__(self, id_cidade, nome):
        self.id = id_cidade
        self.nome = nome
        self.grafo = Grafo() # Cada cidade tem seu próprio grafo de bairros
    
    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome}"

# --- Sistema de Gerenciamento (O orquestrador) ---
class SistemaGerenciamento:
    def __init__(self):
        # A AVL usa o ID da cidade como chave para garantir busca rápida
        self.arvore_cidades = ArvoreAVL()

    def _obter_cidade(self, id_cidade):
        """Busca uma cidade na AVL e retorna o objeto Cidade."""
        no = self.arvore_cidades.buscar(id_cidade)
        return no.valor if no else None

    # --- Funções do Menu ---

    def cadastrar_cidade(self, id_cidade, nome):
        """Cadastra a cidade na AVL."""
        nova_cidade = Cidade(id_cidade, nome)
        self.arvore_cidades.inserir(id_cidade, nova_cidade)
        print(f"\n[SUCESSO] Cidade '{nome}' cadastrada (ID: {id_cidade}).")
        print("Complexidade Teórica da Inserção (AVL): O(log n)")

    def mostrar_percursos(self):
        """Exibe os IDs das cidades nos três percursos."""
        if not self.arvore_cidades.raiz:
            print("\n[INFO] A árvore de cidades está vazia.")
            return

        print("\n--- Percursos da AVL de Cidades (IDs) ---")
        print(f"Pré-Ordem (Raiz -> E -> D): {self.arvore_cidades.preorder(self.arvore_cidades.raiz)}")
        print(f"Em-Ordem (E -> Raiz -> D): {self.arvore_cidades.inorder(self.arvore_cidades.raiz)}")
        print(f"Pós-Ordem (E -> D -> Raiz): {self.arvore_cidades.postorder(self.arvore_cidades.raiz)}")
        print("Complexidade Teórica dos Percursos: O(n)")

    def gerenciar_rotas(self, id_cidade):
        """Menu para interagir com o grafo interno da cidade."""
        cidade = self._obter_cidade(id_cidade)
        if not cidade:
            print(f"\n[ERRO] Cidade com ID {id_cidade} não encontrada. Complexidade de busca: O(log n).")
            return
        
        # Menu de Grafo (simplificado para o esboço)
        print(f"\n--- Rotas de {cidade.nome} ---")
        g = cidade.grafo
        
        # Exemplo de uso
        g.adicionar_aresta("Centro", "Bairro A", 5)
        g.adicionar_aresta("Centro", "Bairro B", 2)
        g.adicionar_aresta("Bairro A", "Bairro C", 4)
        g.adicionar_aresta("Bairro B", "Bairro C", 8)
        
        print("\n[1] Busca em Largura (BFS) do Centro:")
        caminho_bfs = g.bfs("Centro")
        print(f"  Resultado: {caminho_bfs}")
        print("  Complexidade: O(V + E)")

        print("\n[2] Caminho Mínimo (Dijkstra) do Centro para Bairro C:")
        distancia, caminho = g.dijkstra("Centro", "Bairro C")
        if distancia != float('inf'):
            print(f"  Caminho: {' -> '.join(caminho)} | Custo Total: {distancia}")
            print("  Complexidade: O(E log V)")
        else:
            print("  Caminho não encontrado.")

    # --- Menu Principal ---
    def menu_principal(self):
        while True:
            print("\n" + "="*40)
            print("SISTEMA DE GESTÃO DE CIDADES E ROTAS")
            print("="*40)
            print("1. Cadastrar Nova Cidade (AVL)")
            print("2. Mostrar Percursos da Árvore (IDs)")
            print("3. Gerenciar Rotas de Cidade (Grafo)")
            print("0. Sair")
            
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                try:
                    id_cidade = int(input("ID da Cidade (Chave): "))
                    nome = input("Nome da Cidade: ")
                    self.cadastrar_cidade(id_cidade, nome)
                except ValueError:
                    print("[ERRO] ID deve ser um número inteiro.")
            
            elif escolha == '2':
                self.mostrar_percursos()

            elif escolha == '3':
                try:
                    id_cidade = int(input("ID da Cidade para gerenciar rotas: "))
                    self.gerenciar_rotas(id_cidade)
                except ValueError:
                    print("[ERRO] ID deve ser um número inteiro.")

            elif escolha == '0':
                print("Saindo do sistema. Até mais!")
                sys.exit()

            else:
                print("[ERRO] Opção inválida.")

if __name__ == "__main__":
    sistema = SistemaGerenciamento()
    # Dados iniciais para teste
    sistema.cadastrar_cidade(50, "São Paulo")
    sistema.cadastrar_cidade(30, "Rio de Janeiro")
    sistema.cadastrar_cidade(70, "Belo Horizonte")
    sistema.cadastrar_cidade(10, "Porto Alegre")
    sistema.menu_principal()