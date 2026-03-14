# 📊 Análisis y Gestión de Datos Estudiantiles (CLI)

Herramienta de interfaz de línea de comandos (CLI) desarrollada en Python para el procesamiento, análisis estadístico descriptivo y exportación de registros académicos.

---

## 📝 Descripción del Proyecto
El sistema automatiza un flujo de trabajo (pipeline) de datos: desde la ingesta de un archivo plano CSV hasta la generación de un reporte estructurado en JSON. Aplica filtros condicionales y calcula métricas (como promedios y detección de extremos) sobre la población estudiantil.

## 📁 Estructura del Repositorio

```text
datamanager-cli/
├── data/
│   └── estudiantes.csv         # Dataset de entrada
├── docs/
│   └── evidencia_ejecucion.txt # Registro del flujo en consola
├── tests/
│   └── test_processor.py       # Pruebas unitarias matemáticas
├── data_loader.py              # Módulo de ingesta de datos
├── exporter.py                 # Módulo de serialización (UTF-8)
├── main.py                     # Orquestador principal
├── processor.py                # Lógica estadística y filtros
├── utils.py                    # Funciones auxiliares
└── README.md
```

## ✅ Requisitos Técnicos

* **Sistema Operativo:** macOS / Linux / Windows
* **Entorno:** Python 3.13.1 (recomendado)
* **Dependencias:** `pytest` (exclusivamente para correr el entorno de pruebas)

## ⚙️ Instrucciones de Ejecución

**1. Preparación del entorno:**
```bash
pip install pytest
```

**2. Verificación de exactitud matemática (Testing):**
```bash
python -m pytest tests/test_processor.py
```

**3. Inicialización del sistema:**
```bash
python main.py
```

## 💻 Flujo de Operación Estándar
Una vez dentro de la consola interactiva, ejecute la siguiente secuencia para evaluar el ciclo completo de los datos:

1. **Opción 1:** Cargar datos en la memoria temporal.
2. **Opción 4:** Ejecutar el motor de cálculo de estadísticas.
3. **Opción 5:** Volcar los resultados en el archivo `resultados.json`.
4. **Opción 6:** Terminar la ejecución.

---
**Autor:** Jhordy Roly Peña Matos
