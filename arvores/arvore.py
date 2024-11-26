class NoArvore:
    def __init__(self, data):
        self.data = data
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.data)

class ArvoreBinaria:
    def __init__(self, data=None):
        if data:
            no = NoArvore(data)
            self.raiz = no
        else:
            self.raiz = None


if __name__ == "__main__":
    arvore = ArvoreBinaria(2)
    arvore.raiz.esq = NoArvore(1)
    arvore.raiz.dir = NoArvore(3)

    print(arvore.raiz)
    print(arvore.raiz.esq)
    print(arvore.raiz.dir)
