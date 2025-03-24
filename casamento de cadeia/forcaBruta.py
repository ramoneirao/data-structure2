def forca_bruta(texto, padrao):
    ocorrencias = []
    n = len(texto)
    m = len(padrao)

    for i in range(n - m + 1):  # Percorre o texto até a última posição possível
        j = 0
        while j < m and texto[i + j] == padrao[j]:  # Compara caractere a caractere
            j += 1
        if j == m:  # Se percorreu todo o padrão, houve uma correspondência
            ocorrencias.append(i)

    return ocorrencias


# Leitura do arquivo
with open('casamento de cadeia/texto.txt', 'r') as file:
    texto = file.read()

padrao = "abc"
print(forca_bruta(texto, padrao))  # Saída esperada: [2, 5, 8]
