#Algoritmo Bubble Sort
#Complexidade: O(n^2)

def bubble_sort(seq):
    tam = len(seq)

    for i in range(tam - 1):
        troca = False #flag de controle
        for j in range(0, tam-i-1):
            if seq[j] > seq[j+1]:
                troc = True
                #atribuição paralela:
                seq[j], seq[j+i] = seq[j+1], seq[j]
        #se não for necessário realizar troca, o programa irá sair do looping
        if not troca:
            return
        
#Programa Principal
lista = [39, 12, 18, 85, 72, 10, 2, 18]
print(f'Lista Original: {lista}')
bubble_sort(lista)
print(f'Lista Ordenada: {lista}')