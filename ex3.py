# 3. Explique como você implementaria uma fila (queue) utilizando duas pilhas (stacks). Inclua a lógica das operações de enfileiramento (enqueue) e desenfileiramento (dequeue).
 
# Basicamente a solucao mais simples para mim foi uma pilha para enfileirar elementos e outra para desenfileirar.
# A logica esta em transferir os elementos da pilha de entrada para a de saida so quando necessario, mantendo os elementos em ordem.
# Alem disso, implementei os metodos essenciais de uma fila (adicionar, remover, primeiro, esta_vazia e tamanho) para cobrir todas as operacoes fundamentais.
# A solucao é simples e evita a necessidade de suporte externo, apenas com listas nativas do python.

class FilaComDuasPilhas:
    def iniciar(self):
        # inicia com duas pilhas: uma para entrada e outra para saida
        self.pilha_entrada = []
        self.pilha_saida = []

    def adicionar(self, elemento):
        # enfileira o elemento e adiciona ele na pilha de entrada
        self.pilha_entrada.append(elemento)
        print(f"O elemento '{elemento}' foi adicionado na fila.")

    def remover(self):
        # remove o elemento da frente da fila (o primeiro adicionado)
        if not self.pilha_saida:
            if not self.pilha_entrada:
                raise IndexError("A fila está vazia, então não há elementos para remover.")
            # transferimos os elementos da pilha de entrada para a de saida
            while self.pilha_entrada:
                self.pilha_saida.append(self.pilha_entrada.pop())
        return self.pilha_saida.pop()

    def primeiro(self):
        # retorna o elemento da frente da fila sem remover ele
        if not self.pilha_saida:
            if not self.pilha_entrada:
                raise IndexError("A fila está vazia, então não há elementos para visualizar.")
            while self.pilha_entrada:
                self.pilha_saida.append(self.pilha_entrada.pop())
        return self.pilha_saida[-1]

    def esta_vazia(self):
        # verifica se a fila esta vazia
        return not self.pilha_entrada and not self.pilha_saida

    def tamanho(self):
        # retorna o numero total de elementos na fila
        return len(self.pilha_entrada) + len(self.pilha_saida)
