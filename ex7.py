# 7. Explique como você implementaria uma lista encadeada (linked list) e as operações básicas como inserção, remoção e busca de um elemento.

class Node:
    # representa um no da lista encadeada
    def iniciar(self, data):
        self.data = data  # dados armazenados no no
        self.next = None  # o ponteiro para o proximo no se incia como none

class LinkedList:
    # representa a lista encadeada
    def iniciar(self):
        self.head = None  # de inicio a lista esta vazia, o primeiro no é none

    def inserir(self, data):
        # insercao no final da lista
        # cria um novo no a partir dos dados fornecidos
        new_node = Node(data)
        if not self.head:  # se estiver vazia o novo no vira o primeiro no
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # percorre ate o ultimo no
            last_node = last_node.next
        last_node.next = new_node  # insere o novo no no final

    def remover(self, data):
        # remove um no com o valor especificado
        current_node = self.head
        if current_node and current_node.data == data:  # se o no a ser removido for o primeiro
            self.head = current_node.next  # a head passa a ser o proximo no
            current_node = None
            return
        
        # caso contrario o no é procurado
        prev_node = None
        while current_node and current_node.data != data:  # procura pelo no a ser removido
            prev_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            print("Elemento não encontrado!")
            return
        
        prev_node.next = current_node.next  # remove o no da lista
        current_node = None

    def pesquisar(self, data):
        # procura um no com o valor especificado
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next
        return False

    def exibir(self):
        # mostra todos os elementos da lista
        current_node = self.head
        while current_node:  # percorre todos os nos da lista
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # marca o final da lista

