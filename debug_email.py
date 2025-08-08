import smtplib
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv('config.env')

# Configuración SMTP desde variables de entorno
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = int(os.getenv('SMTP_PORT'))
sender_email = os.getenv('EMAIL_USER')
password = os.getenv('EMAIL_PASSWORD')

print("=== DIAGNÓSTICO DE CONFIGURACIÓN ===")
print(f"Servidor SMTP: {smtp_server}")
print(f"Puerto: {smtp_port}")
print(f"Email: {sender_email}")
print(f"Contraseña (primeros 3 caracteres): {password[:3] if password else 'No encontrada'}")
print(f"Longitud de contraseña: {len(password) if password else 0}")

# Verificar codificación
try:
    print(f"Contraseña en ASCII: {password.encode('ascii', errors='ignore')}")
    print("✅ La contraseña es compatible con ASCII")
except Exception as e:
    print(f"❌ Problema con codificación: {e}")

print("\n=== PRUEBA DE CONEXIÓN ===")

try:
    print(f"Conectando a {smtp_server}:{smtp_port}")
    server = smtplib.SMTP(smtp_server, smtp_port)
    print("✅ Conexión SMTP establecida")
    
    print("Iniciando TLS...")
    server.starttls()
    print("✅ TLS iniciado")
    
    print("Iniciando sesión...")
    server.login(sender_email, password)
    print("✅ Login exitoso!")
    
    server.quit()
    print("✅ Conexión cerrada correctamente")
    
except smtplib.SMTPAuthenticationError as e:
    print(f"❌ Error de autenticación: {e}")
    print("Verifica tu email y contraseña")
except Exception as e:
    print(f"❌ Error: {e}")
    print(f"Tipo de error: {type(e).__name__}") 