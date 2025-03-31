from collections import Counter, defaultdict
import heapq

class HuffmanNode:
    def __init__(self, freq, symbol=None, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(word_freq):
    heap = [HuffmanNode(freq, symbol) for symbol, freq in word_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", code_map=None):
    if code_map is None:
        code_map = {}

    if node.symbol is not None:
        code_map[node.symbol] = prefix
    else:
        generate_codes(node.left, prefix + "0", code_map)
        generate_codes(node.right, prefix + "1", code_map)

    return code_map

def display_huffman_tree(node, prefix=""):
    """Exibe apenas os nós folha da árvore de Huffman."""
    if node is not None:
        if node.symbol is not None:  # Nó folha
            print(f"{prefix}[{node.symbol}]")
        else:  # Nó interno
            if node.left:
                display_huffman_tree(node.left, prefix + " 0->")
            if node.right:
                display_huffman_tree(node.right, prefix + " 1->")
                
def compress(text, code_map):
    words = text.split()
    compressed = []
    for word in words:
        if word[-1] in ",.!?;:":
            compressed.append(code_map[word[:-1]])
            compressed.append(code_map[word[-1]])
        else:
            compressed.append(code_map[word])
    return " ".join(compressed)

def decompress(compressed, code_map):
    reverse_code_map = {v: k for k, v in code_map.items()}
    current_code = ""
    decompressed = []
    for bit in compressed.split():
        current_code += bit
        if current_code in reverse_code_map:
            decompressed.append(reverse_code_map[current_code])
            current_code = ""
    return " ".join(decompressed)

def build_tree_from_fixed_codes(code_map):
    """Constrói a árvore de Huffman a partir de um mapa de códigos fixos."""
    root = HuffmanNode(freq=0)
    for symbol, code in code_map.items():
        current = root
        for bit in code:
            if bit == "0":
                if not current.left:
                    current.left = HuffmanNode(freq=0)
                current = current.left
            elif bit == "1":
                if not current.right:
                    current.right = HuffmanNode(freq=0)
                current = current.right
        current.symbol = symbol
    return root

def generate_fixed_codes():
    """Returns a fixed code map for the words."""
    return {
        "rosa": "0",
        "uma": "10",
        "para": "1100",
        "cada": "1101",
        ",": "1110",
        "é": "1111"
    }

def main():
    text = "para cada rosa rosa, uma rosa é uma rosa"

    # Use the fixed code map
    code_map = generate_fixed_codes()

    print("Huffman Codes:")
    for word, code in code_map.items():
        print(f"{word}: {code}")

    # Build the Huffman tree using the fixed codes
    huffman_tree = build_tree_from_fixed_codes(code_map)

    print("\nHuffman Tree:")
    display_huffman_tree(huffman_tree)  # Exibe a árvore no formato solicitado

    print("\nCompressed Text:")
    compressed = compress(text, code_map)
    print(compressed)

    print("\nDecompressed Text:")
    decompressed = decompress(compressed, code_map)
    print(decompressed)

if __name__ == "__main__":
    main()