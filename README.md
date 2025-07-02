#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### \# 🚀 Compresor NASA - TP Final

#### 

#### \*\*Materia\*\*: Introducción a la Ingeniería en Computación  

#### \*\*Universidad\*\*: UNRN

#### \*\*Docente\*\*: docente

#### \*\*Autores\*\*: alumno

#### 

#### <div align="center">

#### &nbsp; <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDRtbTEyamp1ZnV4dmg5ZnNqM2c1YWNrM21ubmNlYXBmajNrdzFmeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J9RFoDzCDrkqtEc/giphy.gif" width="300" alt="Huffman Compression Demo">


#### </div>

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### \## 📌 Descripción

#### 

#### Implementación completa del algoritmo de compresión Huffman desarrollado como trabajo práctico final para la materia de Introducción a la Ingeniería en Computación. 

#### 

#### El proyecto demuestra:

#### 

#### \- 🔍 Compresión/descompresión de mensajes

#### \- 🔄 Conversión binario-hexadecimal

#### \- ✅ Verificación de integridad con checksum

#### \- 📊 Análisis estadístico de compresión

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### \## 🛠️ Tecnologías Utilizadas

#### 

#### ```python

#### tech\_stack = {

#### &nbsp;   "Lenguaje": "Python 3.10",

#### &nbsp;   "Librerías": \["heapq", "collections"],

#### &nbsp;   "Estructuras": \["Árbol binario", "Diccionarios"],

#### &nbsp;   "Algoritmos": \["Huffman", "Checksum", convBin2Hex, convHex2Bin]

#### }

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### Estructura del proyecto

#### NASA\_COM/

#### ├── src/

#### │   ├── huffman.py        # algoritmo provisto

#### │   ├── menu.py           # Interfaz de usuario

#### │   └── funciones.py      # Funciones auxiliares

#### ├── tests/                # Casos de prueba

#### ├── docs/                 # Documentación

#### └── README.md             # Este archivo

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### 

#### \* MENÚ PRINCIPAL \*

#### 1\. Codificar mensaje

#### 2\. Decodificar mensaje

#### 3\. Calcular checksum

#### 4\. Mostrar estadísticas

#### 5\. Salir

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### 

#### Caso de uso::

#### > Ingrese mensaje: "INGENIERIA"

#### 

#### \[RESULTADO]

#### Binario: 1001111100011000110101110

#### Hex: 0x13E31AE

#### Árbol Huffman: {'I': '10', 'N': '01', 'E': '00', ...}

#### Checksum: 0x79

#### Tasa compresión: 68.75%

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### 

#### ⚙️ Instalación

#### >>bash

#### \# Clonar repositorio

#### git clone https://github.com/mfermindev/NASA\_COM

#### cd NASA\_COM

#### 

#### \# Ejecutar (no requiere dependencias externas)

#### python src/menu.py





#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



#### 🖥️ Uso del Programa

#### El sistema ofrece un menú interactivo:

#### 

#### plaintext

#### \* MENÚ PRINCIPAL \*

#### 1\. Codificar mensaje

#### 2\. Decodificar mensaje

#### 3\. Calcular checksum

#### 4\. Mostrar estadísticas

#### 5\. Salir

#### Ejemplo completo:

#### plaintext





#### > Ingrese mensaje: "INGENIERIA"

#### 

#### \[RESULTADO]

#### Binario: 1001111100011000110101110

#### Hex: 0x13E31AE

#### Árbol Huffman: {'I': '10', 'N': '01', 'E': '00', ...}

#### Checksum: 0x79

#### Tasa compresión: 68.75%

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### 📊 Métricas de Compresión

#### Mensaje	Original (bits)	Comprimido (bits)	Reducción

#### "CASA"	32	6	81.25%

#### "Hola"	32	8	75.00%

#### "BANANA"	48	9	81.25%

#### "INGENIERIA"	80	25	68.75%

#### 

#### %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#### 🎓 Aprendizajes Clave

#### Implementación de algoritmos teóricos

#### 

#### Manejo de estructuras de datos complejas

#### 

#### Procesamiento de cadenas binarias

#### 

#### Validación de integridad de datos

#### 

#### Optimización de recursos

