from processor import calcular_estadisticas

def test_calcular_estadisticas_normal():
    datos = [
        {'nombre': 'Ana', 'carrera': 'Ingeniería', 'edad': '21', 'promedio': '8.5'},
        {'nombre': 'Carla', 'carrera': 'Física', 'edad': '20', 'promedio': '9.1'}
    ]
    resultado = calcular_estadisticas(datos)
    assert resultado['promedio_general'] == 8.8
    assert resultado['edad_maxima'] == 21

def test_calcular_estadisticas_vacia():
    assert calcular_estadisticas([]) == {}