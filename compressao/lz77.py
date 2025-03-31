def lz77_compress(sequence, Nd, Nb):
    """
    Implementação do algoritmo LZ77.
    :param sequence: Sequência de entrada a ser comprimida.
    :param Nd: Tamanho do dicionário.
    :param Nb: Tamanho do buffer.
    :return: Lista de tuplas (p, l, c) representando a sequência comprimida.
    """
    dictionary = ""
    buffer = sequence[:Nb]
    sequence = sequence[Nb:]
    compressed = []

    print(f"Sequência inicial: {sequence}")
    print(f"Tamanho do dicionário: {Nd}, Tamanho do buffer: {Nb}\n")

    while buffer:
        # Encontrar a maior sequência no dicionário que também está no buffer
        match_length = 0
        match_position = 0

        for i in range(len(dictionary)):
            length = 0
            while (i + length < len(dictionary) and
                   length < len(buffer) and
                   dictionary[i + length] == buffer[length]):
                length += 1
            if length > match_length:
                match_length = length
                match_position = len(dictionary) - i

        # Determinar o próximo caractere após a sequência
        next_char = buffer[match_length] if match_length < len(buffer) else ""

        # Adicionar o código (p, l, c) à lista comprimida
        compressed.append((match_position, match_length, next_char))

        # Atualizar o dicionário e o buffer
        shift = match_length + 1
        dictionary += buffer[:shift]
        buffer = buffer[shift:] + sequence[:shift]
        sequence = sequence[shift:]

        # Garantir que o dicionário não exceda o tamanho máximo
        if len(dictionary) > Nd:
            dictionary = dictionary[-Nd:]

        # Exibir o estado atual do dicionário e do buffer
        print(f"Dicionário: '{dictionary}'")
        print(f"Buffer: '{buffer}'")
        print(f"Código gerado: ({match_position}, {match_length}, '{next_char}')\n")

    return compressed


# Exemplo de uso
sequence = "bananabanabofana"
Nd = 6  # Tamanho do dicionário
Nb = 4  # Tamanho do buffer

compressed_sequence = lz77_compress(sequence, Nd, Nb)
print("Sequência comprimida:", compressed_sequence)