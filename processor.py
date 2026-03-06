# --- Filtrar datos ---
def filtrar_por_promedio(estudiantes, minimo):
    # Filtrar por promedio mayor a X [cite: 51]
    return [e for e in estudiantes if float(e['promedio']) > minimo]

def filtrar_por_carrera(estudiantes, carrera):
    # Filtrar por carrera [cite: 52]
    return [e for e in estudiantes if e['carrera'].lower() == carrera.lower()]

# --- Ordenar datos ---
def ordenar_datos(estudiantes, criterio):
    # Uso de sorted(..., key=...) [cite: 59]
    if criterio == 'nombre':
        return sorted(estudiantes, key=lambda x: x['nombre']) # Ordenar por nombre [cite: 56]
    elif criterio == 'promedio':
        return sorted(estudiantes, key=lambda x: float(x['promedio']), reverse=True) # Ordenar por promedio [cite: 57]
    elif criterio == 'edad':
        return sorted(estudiantes, key=lambda x: int(x['edad'])) # Ordenar por edad [cite: 58]
    return estudiantes

# --- Estadísticas ---
def calcular_estadisticas(estudiantes):
    if not estudiantes:
        return {}
        
    promedios = [float(e['promedio']) for e in estudiantes]
    edades = [int(e['edad']) for e in estudiantes]
    
    # Conteo por carrera [cite: 63]
    conteo_carreras = {}
    for e in estudiantes:
        carrera = e['carrera']
        if carrera in conteo_carreras:
            conteo_carreras[carrera] += 1
        else:
            conteo_carreras[carrera] = 1

    return {
        "promedio_general": sum(promedios) / len(promedios), # Calcular promedio general [cite: 61]
        "edad_maxima": max(edades), # Edad máxima [cite: 62]
        "edad_minima": min(edades),
        "conteo_carreras": conteo_carreras,
        "total_estudiantes": len(estudiantes)
    }