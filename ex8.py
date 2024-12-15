# 8. - Escreva um algoritmo que inverta uma string sem utilizar funções nativas da linguagem de programação. Explique a lógica utilizada.

# o meu algoritmo inverteu a string percorrendo seus caracteres de tras para frente com um loop for e range
# de forma manual cada caractere foi adicionado a uma nova string vazia,
# construindo o resultado invertido sem usar reversed() por exemplo

def inverter_string(texto):
    # a string vazia para guardar o texto invertido
    invertida = ""
    
    # loop de tras pra frente
    # Começamos no último caracter e vamos ate o primeiro 
    # ou seja (len(texto) - 1) e (índice 0)
    for i in range(len(texto) - 1, -1, -1):
        # adiciona cada caractere no final da string invertida
        invertida += texto[i]
    
    # retorna a stg invertida
    return invertida

# exemplo para teste
frase = "Eu gosto de estudar psicologia comportamental."
resultado = inverter_string(frase)
# exibicao
print("String original:", frase)
print("String invertida:", resultado)

