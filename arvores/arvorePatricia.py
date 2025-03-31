class PatriciaNode:
    def __init__(self, bit_index=None, key=None):
        self.bit_index = bit_index  # Índice do bit usado para dividir
        self.key = key  # Chave armazenada (somente em folhas)
        self.left = None  # Subárvore esquerda
        self.right = None  # Subárvore direita

class PatriciaTrie:
    def __init__(self):
        self.root = None

    def insert(self, key, binary_key):
        if self.root is None:
            # Primeira chave inserida
            self.root = PatriciaNode(key=key)
            return

        current = self.root
        parent = None
        direction = None

        # Caminhar pela árvore até encontrar o ponto de inserção
        while current.bit_index is not None and current.bit_index < len(binary_key):
            parent = current
            direction = 'left' if binary_key[current.bit_index] == '0' else 'right'
            current = current.left if direction == 'left' else current.right

        # Encontrar o primeiro bit diferente entre a nova chave e a chave existente
        existing_binary_key = self._key_to_binary(current.key)
        differing_bit = self._find_first_differing_bit(existing_binary_key, binary_key)

        # Criar um novo nó interno para dividir as chaves
        new_internal_node = PatriciaNode(bit_index=differing_bit)
        new_leaf_node = PatriciaNode(key=key)

        # Determinar a direção do novo nó folha
        if binary_key[differing_bit] == '0':
            new_internal_node.left = new_leaf_node
            new_internal_node.right = current
        else:
            new_internal_node.right = new_leaf_node
            new_internal_node.left = current

        # Atualizar o pai para apontar para o novo nó interno
        if parent is None:
            self.root = new_internal_node
        else:
            if direction == 'left':
                parent.left = new_internal_node
            else:
                parent.right = new_internal_node

    def _key_to_binary(self, key):
        # Converte a chave para uma representação binária fixa
        binary_map = {
            'B': '010010',
            'J': '100001',
            'H': '011000',
            'Q': '101000',
            'C': '010011',
            'K': '100010'
        }
        return binary_map[key]

    def _find_first_differing_bit(self, key1, key2):
        # Encontra o primeiro bit diferente entre duas chaves binárias
        for i in range(min(len(key1), len(key2))):
            if key1[i] != key2[i]:
                return i
        return len(key1)  # Caso todas sejam iguais até o final

    def display(self, node=None, prefix=""):
        # Exibe a árvore para fins de depuração
        if node is None:
            node = self.root

        if node.key is not None:
            print(f"{prefix}[{node.key}]")
        else:
            print(f"{prefix}({node.bit_index})")
            if node.left:
                self.display(node.left, prefix + " 0->")
            if node.right:
                self.display(node.right, prefix + " 1->")


# Exemplo slide pág 11: Uso da árvore PATRICIA
if __name__ == "__main__":
    trie = PatriciaTrie()
    keys = ['B', 'J', 'H', 'Q', 'C', 'K']
    for key in keys:
        binary_key = trie._key_to_binary(key)
        trie.insert(key, binary_key)

    print("Árvore PATRICIA:")
    trie.display()