class NoPatricia:
    def __init__(self, chave=None, folha=False):
        self.chave = chave  # Parte da chave armazenada no nó
        self.esquerda = None  # Subárvore esquerda
        self.direita = None  # Subárvore direita
        self.folha = folha  # Indica se é uma folha


class ArvorePatricia:
    def __init__(self):
        self.raiz = None

    def inserir(self, chave_binaria):
        if not self.raiz:
            self.raiz = NoPatricia()
        
        no_atual = self.raiz
        for bit in chave_binaria:
            if bit == '0':
                if not no_atual.esquerda:
                    no_atual.esquerda = NoPatricia()
                no_atual = no_atual.esquerda
            else:  # bit == '1'
                if not no_atual.direita:
                    no_atual.direita = NoPatricia()
                no_atual = no_atual.direita
        
        # Marcar o nó como folha e armazenar a chave
        no_atual.folha = True
        no_atual.chave = chave_binaria

    def buscar(self, chave_binaria):
        no_atual = self.raiz
        for bit in chave_binaria:
            if bit == '0':
                if not no_atual.esquerda:
                    return False
                no_atual = no_atual.esquerda
            else:  # bit == '1'
                if not no_atual.direita:
                    return False
                no_atual = no_atual.direita
        
        return no_atual.folha and no_atual.chave == chave_binaria

    def exibir(self, no=None, prefixo="", nivel=0):
        if no is None:
            no = self.raiz
        if no.folha:
            # Exibir o valor correspondente à chave binária
            valor = self.converter_binario_para_valor(no.chave)
            print(" " * (nivel * 4) + f"└── Valor: {valor}")
        else:
            # Exibir os bits diferenciais
            print(" " * (nivel * 4) + f"└── Bit diferencial: {prefixo}")
        if no.esquerda:
            print(" " * (nivel * 4) + "    ├── 0:")
            self.exibir(no.esquerda, prefixo + "0", nivel + 1)
        if no.direita:
            print(" " * (nivel * 4) + "    └── 1:")
            self.exibir(no.direita, prefixo + "1", nivel + 1)

    def converter_binario_para_valor(self, chave_binaria):
        # Converte a chave binária para o valor correspondente (caractere)
        return chr(int(chave_binaria, 2) + 65)

# Operações com a Árvore Patricia Binária
if __name__ == "__main__":
    arvore = ArvorePatricia()

    # Inserindo chaves binárias na Árvore Patricia Binária
    chaves_binarias = [
        "010010",  # B
        "100001",  # J
        "011000",  # H
        "101000",  # Q
        "010011",  # C
        "100010"   # K
    ]
    for chave in chaves_binarias:
        arvore.inserir(chave)

    # Buscando chaves na Árvore Patricia Binária
    print("\nBuscando chaves:")
    for chave in chaves_binarias:
        print(f"{chave}: {arvore.buscar(chave)}")
    print("000000:", arvore.buscar("000000"))  # Chave inexistente

    # Exibindo a estrutura da Árvore Patricia Binária
    print("\nEstrutura da Árvore Patricia Binária:")
    arvore.exibir()