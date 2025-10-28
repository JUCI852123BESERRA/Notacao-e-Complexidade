class No:
    """Representa um nó na Árvore Binária de Busca."""
    def __init__(self, chave, valor=None):
        self.chave = chave  # Usada para ordenação (ex: ID da cidade)
        self.valor = valor  # Dados da cidade (o objeto Cidade)
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    """
    Implementa uma Árvore Binária de Busca (BST).
    Complexidade Média: O(log n); Pior Caso: O(n) (árvore degenerada).
    """
    def __init__(self):
        self.raiz = None

    def inserir(self, chave, valor=None):
        """
        Insere um novo nó na BST.
        Complexidade: O(h) (h = altura da árvore).
        """
        if self.raiz is None:
            self.raiz = No(chave, valor)
            return

        def _inserir_recursivo(no_atual, chave, valor):
            if chave < no_atual.chave:
                if no_atual.esquerda is None:
                    no_atual.esquerda = No(chave, valor)
                else:
                    _inserir_recursivo(no_atual.esquerda, chave, valor)
            elif chave > no_atual.chave:
                if no_atual.direita is None:
                    no_atual.direita = No(chave, valor)
                else:
                    _inserir_recursivo(no_atual.direita, chave, valor)
            # Se a chave for igual, ignora ou atualiza (depende da regra do negócio)

        _inserir_recursivo(self.raiz, chave, valor)

    def buscar(self, chave):
        """
        Busca um nó pela chave.
        Complexidade: O(h).
        """
        def _buscar_recursivo(no_atual, chave):
            if no_atual is None or no_atual.chave == chave:
                return no_atual
            
            if chave < no_atual.chave:
                return _buscar_recursivo(no_atual.esquerda, chave)
            else:
                return _buscar_recursivo(no_atual.direita, chave)
        
        return _buscar_recursivo(self.raiz, chave)

    # --- Percursos Recursivos (Complexidade O(n) ---
    def inorder(self, no_atual):
        """Percurso: Esquerda -> Raiz -> Direita."""
        resultado = []
        if no_atual:
            resultado.extend(self.inorder(no_atual.esquerda))
            resultado.append(no_atual.chave)
            resultado.extend(self.inorder(no_atual.direita))
        return resultado

    def preorder(self, no_atual):
        """Percurso: Raiz -> Esquerda -> Direita."""
        resultado = []
        if no_atual:
            resultado.append(no_atual.chave)
            resultado.extend(self.preorder(no_atual.esquerda))
            resultado.extend(self.preorder(no_atual.direita))
        return resultado

    def postorder(self, no_atual):
        """Percurso: Esquerda -> Direita -> Raiz."""
        resultado = []
        if no_atual:
            resultado.extend(self.postorder(no_atual.esquerda))
            resultado.extend(self.postorder(no_atual.direita))
            resultado.append(no_atual.chave)
        return resultado

    # Implementação de remoção (mais complexa e omitida para brevidade, mas deve ser incluída)
    # def remover(self, chave): ...