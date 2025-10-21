### 3. Complexidade de Tempo Quadrática: O(n²)

# O tempo de execução de um algoritmo com complexidade quadrática é proporcional ao quadrado do tamanho da entrada.
# Isso geralmente ocorre quando existem loops aninhados.

'''
Exemplo de Complexidade de Tempo Quadrática - O(n^2)
'''

def encontrar_todos_os_pares(lista):
    '''
    Esta função gera todos os pares possíveis de elementos na lista.
    Ela usa dois loops aninhados. Para cada elemento, ela percorre a lista inteira novamente.
    Se a lista tem 'n' elementos, o número de operações é aproximadamente n * n.
    Portanto, a complexidade é O(n^2).
    '''
    pares = []
    # Loop externo: executa 'n' vezes
    for item1 in lista:
        # Loop interno: executa 'n' vezes para cada execução do loop externo
        for item2 in lista:
            pares.append((item1, item2))
    return pares


# Exemplo de uso:
minha_lista = [1, 2, 3] # n = 3. Esperado: 3 * 3 = 9 pares.
pares_pequena = encontrar_todos_os_pares(minha_lista)
print(f"Lista: {minha_lista}")
print(f"Pares encontrados (tamanho da lista: {len(minha_lista)}): {len(pares_pequena)} pares")
# print(f"Todos os pares: {pares_pequena}")

print("-" * 30)

# Com uma lista um pouco maior, o número de operações cresce drasticamente (5*5=25).
outra_lista = ['a', 'b', 'c', 'd', 'e'] # n = 5. Esperado: 5 * 5 = 25 pares.
pares_grande = encontrar_todos_os_pares(outra_lista)
print(f"Lista: {outra_lista}")
print(f"Pares encontrados (tamanho da lista: {len(outra_lista)}): {len(pares_grande)} pares")
# print(f"Todos os pares: {pares_grande}")