class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def obter_altura(self, no):
        if not no:
            return 0
        return no.altura

    def obter_balanceamento(self, no):
        if not no:
            return 0
        return self.obter_altura(no.esquerda) - self.obter_altura(no.direita)

    def rotacao_direita(self, y):
        print(f"Rotação à direita no nó {y.chave}")
        x = y.esquerda
        T2 = x.direita

        # Realiza a rotação
        x.direita = y
        y.esquerda = T2

        # Atualiza as alturas
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))
        x.altura = 1 + max(self.obter_altura(x.esquerda), self.obter_altura(x.direita))

        return x

    def rotacao_esquerda(self, x):
        print(f"Rotação à esquerda no nó {x.chave}")
        y = x.direita
        T2 = y.esquerda

        # Realiza a rotação
        y.esquerda = x
        x.direita = T2

        # Atualiza as alturas
        x.altura = 1 + max(self.obter_altura(x.esquerda), self.obter_altura(x.direita))
        y.altura = 1 + max(self.obter_altura(y.esquerda), self.obter_altura(y.direita))

        return y

    def inserir(self, raiz, chave):
        # Realiza a inserção normal de uma BST
        if not raiz:
            print(f"Inserindo o nó {chave}")
            return No(chave)
        elif chave < raiz.chave:
            raiz.esquerda = self.inserir(raiz.esquerda, chave)
        else:
            raiz.direita = self.inserir(raiz.direita, chave)

        # Atualiza a altura do nó ancestral
        raiz.altura = 1 + max(self.obter_altura(raiz.esquerda), self.obter_altura(raiz.direita))

        # Obtém o fator de balanceamento
        balanceamento = self.obter_balanceamento(raiz)

        # Balanceia a árvore
        # Caso Esquerda-Esquerda
        if balanceamento > 1 and chave < raiz.esquerda.chave:
            return self.rotacao_direita(raiz)

        # Caso Direita-Direita
        if balanceamento < -1 and chave > raiz.direita.chave:
            return self.rotacao_esquerda(raiz)

        # Caso Dupla à Esquerda
        if balanceamento > 1 and chave > raiz.esquerda.chave:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Caso Dupla à Direita
        if balanceamento < -1 and chave < raiz.direita.chave:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def remover(self, raiz, chave):
        # Passo 1: Realiza a remoção normal de uma BST
        if not raiz:
            return raiz

        if chave < raiz.chave:
            raiz.esquerda = self.remover(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.remover(raiz.direita, chave)
        else:
            print(f"Removendo o nó {chave}")
            # Nó com apenas um filho ou nenhum
            if not raiz.esquerda:
                temp = raiz.direita
                raiz = None
                return temp
            elif not raiz.direita:
                temp = raiz.esquerda
                raiz = None
                return temp

            # Nó com dois filhos: Obtém o sucessor em ordem (menor na subárvore direita)
            temp = self.get_min_value_node(raiz.direita)
            print(f"Substituindo o nó {raiz.chave} pelo sucessor {temp.chave}")
            raiz.chave = temp.chave
            raiz.direita = self.remover(raiz.direita, temp.chave)

        # Se a árvore tiver apenas um nó, basta retornar
        if not raiz:
            return raiz

        # Passo 2: Atualiza a altura do nó atual
        raiz.altura = 1 + max(self.obter_altura(raiz.esquerda), self.obter_altura(raiz.direita))

        # Passo 3: Obtém o fator de balanceamento
        balanceamento = self.obter_balanceamento(raiz)

        # Passo 4: Balanceia a árvore
        # Caso Esquerda
        if balanceamento > 1 and self.obter_balanceamento(raiz.esquerda) >= 0:
            return self.rotacao_direita(raiz)

        # Caso Duplo à Esquerda
        if balanceamento > 1 and self.obter_balanceamento(raiz.esquerda) < 0:
            raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            return self.rotacao_direita(raiz)

        # Caso Direita
        if balanceamento < -1 and self.obter_balanceamento(raiz.direita) <= 0:
            return self.rotacao_esquerda(raiz)

        # Caso Duplo à Direita
        if balanceamento < -1 and self.obter_balanceamento(raiz.direita) > 0:
            raiz.direita = self.rotacao_direita(raiz.direita)
            return self.rotacao_esquerda(raiz)

        return raiz

    def get_min_value_node(self, no):
        # Função auxiliar para encontrar o nó com o menor valor (mais à esquerda)
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def exibir_arvore(self, raiz, nivel=0):
        if raiz is not None:
            self.exibir_arvore(raiz.direita, nivel + 1)
            print("    " * nivel + f"-> {raiz.chave}")
            self.exibir_arvore(raiz.esquerda, nivel + 1)


# Exemplo do Slide AVL Remoção 
if __name__ == "__main__":
    arvore = ArvoreAVL()
    raiz = None

    # Inserindo elementos na árvore AVL
    elementos = [10, 5, 17, 3, 7, 15, 19, 4, 13, 16, 20, 12]
    for elemento in elementos:
        raiz = arvore.inserir(raiz, elemento)
    # Removendo 7
    raiz = arvore.remover(raiz, 7)

    # Exibindo a árvore em pré-ordem
    print("\n\nÁrvore AVL com indentação:")
    arvore.exibir_arvore(raiz)



# # Exemplo do Slide AVL Inserção - pag 16
# if __name__ == "__main__":
#     arvore = ArvoreAVL()
#     raiz = None

#     # Inserindo elementos na árvore AVL
#     elementos = [10, 6, 15, 3, 7, 17, 2, 4, 16]
#     for elemento in elementos:
#         raiz = arvore.inserir(raiz, elemento)


#     # Exibindo a árvore em pré-ordem
#     print("\n\nÁrvore AVL com indentação:")
#     arvore.exibir_arvore(raiz)
