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

def test_conexion_smtp():
    try:
        print(f"Conectando a {smtp_server}:{smtp_port}")
        print(f"Email: {sender_email}")
        
        # Crear conexión SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        print("Iniciando sesión...")
        
        # Solución específica para caracteres especiales
        try:
            # Método 1: Codificar como bytes y luego decodificar
            password_bytes = password.encode('utf-8')
            password_fixed = password_bytes.decode('latin-1')
            server.login(sender_email, password_fixed)
            print("✅ Conexión exitosa con codificación UTF-8!")
        except Exception as e1:
            print(f"❌ Método 1 falló: {e1}")
            try:
                # Método 2: Reemplazar caracteres problemáticos
                password_clean = password.replace('ñ', 'n').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
                server.login(sender_email, password_clean)
                print("✅ Conexión exitosa con caracteres reemplazados!")
            except Exception as e2:
                print(f"❌ Método 2 falló: {e2}")
                try:
                    # Método 3: Usar la contraseña tal como está
                    server.login(sender_email, password)
                    print("✅ Conexión exitosa directa!")
                except Exception as e3:
                    print(f"❌ Método 3 falló: {e3}")
                    print("❌ No se pudo establecer conexión")
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