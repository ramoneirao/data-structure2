def sunday_bad_character_heuristic(pattern):
    m = len(pattern)
    bad_char = {char: m + 1 for char in set(pattern)}
    for i in range(m):
        bad_char[pattern[i]] = m - i
    
    print("Tabela de deslocamento (Sunday):")
    for char, shift in sorted(bad_char.items()):
        print(f"  '{char}': {shift}")
    
    return bad_char

def boyer_moore_horspool_sunday(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n < m:
        return []
    
    bad_char = sunday_bad_character_heuristic(pattern)
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
            shift += bad_char.get(text[shift + m], m + 1) if shift + m < n else m + 1
        else:
            next_char_index = shift + m
            next_char = text[next_char_index] if next_char_index < n else None
            shift += bad_char.get(next_char, m + 1)
            print(f"  Deslocamento pela heurística de ocorrência (Sunday): novo deslocamento para {shift}")
        iteration += 1
    
    return matches

# Exemplo de uso
text = "hbadecaedcade"
pattern = "cade"
result = boyer_moore_horspool_sunday(text, pattern)
print("Padrão encontrado nas posições:", result)