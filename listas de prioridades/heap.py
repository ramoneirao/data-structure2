import math

def troca(A, i, j):
    A[i], A[j] = A[j], A[i]

def muda_prioridade(A, i, chave):
    if A[i] > chave:
        A[i] = chave
        heap_diminui_chave(A, len(A) - 1, i)
    else:
        A[i] = chave
        heap_aumenta_chave(A, i)

def heap_diminui_chave(A, n, i):
    j = 2 * i
    while j <= n:
        maior = j
        if maior < n and A[maior] < A[maior + 1]:
            maior += 1
        if A[i] < A[maior]:
            troca(A, i, maior)
            i = maior
            j = 2 * i
        else:
            j = n + 1

def heap_aumenta_chave(A, i):
    j = i // 2
    while i > 1 and A[j] < A[i]:
        troca(A, i, j)
        i = j
        j = i // 2

def heap_insercao(A, n, chave):
    A.append(chave)
    n += 1
    heap_aumenta_chave(A, n)

def heap_remove(A, n):
    if n < 1:
        raise Exception("Heap vazio")
    maximo = A[1]
    A[1] = A[n]
    A.pop()
    n -= 1
    heap_diminui_chave(A, n, 1)
    return maximo

def max_heap(A, n):
    for i in range(n // 2, 0, -1):
        heap_diminui_chave(A, n, i)

def imprime_heap(A, index=1, nivel=0):
    if index < len(A):
        imprime_heap(A, 2 * index + 1, nivel + 1)
        print("\t" * nivel + f"-> {A[index]}")
        imprime_heap(A, 2 * index, nivel + 1)

# Exemplo de uso, pág 14
if __name__ == "__main__":
    # Lista de prioridade inicial (índice 0 não é usado)
    A = [None, 16, 15, 10, 14, 7, 9, 3, 2, 8, 1]
    n = len(A) - 1

    print("Lista de prioridade inicial:")
    print(A[1:])

    print("\nÁrvore do heap:")
    imprime_heap(A)

    # Exemplo de inserção
    print("\nInserindo elemento 20:")
    heap_insercao(A, n, 20)
    n += 1
    imprime_heap(A)

    # Exemplo de remoção
    print("\nRemovendo elemento máximo:")
    maximo = heap_remove(A, n)
    n -= 1
    print(f"Elemento removido: {maximo}")
    imprime_heap(A)