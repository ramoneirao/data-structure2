class Heap:
    def __init__(self):
        # Usamos uma lista para armazenar os elementos do heap
        self.heap = []

    def insert(self, item):
        """Insere um item no heap."""
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def remove(self):
        """Remove e retorna o menor item do heap."""
        if self.is_empty():
            raise IndexError("O heap está vazio.")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        # Substitui a raiz pelo último elemento e reorganiza o heap
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        """Retorna o menor item do heap sem removê-lo."""
        if not self.is_empty():
            return self.heap[0]
        raise IndexError("O heap está vazio.")

    def change_priority(self, old_value, new_value):
        """Altera a prioridade de um item no heap."""
        try:
            index = self.heap.index(old_value)  # Encontra o índice do valor antigo
            self.heap[index] = new_value  # Substitui pelo novo valor
            # Reorganiza o heap dependendo do novo valor
            if new_value < old_value:
                self._heapify_up(index)
            else:
                self._heapify_down(index)
        except ValueError:
            raise ValueError("O valor antigo não foi encontrado no heap.")

    def is_empty(self):
        """Verifica se o heap está vazio."""
        return len(self.heap) == 0

    def _heapify_up(self, index):
        """Reorganiza o heap de baixo para cima."""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Troca o elemento com o pai
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        """Reorganiza o heap de cima para baixo."""
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        # Verifica se o filho esquerdo é menor
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        # Verifica se o filho direito é menor
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        # Se o menor não for o nó atual, troca e continua
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __str__(self):
        """Retorna uma representação do heap."""
        return str(self.heap)
    
    def display_tree(self, index=0, indent=0):
        """Exibe a árvore do heap de forma indentada."""
        if index < len(self.heap):
            # Exibe o nó atual com a indentação apropriada
            print(" " * indent + str(self.heap[index]))
            # Exibe o filho esquerdo
            self.display_tree(2 * index + 1, indent + 4)
            # Exibe o filho direito
            self.display_tree(2 * index + 2, indent + 4)


# Exemplo de uso com a lista A
if __name__ == "__main__":
    heap = Heap()
    A = [16, 15, 10, 14, 7, 9, 3, 2, 8, 1]
    
    # Inserindo os elementos da lista A no heap
    for item in A:
        heap.insert(item)
    
    print("Heap após inserções da lista A:", heap)
    print("\nÁrvore do heap:")
    heap.display_tree()
