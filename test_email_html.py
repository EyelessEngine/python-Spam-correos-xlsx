import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Cargar variables de entorno
load_dotenv('config.env')

# Configuración SMTP desde variables de entorno
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
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

def test_email_html():
    try:
        print(f"Conectando a {smtp_server}:{smtp_port}")
        print(f"Email: {sender_email}")
        
        # Leer la plantilla HTML
        plantilla_html = leer_plantilla_html()
        if not plantilla_html:
            print("❌ No se pudo leer la plantilla HTML. Abortando.")
            return False
        
        # Personalizar con un nombre de ejemplo
        html_personalizado = plantilla_html.replace('{nombre}', 'Usuario de Prueba')
        
        # Crear conexión SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        print("Iniciando sesión...")
        # Manejar codificación de contraseña con caracteres especiales
        try:
            server.login(sender_email, password)
        except UnicodeEncodeError:
            # Si falla, intentar con codificación específica
            password_encoded = password.encode('utf-8').decode('latin-1')
            server.login(sender_email, password_encoded)
        print("✅ Conexión exitosa!")
        
        # Enviar correo de prueba
        msg = MIMEMultipart('alternative')
        msg['From'] = sender_email
        msg['To'] = sender_email  # Enviar a ti mismo como prueba
        msg['Subject'] = "Prueba de correo HTML - Metales"
        
        # Adjuntar versión HTML
        msg.attach(MIMEText(html_personalizado, 'html'))
        
        server.send_message(msg)
        print("✅ Correo HTML de prueba enviado exitosamente!")
        
        server.quit()
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Error de autenticación: {e}")
        print("Verifique su nombre de usuario y contraseña en el archivo config.env")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Ejecutar la prueba
if __name__ == "__main__":
    print("=" * 50)
    print("PRUEBA DE ENVÍO DE CORREO HTML")
    print("=" * 50)
    
    if test_email_html():
        print("\n✅ La prueba de correo HTML fue exitosa!")
        print("Revise su bandeja de entrada para verificar el correo.")
    else:
        print("\n❌ La prueba de correo HTML falló.")