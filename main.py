from data_loader import cargar_csv
from processor import filtrar_por_promedio, ordenar_datos, calcular_estadisticas
from exporter import guardar_json

def mostrar_menu():
    print("\n--- DataManager CLI ---")
    print("1 - Cargar datos") # [cite: 73]
    print("2 - Filtrar") # [cite: 74]
    print("3 - Ordenar") # [cite: 75]
    print("4 - Mostrar estadísticas") # [cite: 76]
    print("5 - Exportar resultados") # [cite: 77]
    print("6 - Salir") # [cite: 78]

def main():
    estudiantes = []
    estadisticas_actuales = {}
    
    # Uso de bucle while principal [cite: 81]
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            estudiantes = cargar_csv('data/estudiantes.csv')
            print(f"Se cargaron {len(estudiantes)} estudiantes.")
            
        elif opcion == '2':
            if not estudiantes:
                print("Primero debes cargar los datos.")
                continue
            try:
                minimo = float(input("Ingresa el promedio minimo: "))
                filtrados = filtrar_por_promedio(estudiantes, minimo)
                for e in filtrados:
                    print(f"{e['nombre']} - Promedio: {e['promedio']}")
            except ValueError:
                # No finalizar abruptamente ante errores [cite: 80]
                print("Por favor, ingresa un numero valido.") 
                
        elif opcion == '3':
            if not estudiantes:
                print("Primero debes cargar los datos.")
                continue
            criterio = input("Ordenar por (nombre, promedio, edad): ").lower()
            if criterio in ['nombre', 'promedio', 'edad']:
                ordenados = ordenar_datos(estudiantes, criterio)
                for e in ordenados:
                    print(f"{e['nombre']} - {criterio}: {e[criterio]}")
            else:
                print("Criterio no valido.")
                
        elif opcion == '4':
            if not estudiantes:
                print("Primero debes cargar los datos.")
                continue
            estadisticas_actuales = calcular_estadisticas(estudiantes)
            print("\nEstadisticas:")
            for clave, valor in estadisticas_actuales.items():
                print(f"{clave}: {valor}")
                
        elif opcion == '5':
            if not estadisticas_actuales:
                print("Primero calcula las estadisticas (Opcion 4).")
                continue
            guardar_json(estadisticas_actuales, 'resultados.json')
            
        elif opcion == '6':
            print("Saliendo del programa...")
            break
            
        else:
            # Validar entradas del usuario [cite: 79]
            print("Opcion invalida. Intenta de nuevo.") 

if __name__ == "__main__":
    main()