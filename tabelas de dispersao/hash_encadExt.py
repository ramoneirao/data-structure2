class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Inicializa a tabela com listas vazias (encadeamento externo)

    def hash_function(self, key):
        return key % self.size  # Função hash: h(k) = k mod size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)  # Insere a chave na lista correspondente ao índice calculado

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"T[{i}]: {bucket}")  # Exibe cada posição da tabela e suas listas


# Tamanho da tabela hash
size = 9

# Criação da tabela hash
hash_table = HashTable(size)

# Chaves a serem inseridas
keys = [5, 28, 19, 15, 20, 33]

# Inserção das chaves na tabela hash
for key in keys:
    hash_table.insert(key)

# Exibição da tabela hash final
print("Tabela Hash com Encadeamento Externo:")
hash_table.display()