def soma_lista(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

#Função Recursiva 
def soma_lista_(lista):
    if len(lista) == 1: #caso base
        return lista[0]
    else:
        return lista[0] + soma_lista_(lista[1:])


#main
lista = [1, 3, 5, 7, 9]
print(f'Soma: {soma_lista(lista)}')
print(f'Soma da lista recursiva: {soma_lista_(lista)}')

