import pandas as pd
import os

def crear_excel_ejemplo():
    """Crear un archivo Excel de ejemplo con la estructura correcta"""
    
    # Crear datos de ejemplo
    datos = {
        'email': [
            'cliente1@ejemplo.com',
            'cliente2@ejemplo.com', 
            'cliente3@ejemplo.com',
            'cliente4@ejemplo.com',
            'cliente5@ejemplo.com'
        ],
        'nombre': [
            'Juan Pérez',
            'María García',
            'Carlos López',
            'Ana Rodríguez',
            'Luis Martínez'
        ]
    }
    
    # Crear DataFrame
    df = pd.DataFrame(datos)
    
    # Asegurar que la carpeta Data existe
    os.makedirs('Data', exist_ok=True)
    
    # Guardar el archivo Excel
    archivo_excel = 'Data/Base de datos - Ejemplo.xlsx'
    df.to_excel(archivo_excel, index=False)
    
    print("=" * 50)
    print("ARCHIVO EXCEL CREADO")
    print("=" * 50)
    print(f"Archivo: {archivo_excel}")
    print(f"Total de filas: {len(df)}")
    print(f"Columnas: {list(df.columns)}")
    
    print("\n" + "-" * 50)
    print("DATOS DEL ARCHIVO:")
    print("-" * 50)
    print(df)
    
    print("\n" + "=" * 50)
    print("INSTRUCCIONES:")
    print("=" * 50)
    print("1. Abre el archivo 'Data/Base de datos.xlsx'")
    print("2. Reemplaza los datos de ejemplo con tus datos reales")
    print("3. Guarda el archivo")
    print("4. Ejecuta: python Main.py")
    
    return True

if __name__ == "__main__":
    crear_excel_ejemplo() 