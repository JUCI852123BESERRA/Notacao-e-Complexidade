### 2. Complexidade de Tempo Linear: O(n)

#Neste caso, o tempo de execução do algoritmo cresce linearmente com o tamanho da entrada (`n`). Se a entrada dobrar de tamanho, o tempo de execução também dobrará. Um exemplo clássico é percorrer todos os elementos de uma lista.

"""python
"""
#Exemplo de Complexidade de Tempo Linear - O(n)


def encontrar_soma(lista):
    """
    Esta função calcula a soma de todos os elementos na lista.
    A função precisa percorrer cada elemento da lista uma vez.
    Se a lista dobrar de tamanho, o tempo de execução também dobrará.
    Portanto, a complexidade é O(n).
    """
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

# Exemplo de uso:
minha_lista = [1, 2, 3, 4, 5]
print(f"A soma é: {encontrar_soma(minha_lista)}")

outra_lista = list(range(101)) # Lista de 0 a 100
print(f"A soma de uma lista maior é: {encontrar_soma(outra_lista)}")