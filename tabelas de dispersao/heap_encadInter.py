class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Cada posição é inicializada como None

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            # Insere diretamente se a posição estiver vazia
            self.table[index] = key
        else:
            # Trata a colisão
            print(f"Colisão na posição {index}, tentando inserir em outra posição.")
            inserted = False
            for i in range(self.size - 1, -1, -1):  # Verifica da última posição para a primeira
                if self.table[i] is None:
                    self.table[i] = key
                    print(f"Chave {key} inserida na posição {i}.")
                    inserted = True
                    break
            if not inserted:
                print(f"Erro: não foi possível inserir a chave {key}, tabela cheia.")

    def display(self):
        for i, value in enumerate(self.table):
            print(f"Posição {i}: {value}")


# Exemplo de uso, pág 33
if __name__ == "__main__":
    # Tamanho da tabela é 7
    hash_table = HashTable(7)

    # Chaves a serem inseridas
    keys = [28, 35, 14, 70, 19]

    for key in keys:
        hash_table.insert(key)

    # Exibe a tabela hash
    hash_table.display()