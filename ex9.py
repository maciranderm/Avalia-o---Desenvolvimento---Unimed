# 9. Descreva como você abordaria a criação de um algoritmo para resolver o problema de encontrar todos os pares de números em um array cuja soma é igual a um valor específico.

# primeiro crio uma funcao que receba o array e o valor alvo como parametros
# entao uso um dicionario para armazenar os numeros encontrados e que possam formar par com os proximos numeros do array
# logo percorro o array e para cada numero, calculo a diferenca entre o valor que quero (chamei de alvo) e o numero atual
# verifico se a diferenca ja este no dicionario, se estiver eu encontroi um par
# por fim adicionei o numero atual no dicionario para que ele possa ser usado para formar pares com os proximos numeros

def encontrar_pares(array, alvo):
    pares = []
    numeros_vistos = {}
    
    for numero in array:
        diferenca = alvo - numero
        if diferenca in numeros_vistos:
            pares.append((diferenca, numero))
        numeros_vistos[numero] = True
    
    return pares

# Exemplo de uso
array = [2, 4, 3, 5, 7, 8, 9, 1, 11, 34, 100]
alvo = 7
print(encontrar_pares(array, alvo))

