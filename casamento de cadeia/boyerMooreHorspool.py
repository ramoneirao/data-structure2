def horspool_bad_character_heuristic(pattern):
    m = len(pattern)
    bad_char = {char: m for char in set(pattern)}
    for i in range(m - 1):
        bad_char[pattern[i]] = m - 1 - i
    
    print("Tabela de deslocamento:")
    for char, shift in sorted(bad_char.items()):
        print(f"  '{char}': {shift}")
    
    return bad_char

def boyer_moore_horspool(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n < m:
        return []
    
    bad_char = horspool_bad_character_heuristic(pattern)
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
            shift += bad_char.get(text[shift + m - 1], m)
        else:
            shift += bad_char.get(text[shift + m - 1], m)
            print(f"  Deslocamento pela heurística de ocorrência: novo deslocamento para {shift}")
        iteration += 1
    
    return matches

# Exemplo de uso
text = "hbadecaedcade"
pattern = "cade"
result = boyer_moore_horspool(text, pattern)
print("Padrão encontrado nas posições:", result)