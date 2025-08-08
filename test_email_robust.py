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

def login_with_encoding_handling(server, email, password):
    """Intenta hacer login con diferentes codificaciones"""
    encodings_to_try = [
        None,  # Sin codificación
        'utf-8',
        'latin-1',
        'cp1252',
        'iso-8859-1'
    ]
    
    for encoding in encodings_to_try:
        try:
            if encoding:
                password_encoded = password.encode(encoding).decode('latin-1')
                server.login(email, password_encoded)
            else:
                server.login(email, password)
            print(f"✅ Login exitoso con codificación: {encoding or 'default'}")
            return True
        except UnicodeEncodeError:
            print(f"❌ Falló con codificación: {encoding or 'default'}")
            continue
        except smtplib.SMTPAuthenticationError:
            print(f"❌ Error de autenticación con codificación: {encoding or 'default'}")
            continue
        except Exception as e:
            print(f"❌ Error con codificación {encoding or 'default'}: {e}")
            continue
    
    return False

def safe_login(server, email, password):
    """Método alternativo para login que maneja caracteres especiales"""
    try:
        # Intentar con codificación UTF-8
        password_bytes = password.encode('utf-8')
        server.login(email, password_bytes.decode('latin-1'))
        print("✅ Login exitoso con codificación UTF-8")
        return True
    except Exception as e:
        print(f"❌ Error en login seguro: {e}")
        return False

def test_conexion_smtp():
    try:
        print(f"Conectando a {smtp_server}:{smtp_port}")
        print(f"Email: {sender_email}")
        
        # Crear conexión SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        print("Iniciando sesión...")
        # Intentar primero con el método seguro
        if not safe_login(server, sender_email, password):
            # Si falla, intentar con diferentes codificaciones
            if not login_with_encoding_handling(server, sender_email, password):
                print("❌ No se pudo hacer login con ninguna codificación")
                return False
        
        # Enviar correo de prueba
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email  # Enviar a ti mismo como prueba
        msg['Subject'] = "Prueba de configuración SMTP"
        
        body = "Este es un correo de prueba para verificar que la configuración SMTP funciona correctamente."
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        server.send_message(msg)
        print("✅ Correo de prueba enviado exitosamente!")
        
        server.quit()
        return True
        
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

if __name__ == "__main__":
    test_conexion_smtp() 