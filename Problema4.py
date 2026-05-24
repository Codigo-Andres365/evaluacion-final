def contar_titulos_populares_recientes(matriz_videoteca, umbral_calificacion, anio_limite):
    """
    Función encargada de contar cuántos títulos cumplen con ser populares
    (calificación >= umbral) y recientes (año >= anio_limite).
    """
    contador = 0
    
    # Recorremos la matriz fila por fila
    for pelicula in matriz_videoteca:
        # Estructura: [Título, Año de Lanzamiento, Calificación, Género]
        # El año está en el índice 1, la calificación en el índice 2
        anio = pelicula[1]
        calificacion = pelicula[2]
        
        # Lógica de Negocio: Calificación >= Y  Y  Año >= Año límite
        if calificacion >= umbral_calificacion and anio >= anio_limite:
            contador += 1
            
    return contador


def main():
    print("=== SISTEMA DE GESTIÓN - VIDEOTECA DIGITAL ===")
    
    # Requisito: Matriz con al menos 7 títulos
    videoteca = [
        ["Inception", 2010, 8.8, "Ciencia Ficción"],
        ["Interstellar", 2014, 8.6, "Ciencia Ficción"],
        ["Spider-Man: No Way Home", 2021, 8.2, "Acción"],
        ["Everything Everywhere All at Once", 2022, 7.9, "Aventura"],
        ["Dune: Part Two", 2024, 8.9, "Ciencia Ficción"],
        ["The Dark Knight", 2008, 9.0, "Acción"],
        ["Avatar: The Way of Water", 2022, 7.6, "Ciencia Ficción"],
        ["Oppenheimer", 2023, 8.4, "Drama"]
    ]
    
    # Captura de datos / Entrada del usuario con validación básica
    try:
        print("\n--- Criterios de Búsqueda ---")
        umbral_Y = float(input("Ingrese el umbral de calificación mínima (1-10): "))
        anio_limite = int(input("Ingrese el año de lanzamiento límite (ej. 2020): "))
        
        # Llamado al módulo/función requerido
        total_coincidencias = contar_titulos_populares_recientes(videoteca, umbral_Y, anio_limite)
        
        # Salida del requerimiento
        print("\n--- Resultados ---")
        print(f"Total de títulos con calificación >= {umbral_Y} y lanzados desde el año {anio_limite}:")
        print(f"-> {total_coincidencias} título(s) encontrado(s).")
        
    except ValueError:
        print("\n[Error]: Por favor ingrese datos numéricos válidos para el año y la calificación.")

# Punto de entrada del script
if __name__ == "__main__":
    main()