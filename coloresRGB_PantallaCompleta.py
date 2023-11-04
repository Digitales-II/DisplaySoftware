import math
import os

def procesar_archivo(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entrada, open(archivo_salida, 'w') as salida:
        lineas_entrada = entrada.readlines()
        total_lineas = len(lineas_entrada)
    
        for num_linea in range(3200):
            num1 = obtener_numeros(lineas_entrada[num_linea])
            num2 = obtener_numeros(lineas_entrada[num_linea+3200])
            num3 = obtener_numeros(lineas_entrada[num_linea+6400])
            num4 = obtener_numeros(lineas_entrada[num_linea+9600])
            num5 = obtener_numeros(lineas_entrada[num_linea+12800])
            num6 = obtener_numeros(lineas_entrada[num_linea+16000])
            for i in range(3):
                bin1 = binarizar(num1[i])
                bin1 = bin1.zfill(3)
                salida.write(bin1)
            for i in range(3):
                bin2 = binarizar(num2[i])
                bin2 = bin2.zfill(3)
                salida.write(bin2) 
            for i in range(3):
                bin3 = binarizar(num3[i])
                bin3 = bin3.zfill(3)
                salida.write(bin3) 
            for i in range(3):
                bin4 = binarizar(num4[i])
                bin4 = bin4.zfill(3)
                salida.write(bin4)  
            for i in range(3):
                bin5 = binarizar(num5[i])
                bin5 = bin5.zfill(3)
                salida.write(bin5) 
            for i in range(3):
                bin6 = binarizar(num6[i])
                bin6 = bin6.zfill(3)
                salida.write(bin6) 
            #salida.write('\n')
    


def obtener_numeros(linea):
    inicio = linea.index('(') + 1
    fin = linea.index(')')
    numeros_str = linea[inicio:fin].split(',')
    numeros = [int(int(numero)/34) for numero in numeros_str]
    return numeros

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
    
Lista_Foto_txt = os.listdir("Fotogramas_txt")

archivos_entrada = []

archivos_salida = []

# Recorre la lista de archivos y crea las rutas completas
for foto in Lista_Foto_txt:
    ruta_completa = os.path.join("Fotogramas_txt", foto)
    archivos_entrada.append(ruta_completa)
#print(archivos_entrada)

a = 1

for archivo in archivos_entrada:
    ruta_completa = os.path.join("Archivos_de_memoria", "salida" + str(a) + ".bin")
    archivos_salida.append(ruta_completa)
    a += 1  # Usar a += 1 en lugar de a++ en Python

# Imprimir la lista de nombres diferentes
#print(archivos_salida)
for entrada, salida in zip(archivos_entrada, archivos_salida):
    procesar_archivo(entrada, salida)

archivo_salida2 = "Archivo_ethernet/completo.bin"
with open(archivo_salida2, "w") as new_file:
    for name in archivos_salida:
        with open(name) as f:
            for line in f:
                # Verificar si la línea no está vacía antes de escribirla
                if line.strip():  # Esto elimina espacios en blanco y caracteres de nueva línea.
                    new_file.write(line)

            #new_file.write("\n")
            
"""

# Lista para almacenar las líneas no vacías
lineas_no_vacias = []

# Abrir el archivo de salida y leer las líneas no vacías
with open(archivo_salida2, "r") as archivo:
    for linea in archivo:
        if linea.strip():  # Verificar si la línea no está vacía después de eliminar espacios en blanco
            lineas_no_vacias.append(linea)

# Reescribir el archivo de salida con las líneas no vacías
with open(archivo_salida2, "w") as archivo:
    archivo.writelines(lineas_no_vacias)"""

