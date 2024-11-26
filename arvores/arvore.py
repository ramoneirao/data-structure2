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
    
    def percursoSimetrico(self, no=None):
        if no is None:
            no = self.raiz
        if no.esq:
            #print('(', end='')
            self.percursoSimetrico(no.esq)
        print(no)
        
        if no.dir:
            self.percursoSimetrico(no.dir)
            #print(')', end='')



if __name__ == "__main__":
    #arvore = ArvoreBinaria(2)
    #arvore.raiz.esq = NoArvore(1)
    #arvore.raiz.dir = NoArvore(3)

    #print(arvore.raiz)
    #print(arvore.raiz.esq)
    #print(arvore.raiz.dir)

    tree = ArvoreBinaria()
    n1 = NoArvore('a')
    n2 = NoArvore('+')
    n3 = NoArvore('*')
    n4 = NoArvore('b')
    n5 = NoArvore('-')
    n6 = NoArvore('/')
    n7 = NoArvore('c')
    n8 = NoArvore('d')
    n9 = NoArvore('e')

    n6.esq = n7
    n6.dir = n8
    n5.esq = n6
    n5.dir = n9
    n3.esq = n4
    n3.dir = n5
    n2.esq = n1
    n2.dir = n3
    
    tree.raiz = n2

    tree.percursoSimetrico()