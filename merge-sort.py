"""
Algoritmo Merge Sort - Ordenação por intercalação ou fusão
- Algoritmo recursivo
- Divide a lista em sublistas até que cada sublista contenha um único elemento
- Intercala as sublistas para produzir novas sublistas ordenadas até que haja apenas uma sublista restante, que será a lista ordenada

Complexidade de tempo: O(n log n)
"""

def merge_sort(lista):
    """
    Algoritmo Merge Sort - Ordenação por intercalação ou fusão
    """
    if len(lista) > 1:

        meio = len(lista) // 2  # divisão inteira

        # fatia a lista em duas metades
        L = lista[:meio]  # sublista esquerda
        R = lista[meio:]  # sublista direita

        # chamada recursiva em cada metade
        merge_sort(L)
        merge_sort(R)

        # variáveis de controle
        # i - fara o controle da sublista esquerda
        # j - fara o controle da sublista direita
        # k - fara o controle da lista principal
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1


        # verifica dos elementos da lista L
        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        # verifica dos elementos da lista R
        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

# Programa principal
lista = [38, 27, 43, 3, 9, 82, 10]
print(f'Lista Original: {lista}')
merge_sort(lista)
print(f'Lista Ordenada: {lista}')
