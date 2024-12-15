# 5. Crie um algoritmo que calcule o fatorial de um número inteiro positivo utilizando uma estrutura de repetição (loop). Explique a lógica utilizada.

def calcular_fatorial(numero):
    # iniciei o resultado como 1 pois o fatorial de 0 e 1 é 1, e a multiplicacao do fatorial inicia com 1
    resultado = 1
    
    # o loop percorre cada numero de 1 ate o numero informado, cada interacao do loop multiplica o resultado atual pelo numero correspondente
    # a cada ciclo do loop o valor de i que começa em 1 e vai ate o "numero" é multiplicado pelo valor de "resultado", assim fazendo o calculo do fatorial
    for i in range(1, numero + 1):
        resultado *= i
    
    # depois do loop o "resultado" vai conter o valor do fatorial do numero fornecido
    return resultado

numero = int(input("Digite um número inteiro positivo: "))

# aqui ha a verificacao de que o numero é positivo, se ele é maior ou igual a 0
if numero >= 0:
    # se for valido a funcao calcula o fatorial e entao mostramos o resultado
    print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")
else:
    # e se for negativo da erro, entao exibe a mensagem abaixo
    print("Digite um número inteiro positivo")

