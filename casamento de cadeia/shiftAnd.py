def shift_and_search_with_table(pattern, text):
    m = len(pattern)
    n = len(text)
    
    # Construção da tabela de máscaras de bits
    mask = {}
    for char in set(text):  # Inicializa todas as máscaras como 0
        mask[char] = 0
    for i, char in enumerate(pattern):  # Define as máscaras para os caracteres do padrão
        mask[char] |= (1 << i)
    
    # Inicializa o estado de correspondência
    state = 0
    match_bit = 1 << (m - 1)  # Bit mais significativo do padrão
    matches = []

    # Tabela para exibição
    table = []

    # Processa o texto
    for i in range(n):
        char = text[i]
        previous_state = state
        state = ((state << 1) | 1) & mask.get(char, 0)
        table.append({
            "Texto": char,
            "(R >> 1) | 10^(m-1)": bin((previous_state << 1) | 1)[2:].zfill(m),
            "R'": bin(state)[2:].zfill(m)
        })
        if state & match_bit:  # Verifica se o bit mais significativo está ativo
            matches.append(i - m + 1)  # Adiciona o índice da correspondência

    return mask, matches, table


# Exemplo de uso
pattern = "teste"
text = "os testes"
mask_table, match_indices, state_table = shift_and_search_with_table(pattern, text)

# Exibe as tabelas de máscaras
print("Tabela de Máscaras:")
for char, mask in mask_table.items():
    print(f"{char}: {bin(mask)[2:].zfill(len(pattern))}")

# Exibe a tabela de estados
print("\nTabela de Estados:")
print(f"{'Texto':<6} {'(R >> 1) | 10^(m-1)':<20} {"R'":<10}")
for row in state_table:
    print(f"{row['Texto']:<6} {row['(R >> 1) | 10^(m-1)']:<20} {row["R'"]:<10}")

# Exibe os índices de correspondência
print("\nÍndices de correspondência encontrados:", match_indices)