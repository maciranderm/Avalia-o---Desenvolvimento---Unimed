# 2. Descreva como você implementaria uma pilha (stack) utilizando uma lista (array). Explique como seriam feitas as operações de push, pop e peek.

# # Implementei a pilha usando uma lista e aprovei a estrutura de dados que as listas oferecem. O ultimo item adicionado é o primeiro a ser removido.
# O push foi realizado com o metodo append, que adiciona um item no final da lista que simula o topo da pilha.
# O pop remove o item do topo da pilha. Usei metodo pop da lista para retirar o ultimo item inserido e antes verifica se a pilha nao esta vazia para evitar erros.
# O peek retorna o item no topo da pilha sem remover ele, entao acessamos o ultimo elemento da lista com o indice -1,
# assim garante que a pilha nao esteja vazia antes de acessar o topo.
# Para finalizar adicionei metodos auxiliares com o objetivo verificar se a pilha esta vazia e para a contagem do numero de itens.
# O mostrar_pilha é intuitivo, mostra a pilha em string e isso facilita a visualizacao dos elementos.

class Pilha:
    def iniciar_pilha(self):
        # inicializa a pilha como uma lista vazia
        self.stack = []

    def adicionar(self, item):
        # coloca um item no topo da pilha
        self.stack.append(item)

    def remover(self):
        # tira o item do topo da pilha
        if not self.stack:
            raise IndexError("A pilha está vazia.")
        return self.stack.pop()

    def topo(self):
        # olha o item do topo sem remover
        if not self.stack:
            raise IndexError("A pilha está vazia.")
        return self.stack[-1]

    def vazia(self):
        # verifica se a pilha esta vazia
        return len(self.stack) == 0

    def tamanho(self):
        # conta quantos itens tem na pilha
        return len(self.stack)

    def mostrar_pilha(self):
        # mostra a pilha em formato de lista
        return f"Pilha: {self.stack}"

