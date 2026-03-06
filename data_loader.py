import csv
from utils import validar_datos

def cargar_csv(ruta_archivo):
    estudiantes = []
    try:
        # Leer archivo usando 'with open' [cite: 40]
        with open(ruta_archivo, mode='r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    nombre = fila['nombre']
                    carrera = fila['carrera']
                    # Convertir edad a int y promedio a float [cite: 41]
                    edad = int(fila['edad'])
                    promedio = float(fila['promedio'])
                    
                    validar_datos(nombre, edad, promedio)
                    estudiantes.append(fila)
                    
                except ValueError as e: # Uso de try/except [cite: 48]
                    print(f"Error en los datos de {fila.get('nombre', 'Desconocido')}: {e}")
                    
    except FileNotFoundError: # Manejar FileNotFoundError [cite: 42]
        print(f"Error: No se encontro el archivo en la ruta '{ruta_archivo}'.")
        
    return estudiantes # Retornar lista de diccionarios [cite: 43]