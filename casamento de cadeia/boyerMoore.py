# Heuristica da Ocorrencia
def bad_character_heuristic(pattern):
    bad_char = {}
    for i in range(len(pattern) - 1):
        bad_char[pattern[i]] = i
    return bad_char

# Heuristica da Casamento
def good_suffix_heuristic(pattern):
    m = len(pattern)
    suffix = [-1] * m
    border = [0] * m
    
    j = m
    for i in range(m - 1, -1, -1):
        if i == m - 1 or (j < m and pattern[i] != pattern[j]):
            j = i + 1
        border[i] = j
    
    j = border[0]
    for i in range(m):
        if suffix[i] == -1:
            suffix[i] = j
        if i == j:
            j = border[j]
    
    return suffix

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0:
        return []
    
    bad_char = bad_character_heuristic(pattern)
    good_suffix = good_suffix_heuristic(pattern)
    
    matches = []
    shift = 0
    iteration = 1
    
    while shift <= n - m:
        print(f"Iteração {iteration}: Padrão alinhado na posição {shift}")
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            print(f"  Casamento no índice {shift + j} ({pattern[j]})")
            j -= 1
        
        if j < 0:
            print(f"  Padrão encontrado na posição {shift}")
            matches.append(shift)
            shift += good_suffix[0] if good_suffix[0] > 1 else 1
        else:
            bad_char_shift = j - bad_char.get(text[shift + j], -1)
            good_suffix_shift = good_suffix[j]
            shift += max(bad_char_shift, good_suffix_shift)
            print(f"  Deslocamento: heurística ocorrência = {bad_char_shift}, heurística casamento = {good_suffix_shift}, deslocando para {shift}")
        iteration += 1
    
    return matches

# Exemplo de uso
text = "aabcaccacbac"
pattern = "cacbac"
result = boyer_moore(text, pattern)
print("Padrão encontrado nas posições:", result)