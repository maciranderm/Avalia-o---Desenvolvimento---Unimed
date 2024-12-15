# 1. Escreva um algoritmo que receba um número inteiro positivo e calcule a soma de todos os números ímpares até esse número. Explique a lógica utilizada.

def soma_impar(numero):
    # soma com 0 para acumular a soma dos numeros impares.
    soma = 0
    # percorre todos os numeros de 1 até o numero
    for i in range(1, numero + 1):
        # analisa se o numero atual e impar usando %
        # é ímpar se o resto da divisao por 2 for diferente de 0
        if i % 2 != 0:
            # caso seja impar adiciona ele a variavel soma
            soma += i
    # depois do loop retornq o valor que acumulou na variavel soma
    return soma

# exemplo de teste
numero = int(input("Digite um número inteiro positivo: "))
resultado = soma_impar(numero)
print(f"A soma de todos os números ímpares até {numero} é: {resultado}")
