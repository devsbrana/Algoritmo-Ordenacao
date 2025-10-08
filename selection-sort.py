'''
Algoritmo de ordenação
Selection Sort (Ordenação por seleção)

Trabalha em interações (passes) - elemento por elemento
Troca o elemento, se ele for maior (ou menor)
- aumentando a parte ordenada e diminuindo a parte desordenada

Complexidade de tempo: O(n^2)
'''

def selection_sort(lista):

    '''
    Ordena uma lista usando o algoritmo de ordenação por seleção.
    '''

    tam = len(lista) # obtem o tamanho da lista

    for i in range(tam):
        # assume que o menor elemento é o primeiro elemento não ordenado
        indice_minimo = i # auxiliar 
        for j in range(i + 1, tam):
            # encontra o índice do menor elemento na parte não ordenada da lista
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # realiza a troca do elemento atual com o menor elemento encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

#Programa principal
lista_original = [64, 25, 12, 22, 11]
print(f'Lista Original: {lista_original}')
selection_sort(lista_original)
print(f'Lista Ordenada: {lista_original}')