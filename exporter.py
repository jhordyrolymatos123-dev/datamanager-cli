import json # Uso del módulo json [cite: 69]

def guardar_json(datos, ruta_archivo):
    try:
        # Escritura segura con 'with' [cite: 70]
        with open(ruta_archivo, mode='w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)
        print(f"Resultados guardados exitosamente en {ruta_archivo}")
    except Exception as e:
        print(f"Ocurrio un error al guardar: {e}")