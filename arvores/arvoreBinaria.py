# Classe para o nó
class Node:
     
    def __init__(self, chave, direita, esquerda):
        self.valor = chave
        self.dir = direita
        self.esq = esquerda


# Classe para a árvore
class Tree:

    def __init__(self):
        self.raiz = Node(None,None,None)
        self.raiz = None

  # Insere um nó na árvore
    def insert(self, valor):
        novo = Node(valor,None,None) 
        if self.raiz == None:
            self.raiz = novo
        else: 
            atual = self.raiz
            while True:
                anterior = atual
                if valor <= atual.valor: 
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return             
                else: 
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return

  # Busca um nó na árvore              
    def search(self, chave):
        if self.raiz == None:
            return None 
        atual = self.raiz 
        while atual.valor != chave: 
            if chave < atual.valor:
                atual = atual.esq 
            else:
                atual = atual.dir 
                if atual == None:
                    return None
        return atual   

  # Devolve o nó sucessor
    def noSucessor(self, apaga): 
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir

        while atual != None: 
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq 

        if sucessor != apaga.dir: 
            paidosucessor.esq = sucessor.dir 
            sucessor.dir = apaga.dir 

        return sucessor

  # Remove um nó da árvore
    def searchAndRemove(self, valor):
        if self.raiz == None:
            return False 
        atual = self.raiz
        pai = self.raiz
        filhoEsq = True

        # Buscando o nó
        while atual.valor!= valor:
            pai = atual
            if valor < atual.valor: 
                atual = atual.esq
                filhoEsq = True 
            else: 
                atual = atual.dir 
                filhoEsq = False 
            if atual == None:
                return False
         
        if atual.esq == None and atual.dir == None:
            if atual == self.raiz:
                self.raiz = None 
            else:
                if filhoEsq:
                    pai.esq =  None 
                else:
                    pai.dir = None 

        elif atual.dir == None:
            if atual == self.raiz:
                self.raiz = atual.esq 
            else:
                if filhoEsq:
                    pai.esq = atual.esq 
                else:
                    pai.dir = atual.esq 
         
        elif atual.esq == None:
            if atual == self.raiz:
                self.raiz = atual.dir 
            else:
                if filhoEsq:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir 

        else:
            sucessor = self.noSucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            else:
                if filhoEsq:
                    pai.esq = sucessor 
                else:
                    pai.dir = sucessor 
            sucessor.esq = atual.esq   

    # Mostra a árvore

    def mostrarArvore(self, node, level=0, prefix="Root: \n"):
        if node is not None:
            print("  " * level + prefix + str(node.valor))
            if node.esq or node.dir:
                self.mostrarArvore(node.esq, level + 1, "L--- ")
                self.mostrarArvore(node.dir, level + 1, "R--- ")

        return True


arvore = Tree()
opcao = 0

while opcao != 5:
    print("MENU:\n")
    print("1 - INSERIR \n2 - EXCLUIR \n3 - BUSCAR \n4 - MOSTRAR ÁRVORE \n5 - SAIR")
    
    opcao = int(input("-> "))
    if opcao == 1:
        valor = int(input("Digite o valor que deseja inserir: "))
        arvore.insert(valor)
        print("O valor foi inserido com sucesso!")
        print("Voltando ao menu")
    
    elif opcao == 2:
        valor = int(input("Digite o valor que deseja excluir: "))
        if arvore.searchAndRemove(valor) == True:
            print("Removido com sucesso!")
        else:
            print("O valor não foi encontrado")
        print("Voltando ao menu")

    elif opcao == 3:
        valor = int(input("Digite o valor que deseja buscar: "))
        if arvore.search(valor) != None:
            print(f"O núemro {valor} foi encontrado na árvore")
        else:
            print(f"O número {valor} não foi encontrado na árvore")
        print("Voltando ao menu")

    elif opcao == 4:
        print("Árvore: ", end='')
        arvore.mostrarArvore(arvore.raiz)
        print("\nVoltando ao menu")

    elif opcao == 5:
        break