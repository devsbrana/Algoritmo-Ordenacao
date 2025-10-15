"""
Recursão - conceito de programação no qual uma função chama a si mesma para resolver um problema específico

Componenets essencias da recursão:
1. Caso base - condição que encerra a recursão
2. Passo da recursão (step) 

menu() >>> add() >>> menu() >>> sub() >>> mult() >>> menu() 
"""

# Exemplo 1: Somatória de todos elementos de uma lista de fomar (recursiva)
def somatorio(lista):
    if len(lista) == 1:  # Caso base
        return lista[0]
    else:
        return lista[0] + somatorio(lista[1:])  # Passo da recursão
    
# Exemplo 2: Calculo do Fatorial de um número - 5! = 5*4*3*2*1
# 1 é o caso base do calculo do fatorial
# 0! = 1

def fatorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * fatorial(n - 1)  # Passo da recursão

    
# Programa principal
lista = [1, 3, 5, 7, 9]
print(f'Somatório: {somatorio(lista)}')
print(f'Fatorial: {fatorial(5)}')