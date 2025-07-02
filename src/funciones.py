def binario_a_hex(binario: str) -> str:
    """convierte un binario a hexa
    @parameter: binatio (str): numero binario de mensaje codificado
    @return: str: hexa de binario"""
    if not binario:
        return "0x0"
 
    padding = (4 - len(binario) % 4) % 4
    binario_padded = '0' * padding + binario

    hex_str = hex(int(binario_padded, 2))[2:]
    return f"0x{hex_str}"

def hex_a_binario(hex_str: str, longitud_original: int) -> str:
    """convierte un binario a hexa
    @parameter: binatio (str): numero hexa de mensaje codificado
    @parameter: longitud_original (int): longitud original del binario, para mantener el orden despues
    @return: str: binario de hexadecimal    """
    if hex_str.startswith('0x'):
        hex_str = hex_str[2:]
    binario = bin(int(hex_str, 16))[2:]

    binario = binario.zfill(longitud_original)
    return binario

def calcular_checksum(mensaje: str) -> str:
    """Calcula el checksum de un mensaje usando suma de valores ASCII y modulo 256.
    @parameter: msj (str): Mensaje original 
    @return: str: Checksum en formato hexadecimal de 2 dig
    """
    if not mensaje:
        return "00"
    
    checksum = 0
    for caracter in mensaje:
        checksum += ord(caracter) 
    
    checksum %= 256  
    
    return f"{checksum:02X}"
