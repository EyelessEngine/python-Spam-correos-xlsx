import pandas as pd
import os

def verificar_excel():
    """Verificar la estructura del archivo Excel"""
    
    archivo_excel = 'Data/Base de datos.xlsx'
    
    try:
        # Leer el archivo Excel
        df = pd.read_excel(archivo_excel)
        
        print("=" * 50)
        print("INFORMACIÓN DEL ARCHIVO EXCEL")
        print("=" * 50)
        print(f"Archivo: {archivo_excel}")
        print(f"Total de filas: {len(df)}")
        print(f"Columnas disponibles: {list(df.columns)}")
        
        print("\n" + "-" * 50)
        print("PRIMERAS 5 FILAS DEL ARCHIVO:")
        print("-" * 50)
        print(df.head())
        
        print("\n" + "-" * 50)
        print("VERIFICACIÓN DE COLUMNAS:")
        print("-" * 50)
        
        # Verificar si existe la columna 'Correo'
        if 'Correo' in df.columns:
            print("✅ Columna 'Correo' encontrada")
            emails_validos = df['Correo'].notna().sum()
            print(f"   - Emails válidos: {emails_validos}")
        else:
            print("❌ Columna 'Correo' NO encontrada")
            print("   - Columnas disponibles:", list(df.columns))
        
        # Verificar si existe la columna 'Nombre'
        if 'Nombre' in df.columns:
            print("✅ Columna 'Nombre' encontrada")
            nombres_validos = df['Nombre'].notna().sum()
            print(f"   - Nombres válidos: {nombres_validos}")
        else:
            print("⚠️  Columna 'Nombre' NO encontrada - se usará 'Cliente' por defecto")
        
        print("\n" + "=" * 50)
        print("¿QUIERES PROCEDER CON EL ENVÍO?")
        print("=" * 50)
        
        respuesta = input("¿Continuar con el envío de correos? (s/n): ")
        
        if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
            return True
        else:
            print("Envío cancelado.")
            return False
            
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {archivo_excel}")
        return False
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return False

if __name__ == "__main__":
    verificar_excel() 