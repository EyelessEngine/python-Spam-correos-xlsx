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

def test_conexion_simple():
    try:
        print(f"Conectando a {smtp_server}:{smtp_port}")
        print(f"Email: {sender_email}")
        
        # Crear conexión SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        print("✅ Conexión SMTP establecida")
        
        # Iniciar TLS
        server.starttls()
        print("✅ TLS iniciado")
        
        # Login simple
        print("Iniciando sesión...")
        server.login(sender_email, password)
        print("✅ Login exitoso!")
        
        # Enviar correo de prueba
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg['Subject'] = "Prueba de configuración SMTP"
        
        body = "Este es un correo de prueba para verificar que la configuración SMTP funciona correctamente."
        msg.attach(MIMEText(body, 'plain'))
        
        server.send_message(msg)
        print("✅ Correo de prueba enviado exitosamente!")
        
        server.quit()
        return True
        
    except smtplib.SMTPAuthenticationError as e:
        print(f"❌ Error de autenticación: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_conexion_simple() 