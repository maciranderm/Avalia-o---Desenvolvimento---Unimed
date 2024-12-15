# 4. Escreva um algoritmo que receba uma lista de números e remova todos os números duplicados. Explique a lógica utilizada e a complexidade do algoritmo.

def remover_duplicados(lista):
    # a funcao set() cria um conjunto que por padrao nao permite elementos duplicados
    # ao converter a lista em um conjunto, automaticamente os duplicados sao removidos
    lista_sem_duplicados = list(set(lista))
    return lista_sem_duplicados

# exemplo pra teste
lista = [1, 2, 3, 4, 1, 2, 3, 6, 71]
resultado = remover_duplicados(lista)
print("Lista sem os duplicados:", resultado)
