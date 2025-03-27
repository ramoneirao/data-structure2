class NoRubroNegro:
    def __init__(self, chave):
        self.chave = chave
        self.cor = "VERMELHO"  # Todos os novos nós começam como vermelhos
        self.esquerda = None
        self.direita = None
        self.pai = None


class ArvoreRubroNegra:
    def __init__(self):
        self.NIL = NoRubroNegro(None)  # Nó NIL (nó folha)
        self.NIL.cor = "PRETO"
        self.raiz = self.NIL

    def rotacao_esquerda(self, x):
        print(f"Rotação à esquerda no nó {x.chave}")
        y = x.direita
        x.direita = y.esquerda
        if y.esquerda != self.NIL:
            y.esquerda.pai = x
        y.pai = x.pai
        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y
        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, y):
        print(f"Rotação à direita no nó {y.chave}")
        x = y.esquerda
        y.esquerda = x.direita
        if x.direita != self.NIL:
            x.direita.pai = y
        x.pai = y.pai
        if y.pai is None:
            self.raiz = x
        elif y == y.pai.direita:
            y.pai.direita = x
        else:
            y.pai.esquerda = x
        x.direita = y
        y.pai = x

    def inserir(self, chave):
        novo_no = NoRubroNegro(chave)
        novo_no.esquerda = self.NIL
        novo_no.direita = self.NIL
        novo_no.pai = None

        pai = None
        atual = self.raiz

        while atual != self.NIL:
            pai = atual
            if novo_no.chave < atual.chave:
                atual = atual.esquerda
            else:
                atual = atual.direita

        novo_no.pai = pai
        if pai is None:
            self.raiz = novo_no
        elif novo_no.chave < pai.chave:
            pai.esquerda = novo_no
        else:
            pai.direita = novo_no

        novo_no.cor = "VERMELHO"
        self._ajustar_insercao(novo_no)

    def _ajustar_insercao(self, no):
        while no.pai and no.pai.cor == "VERMELHO":
            if no.pai == no.pai.pai.esquerda:
                tio = no.pai.pai.direita
                if tio and tio.cor == "VERMELHO":
                    print(f"Recolorindo: pai {no.pai.chave}, tio {tio.chave}, e avô {no.pai.pai.chave}")
                    no.pai.cor = "PRETO"
                    tio.cor = "PRETO"
                    no.pai.pai.cor = "VERMELHO"
                    no = no.pai.pai
                else:
                    if no == no.pai.direita:
                        no = no.pai
                        self.rotacao_esquerda(no)
                    no.pai.cor = "PRETO"
                    no.pai.pai.cor = "VERMELHO"
                    self.rotacao_direita(no.pai.pai)
            else:
                tio = no.pai.pai.esquerda
                if tio and tio.cor == "VERMELHO":
                    print(f"Recolorindo: pai {no.pai.chave}, tio {tio.chave}, e avô {no.pai.pai.chave}")
                    no.pai.cor = "PRETO"
                    tio.cor = "PRETO"
                    no.pai.pai.cor = "VERMELHO"
                    no = no.pai.pai
                else:
                    if no == no.pai.esquerda:
                        no = no.pai
                        self.rotacao_direita(no)
                    no.pai.cor = "PRETO"
                    no.pai.pai.cor = "VERMELHO"
                    self.rotacao_esquerda(no.pai.pai)
        self.raiz.cor = "PRETO"

    def exibir_arvore(self, no, nivel=0):
        if no != self.NIL:
            self.exibir_arvore(no.direita, nivel + 1)
            cor = "V" if no.cor == "VERMELHO" else "P"
            print("    " * nivel + f"-> {no.chave}({cor})")
            self.exibir_arvore(no.esquerda, nivel + 1)

## Resolvendo o exercício da pág 17-18 
if __name__ == "__main__":
    arvore = ArvoreRubroNegra()

    # Inserindo elementos na árvore Rubro-Negra
    elementos = [11,2,14,1,7,13,15,5,8,4]
    for elemento in elementos:
        arvore.inserir(elemento)

    # Exibindo a árvore
    print("\n\nÁrvore Rubro-Negra com indentação:")
    arvore.exibir_arvore(arvore.raiz)