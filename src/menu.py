from huffman import (
    huffman_compresion,
    huffman_descompresion
)

from funciones import (
    binario_a_hex,
    hex_a_binario,
    calcular_checksum
)
from collections import defaultdict

def mostrar_menu():
    print("\n" + "*" * 30)
    print("* MENÚ PRINCIPAL *".center(30))
    print("*" * 30)
    print("1. Codificar mensaje y enviar")
    print("2. Decodificar mensaje recibido")
    print("3. Calcular checksum")
    print("4. Mostrar estadísticas")
    print("5. Salir")
    print(" ")
    return input("Seleccione una opción: ")

def mostrar_frecuencias(mensaje):
    frecuencias = defaultdict(int)
    for char in mensaje:
        frecuencias[char] += 1
    print("\nFrecuencias de caracteres:")
    for char, freq in sorted(frecuencias.items()):
        print(f"'{char}': {freq}")

def main():
    historial = []
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":  
            mensaje = input("\nIngrese el mensaje a codificar: ")
            if not mensaje:
                print("⚠️ Error: Mensaje vacío")
                continue
                
            comprimido, arbol = huffman_compresion(mensaje)
            hex_enviado = binario_a_hex(comprimido)
            checksum = calcular_checksum(mensaje)
            
            historial.append({
                'tipo': 'envio',
                'original': mensaje,
                'comprimido': comprimido,
                'hex': hex_enviado,
                'arbol': arbol,
                'checksum': checksum
            })
            
            print("\n✅ Mensaje codificado:")
            print(f"Original: {mensaje}")
            print(f"Comprimido (bin): {comprimido}")
            print(f"Hex enviado: {hex_enviado}")
            print(f"Checksum: 0x{checksum}")
            print(f"Árbol Huffman: {arbol}")
        
        elif opcion == "2": 
            hex_recibido = input("\nIngrese el mensaje hex recibido (con 0x): ").strip()
            longitud = int(input("Longitud original del binario: "))
            
            try:
                binario = hex_a_binario(hex_recibido, longitud)
                arbol_str = input("Ingrese el árbol Huffman (ej: {'A':'0', 'B':'1'}): ")
                arbol = eval(arbol_str)  
                
                mensaje = huffman_descompresion(binario, arbol)
                checksum = calcular_checksum(mensaje)
                
                historial.append({
                    'tipo': 'recepcion',
                    'hex': hex_recibido,
                    'decodificado': mensaje,
                    'checksum': checksum
                })
                
                print("\n✅ Mensaje decodificado:")
                print(f"Hex recibido: {hex_recibido}")
                print(f"Binario: {binario}")
                print(f"Mensaje: {mensaje}")
                print(f"Checksum: 0x{checksum}")
                
            except Exception as e:
                print(f"⚠️ Error al decodificar: {e}")
        
        elif opcion == "3":  
            mensaje = input("\nIngrese el mensaje para checksum: ")
            print(f"Checksum: 0x{calcular_checksum(mensaje)}")
        
        elif opcion == "4":  
            if not historial:
                print("\n⚠️ No hay datos en el historial")
                continue
                
            print("\n📊 Estadísticas:")
            for i, item in enumerate(historial, 1):
                if item['tipo'] == 'envio':
                    print(f"\nEnvío {i}:")
                    print(f"Original: {item['original']}")
                    mostrar_frecuencias(item['original'])
                    print(f"Tasa compresión: {len(item['comprimido'])/len(item['original'])*8:.1f} bits/carácter")
        
        elif opcion == "5":
            print("\n EXIT")
            break
            
        else:
            print("\n⚠️ Opción no válida")

if __name__ == "__main__":
    main()