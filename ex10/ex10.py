# 10. Crie um algoritmo que encontre a sequência de Fibonacci até um determinado número n. Explique a lógica utilizada.

def fibonacci(n):
    # inicia a sequencia com os dois primeiros numeros de fibonacci
    sequence = [0, 1]
    
    # vai adicionando numeros a sequencia enquanto a soma dos dois ultimos numeros for menor ou igual a n
    while sequence[-1] + sequence[-2] <= n:
        # adiciona na sequência a soma dos dois ultimos numeros
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

# pede que o usuario digite um numero
n = int(input("Digite um número: "))
# imprime a sequencia de fibonacci ate o numero n
print(fibonacci(n))
