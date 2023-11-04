#!/bin/bash
ffmpeg -i video.mp4 -r 2 -s 160x120 -f image2 Fotogramas/ext_mem%01d.png
# Carpeta de origen y destino
python3 Pixeles.py

python3 coloresRGB_PantallaCompleta.py

rm -r Fotogramas/*
rm -r Fotogramas_txt/*
rm -r Archivos_de_memoria/*



