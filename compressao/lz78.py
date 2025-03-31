def lz78_compress(sequence):
    dictionary = {}
    compressed = []
    current_string = ""
    dict_index = 1

    print(f"Sequência inicial: {sequence}\n")

    for char in sequence:
        current_string += char
        if current_string not in dictionary:
            # Determinar o índice do prefixo
            prefix_index = dictionary.get(current_string[:-1], 0)

            # Adicionar o código (index, char) à lista comprimida
            compressed.append((prefix_index, char))

            # Adicionar a string atual ao dicionário
            dictionary[current_string] = dict_index
            dict_index += 1

            print(f"Dicionário atualizado: {dictionary}")
            print(f"Código gerado: ({prefix_index}, '{char}')\n")

            # Reiniciar a string atual
            current_string = ""

    return compressed


# Exemplo de uso
sequence = "bananabanabofana"

compressed_sequence = lz78_compress(sequence)
print("Sequência comprimida:", compressed_sequence)