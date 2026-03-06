def validar_datos(nombre, edad, promedio):
    # Nombre no vacío [cite: 47]
    if not nombre or nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacio.")
    
    # Edad debe ser entero positivo [cite: 45]
    if edad <= 0:
        raise ValueError("La edad debe ser un numero positivo.")
        
    # Promedio entre 0 y 10 [cite: 46]
    if promedio < 0 or promedio > 10:
        raise ValueError("El promedio debe estar entre 0 y 10.")
        
    return True