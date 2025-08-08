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

def enviar_correos_desde_excel(archivo_excel):
    # Leer el archivo Excel
    df = pd.read_excel(archivo_excel)
    
    try:
        # Conectar al servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        
        # Enviar correos a cada fila
        for index, row in df.iterrows():
            # Obtener el nombre del destinatario (usando 'Nombre' de tu Excel)
            nombre = row.get('Nombre', 'Cliente')  # Usa 'Nombre' de tu archivo
            
            # Crear mensaje
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = row['Correo']  # Usa 'Correo' de tu archivo
            msg['Subject'] = "Servicios de Compra y Venta de Metales - Oportunidad Comercial"
            
            # Cuerpo del mensaje personalizado
            body = f"""
Estimado/a {nombre},

Esperamos que este mensaje le encuentre bien.

Nos complace presentarle nuestros servicios profesionales de compra y venta de metales, 
especializados en ofrecer soluciones integrales para sus necesidades comerciales e industriales.

Nuestros servicios incluyen:
• Compra y venta de metales preciosos y no preciosos
• Evaluación profesional de materiales
• Servicios de transporte y logística
• Asesoría técnica especializada
• Transacciones seguras y confidenciales

Para obtener información detallada sobre nuestros servicios, tarifas y condiciones, 
le invitamos a contactarnos directamente a través de nuestro correo corporativo:

correo@empresa.com

Nuestro equipo de especialistas estará encantado de atenderle y brindarle 
una propuesta personalizada que se ajuste a sus requerimientos específicos.

Agradecemos su interés y quedamos a su disposición para cualquier consulta adicional.

Atentamente,

Robot de Compra y Venta de Metales
Sistema Automatizado de Comunicación Corporativa
"""
            msg.attach(MIMEText(body, 'plain'))
            
            # Enviar correo
            server.send_message(msg)
            print(f"✅ Correo enviado a: {row['Correo']} (Nombre: {nombre})")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()

# Usar la función
if __name__ == "__main__":
    enviar_correos_desde_excel('Data/Base de datos.xlsx')