import os

# Directorio donde están los archivos HTML
DIRECTORIO = "D:\TFM_Barrios\mapas_con_barrios"

for nombre_archivo in os.listdir(DIRECTORIO):
    if nombre_archivo.endswith(".html"):
        ruta = os.path.join(DIRECTORIO, nombre_archivo)

        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        # Eliminar líneas 8 a 15 (índices 7 a 15 en Python, porque empieza en 0)
        nuevas_lineas = [
            linea for i, linea in enumerate(lineas)
            if not (7 <= i <= 14)
        ]

        with open(ruta, "w", encoding="utf-8") as f:
            f.writelines(nuevas_lineas)

        print(f"✔ Líneas 8–15 eliminadas en: {nombre_archivo}")
