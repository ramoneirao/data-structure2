class HashTableQuadraticProbing:
    def __init__(self, size, c1=1, c2=3):
        self.size = size
        self.table = [None] * size
        self.c1 = c1
        self.c2 = c2

    def hash_function(self, key):
        return key % self.size

    def quadratic_probing(self, key):
        initial_index = self.hash_function(key)
        for j in range(self.size):
            index = (initial_index + self.c1 * j + self.c2 * j ** 2) % self.size
            if self.table[index] is None:  # Encontra uma posição vazia
                return index
            else:
                print(f"A chave {key} não pode ser colocada no índice {index}, tentando colocar no índice {(initial_index + self.c1 * (j + 1) + self.c2 * (j + 1) ** 2) % self.size}")
        raise Exception("Tabela hash está cheia!")

    def insert(self, key):
        index = self.quadratic_probing(key)
        self.table[index] = key

    def display(self):
        for i, value in enumerate(self.table):
            print(f"Índice {i}: {value}")


# Exemplo de uso, pág 45
if __name__ == "__main__":
    # Tamanho da tabela hash (potência de 2 ou número primo)
    tamanho_tabela = 11
    chaves = [10, 22, 31, 4, 15, 28, 59]

    # Inicializa a tabela hash
    tabela_hash = HashTableQuadraticProbing(tamanho_tabela)

    # Insere as chaves na tabela
    for chave in chaves:
        tabela_hash.insert(chave)

    # Exibe a tabela hash
    tabela_hash.display()