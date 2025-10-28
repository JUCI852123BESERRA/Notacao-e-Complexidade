from arvore_binaria import No # Reutiliza a estrutura base do Nó
import math

class NoAVL(No):
    """Extensão do Nó BST com atributo de altura."""
    def __init__(self, chave, valor=None):
        super().__init__(chave, valor)
        self.altura = 1  # Nó folha tem altura 1 por definição

class ArvoreAVL:
    """
    Implementa uma Árvore AVL, que é uma BST auto-balanceada.
    Complexidade: O(log n) para Inserção, Remoção e Busca.
    """
    def __init__(self):
        self.raiz = None

    # --- Funções Auxiliares de Balanceamento ---
    def _get_altura(self, no):
        """Retorna a altura do nó (0 se None)."""
        return no.altura if no else 0

    def _get_fb(self, no):
        """Calcula o Fator de Balanceamento (FB)."""
        return self._get_altura(no.esquerda) - self._get_altura(no.direita) if no else 0

    def _atualizar_altura(self, no):
        """Atualiza a altura do nó após uma operação."""
        no.altura = 1 + max(self._get_altura(no.esquerda), self._get_altura(no.direita))

    # --- Rotações (Rebalanceamento) ---
    def _rotacao_direita(self, z):
        """
        Rotação Simples à Direita (caso LL).
              z                   y
             / \                 / \
            y   T3    ==>       x   z
           / \                 / \ / \
          x   T2              T1 T2 T3
        """
        y = z.esquerda
        T2 = y.direita

        # Realiza a rotação
        y.direita = z
        z.esquerda = T2

        # Atualiza alturas
        self._atualizar_altura(z)
        self._atualizar_altura(y)

        return y # Nova raiz sub-árvore

    def _rotacao_esquerda(self, z):
        """
        Rotação Simples à Esquerda (caso RR).
              z                     y
             / \                   / \
            T1  y      ==>        z   x
               / \               / \ / \
              T2  x             T1 T2 T3
        """
        y = z.direita
        T2 = y.esquerda

        # Realiza a rotação
        y.esquerda = z
        z.direita = T2

        # Atualiza alturas
        self._atualizar_altura(z)
        self._atualizar_altura(y)

        return y # Nova raiz sub-árvore

    # --- Inserção e Rebalanceamento (Complexidade O(log n)) ---
    def inserir(self, chave, valor=None):
        """Insere e rebalanceia a AVL."""
        self.raiz = self._inserir_recursivo(self.raiz, chave, valor)

    def _inserir_recursivo(self, no, chave, valor):
        # 1. Inserção como BST padrão
        if no is None:
            return NoAVL(chave, valor)
        
        if chave < no.chave:
            no.esquerda = self._inserir_recursivo(no.esquerda, chave, valor)
        elif chave > no.chave:
            no.direita = self._inserir_recursivo(no.direita, chave, valor)
        else:
            return no # Chaves duplicadas não permitidas

        # 2. Atualizar altura do nó pai
        self._atualizar_altura(no)

        # 3. Verificar o Fator de Balanceamento (FB)
        fb = self._get_fb(no)

        # 4. Rebalancear se necessário (FB > 1 ou FB < -1)

        # Caso RR (Rotação Simples Esquerda)
        if fb < -1 and chave > no.direita.chave:
            return self._rotacao_esquerda(no)

        # Caso LL (Rotação Simples Direita)
        if fb > 1 and chave < no.esquerda.chave:
            return self._rotacao_direita(no)

        # Caso LR (Rotação Dupla Esquerda-Direita)
        if fb > 1 and chave > no.esquerda.chave:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        # Caso RL (Rotação Dupla Direita-Esquerda)
        if fb < -1 and chave < no.direita.chave:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    # O método 'buscar' é idêntico ao da BST, e a 'remover' deve seguir a mesma lógica de inserção (remover, atualizar altura e rebalancear).