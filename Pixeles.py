import os
from PIL import Image

# Función para aproximar un valor a un múltiplo de 17 hacia abajo
def aproximar_a_multiplo_17(valor):
    return (valor // 17) * 17

# Ruta de la carpeta con las imágenes de entrada
carpeta_entrada = "Fotogramas/"

# Ruta de la carpeta de salida para los archivos de texto
carpeta_salida = "Fotogramas_txt/"

# Asegurarse de que la carpeta de salida exista, si no, créala
if not os.path.exists(carpeta_salida):
    os.makedirs(carpeta_salida)

# Lista todos los archivos en la carpeta de entrada
archivos_imagen = os.listdir(carpeta_entrada)

# Itera a través de cada imagen en la carpeta de entrada
for archivo in archivos_imagen:
    if archivo.endswith(".jpg") or archivo.endswith(".png"):
        # Abre la imagen
        imagen = Image.open(os.path.join(carpeta_entrada, archivo))

        # Obtiene las dimensiones de la imagen
        ancho, alto = imagen.size

        # Nombre del archivo de salida
        nombre_archivo_salida = os.path.splitext(archivo)[0] + ".txt"
        ruta_archivo_salida = os.path.join(carpeta_salida, nombre_archivo_salida)

        # Abre el archivo de salida para escribir
        with open(ruta_archivo_salida, "w") as archivo_salida:
            # Itera a través de cada píxel y obtiene su color RGB en el formato deseado
            for y in range(alto):
                for x in range(ancho):
                    pixel = imagen.getpixel((x, y))
                    r, g, b = pixel
                    
                    # Aproxima los valores R, G y B al múltiplo de 17 más cercano hacia abajo
                    r = aproximar_a_multiplo_17(r)
                    g = aproximar_a_multiplo_17(g)
                    b = aproximar_a_multiplo_17(b)
                    
                    # Escribe la línea en el archivo
                    linea = f"{x},{y} = rgb({r},{g},{b})\n"
                    archivo_salida.write(linea)

        # Cierra la imagen
        imagen.close()

