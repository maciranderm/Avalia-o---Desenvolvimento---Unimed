# 6. Desenvolva um algoritmo para encontrar o maior e o menor número em um array de inteiros. Explique a lógica utilizada.

def achar_maior_menor(lista):
    # assume que o primeiro numero é o maior e o menor
    maior = menor = lista[0]
    
    # percorre a lista a partir do primeiro numero
    # se encontrar um numero maior vai atualizar o maior
    for numero in lista:
        if numero > maior:
            maior = numero
        # se encontrar um numero menor vai atualiza o menor
        if numero < menor:
            menor = numero
    
    # retorna o maior e o menor numero
    return maior, menor

numeros = [3, 5, 1, 8, 4, 2]
maior, menor = achar_maior_menor(numeros)
print(f'O maior número é {maior} e o menor número é {menor}')
