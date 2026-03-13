Proyecto DataManager CLI

Este es el código fuente para el sistema de análisis y gestión de datos estudiantiles, desarrollado en Python. 

Descripción general del proyecto
El programa funciona desde la consola y sirve para procesar una base de datos académica. El flujo principal toma un archivo CSV inicial, permite aplicar filtros por promedio y calcula estadísticas básicas, como la media aritmética de las calificaciones y la detección de valores extremos (edades). Al finalizar el procesamiento, los resultados se exportan a un archivo JSON, configurado para mantener las tildes y caracteres especiales con codificación UTF-8.

Lógica de procesamiento y estructura
Decidí separar el código en distintos módulos para que la lógica estadística y la carga de datos no estén mezcladas en un solo archivo:

- El módulo data_loader.py se encarga exclusivamente de la ingesta de datos y de manejar los errores si el archivo CSV no se encuentra.
- El módulo processor.py contiene la lógica de cálculo. Aquí es donde el programa calcula el promedio general aplicando un redondeo a un decimal para normalizar los datos, y donde se extraen los máximos y mínimos iterando sobre los registros.
- El módulo exporter.py toma esa información ya procesada y la serializa en el archivo resultados.json.
- Finalmente, agregué un archivo test_processor.py con pruebas unitarias. Esto lo hice para comprobar automáticamente que las matemáticas de los promedios y las edades no tengan errores antes de exportar nada.

Instrucciones para probar el código
Para ejecutar y evaluar el programa, solo se necesita tener Python instalado. La única dependencia extra es pytest para correr las pruebas.

Pasos para la ejecución:
1. Para instalar la herramienta de pruebas, escribir en la consola: pip install pytest
2. Para comprobar que los cálculos estadísticos son correctos: python -m pytest tests/test_processor.py
3. Para iniciar el programa principal: python main.py

Una vez en el menú del programa, el flujo secuencial recomendado para evaluarlo es:
Elegir la opción 1 para cargar los datos en memoria.
Elegir la opción 4 para ejecutar los cálculos estadísticos.
Elegir la opción 5 para exportar el archivo JSON final.
Elegir la opción 6 para salir.

Autor: Jhordy Roly Peña Matos
Elegir la opción 5 para exportar el archivo JSON final.
Elegir la opción 6 para salir.

Autor: Jhordy Roly Peña Matos
