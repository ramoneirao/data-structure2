class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.fim_palavra = False


class ArvoreTrie:
    def __init__(self):
        self.raiz = NoTrie()

    def inserir(self, palavra):
        no_atual = self.raiz
        for char in palavra:
            if char not in no_atual.filhos:
                no_atual.filhos[char] = NoTrie()
            no_atual = no_atual.filhos[char]
        no_atual.fim_palavra = True

    def buscar(self, palavra):
        no_atual = self.raiz
        for char in palavra:
            if char not in no_atual.filhos:
                return False
            no_atual = no_atual.filhos[char]
        return no_atual.fim_palavra

    def exibir(self, no=None, prefixo=""):
        if no is None:
            no = self.raiz
        if no.fim_palavra:
            print(prefixo)
        for char, filho in no.filhos.items():
            self.exibir(filho, prefixo + char)

    def mostrar_arvore(self, no=None, nivel=0):
        if no is None:
            no = self.raiz
        for char, filho in no.filhos.items():
            print("    " * nivel + f"'{char}' -> {'(Fim)' if filho.fim_palavra else ''}")
            self.mostrar_arvore(filho, nivel + 1)


# Oerções com a Árvore Trie - pág  32
if __name__ == "__main__":
    arvore = ArvoreTrie()

    # Inserindo palavras na Árvore Trie
    palavras = ["amy", "ann", "emma", "rob", "roger", "anne", "ro"]
    for palavra in palavras:
        arvore.inserir(palavra)

    # É membro?
    print("\nÉ membro?:")
    print("ro:", arvore.buscar("ro"))

    # Exibindo a Árvore Trie
    print("\nPalavras na Árvore Trie:")
    arvore.exibir()

    # Mostrando a estrutura da Árvore Trie
    print("\nEstrutura da Árvore Trie:")
    arvore.mostrar_arvore()