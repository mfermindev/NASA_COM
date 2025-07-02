import heapq
from collections import defaultdict

def huffman_compresion(mensaje):
    """Comprime un mensaje texto plano usando codificación Huffman
    @parameter: mensaje(type: str): Mensaje de texto a comprimir
    @return: type: tuple: (mensaje_comprimido, arbol_huffman)
        mensaje_comprimido: (type: str) Cadena binaria
        arbol_huffman: (type: dict) Diccionario de códigos
    """
    if not mensaje:
        return "", {}
    
    # Paso 1: Calcular frecuencias
    frecuencias = defaultdict(int)
    for caracter in mensaje:
        frecuencias[caracter] += 1

    # Paso 2: Construir arbol Huffman
    heap = [[freq, [char, ""]] for char, freq in frecuencias.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        
        for par in izq[1:]:
            par[1] = '0' + par[1]
        for par in der[1:]:
            par[1] = '1' + par[1]
            
        heapq.heappush(heap, [izq[0] + der[0]] + izq[1:] + der[1:])
    
    # Paso 3: asignar codigo binario
    arbol_huffman = {char: code for char, code in heap[0][1:]}
    
    # Paso 4: Codificar mensaje segun orden
    mensaje_comprimido = ''.join([arbol_huffman[char] for char in mensaje])
    
    return mensaje_comprimido, arbol_huffman

def huffman_descompresion(mensaje_comprimido, arbol_huffman):
    """Descomprime un mensaje codificado con Huffman
    @parameter: mensaje_comprimido(str): Binario comprimido
    @parameter: arbol_huffman(dict): Diccionario de codigos
    @return: str: Mensaje original descomprimido
    """
    if not mensaje_comprimido or not arbol_huffman:
        return ""
    

    codigos_invertidos = {v: k for k, v in arbol_huffman.items()}
    
    mensaje_decodificado = []
    codigo_actual = ""
    
    for bit in mensaje_comprimido:
        codigo_actual += bit
        if codigo_actual in codigos_invertidos:
            mensaje_decodificado.append(codigos_invertidos[codigo_actual])
            codigo_actual = ""
    
    return ''.join(mensaje_decodificado)
