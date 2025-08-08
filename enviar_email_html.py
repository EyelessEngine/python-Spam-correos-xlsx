import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv('config.env')

# Configuración SMTP desde variables de entorno
smtp_server = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
smtp_port = int(os.getenv('SMTP_PORT', 587))
sender_email = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')

def leer_plantilla_html():
    """Lee la plantilla HTML y la devuelve como string"""
    try:
        with open('email_template.html', 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error al leer la plantilla HTML: {e}")
        return None

def enviar_correos_html_desde_excel(archivo_excel):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_excel)
    
    # Leer la plantilla HTML
    plantilla_html = leer_plantilla_html()
    if not plantilla_html:
        print("❌ No se pudo leer la plantilla HTML. Abortando.")
        return
    
    try:
        # Conectar al servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        
        # Contador de correos enviados
        correos_enviados = 0
        
        # Enviar correos a cada fila
        for index, row in df.iterrows():
            # Obtener el nombre del destinatario (usando 'Nombre' de tu Excel)
            nombre = row.get('Nombre', 'Cliente')  # Usa 'Nombre' de tu archivo
            
            # Personalizar la plantilla HTML con el nombre del destinatario
            html_personalizado = plantilla_html.replace('{nombre}', nombre)
            
            # Crear mensaje
            msg = MIMEMultipart('alternative')
            msg['From'] = sender_email
            msg['To'] = row['Correo']  # Usa 'Correo' de tu archivo
            msg['Subject'] = "Servicios de Compra y Venta de Metales - Oportunidad Comercial"
            
            # Adjuntar versión HTML
            msg.attach(MIMEText(html_personalizado, 'html'))
            
            # Enviar correo
            server.send_message(msg)
            correos_enviados += 1
            print(f"✅ Correo HTML enviado a: {row['Correo']} (Nombre: {nombre})")
            
        print(f"\n=== Resumen ===\nTotal de correos enviados: {correos_enviados} de {len(df)}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

def preview_email_html():
    """Muestra una vista previa del correo HTML"""
    plantilla_html = leer_plantilla_html()
    if not plantilla_html:
        print("❌ No se pudo leer la plantilla HTML.")
        return
    
    # Personalizar con un nombre de ejemplo
    html_personalizado = plantilla_html.replace('{nombre}', 'Cliente Ejemplo')
    
    # Guardar la vista previa en un archivo temporal
    with open('preview_email.html', 'w', encoding='utf-8') as file:
        file.write(html_personalizado)
    
    print("=" * 50)
    print("VISTA PREVIA DEL CORREO HTML GENERADA")
    print("=" * 50)
    print("Se ha creado el archivo 'preview_email.html'")
    print("Abra este archivo en su navegador para ver cómo se verá el correo.")

# Usar la función
if __name__ == "__main__":
    opcion = input("¿Qué desea hacer?\n1. Enviar correos HTML\n2. Ver vista previa\nElija una opción (1/2): ")
    
    if opcion == "1":
        enviar_correos_html_desde_excel('Data/Base de datos.xlsx')
    elif opcion == "2":
        preview_email_html()
    else:
        print("Opción no válida.")