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

def preview_email():
    """Mostrar una vista previa del correo que se enviará"""
    
    # Configuración del correo (puedes modificar esto)
    subject = "Servicios de Compra y Venta de Metales - Oportunidad Comercial"
    body = f"""
Estimado/a {{nombre}},

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

nicolas.klauser@gmail.com

Nuestro equipo de especialistas estará encantado de atenderle y brindarle 
una propuesta personalizada que se ajuste a sus requerimientos específicos.

Agradecemos su interés y quedamos a su disposición para cualquier consulta adicional.

Atentamente,

Robot de Compra y Venta de Metales
Sistema Automatizado de Comunicación Corporativa
"""
    
    print("=" * 50)
    print("VISTA PREVIA DEL CORREO")
    print("=" * 50)
    print(f"De: {sender_email}")
    print(f"Asunto: {subject}")
    print("-" * 50)
    print("Cuerpo del mensaje:")
    print(body)
    print("=" * 50)
    
    # Preguntar si quiere enviar un correo de prueba
    respuesta = input("¿Quieres enviar un correo de prueba a ti mismo? (s/n): ")
    
    if respuesta.lower() in ['s', 'si', 'sí', 'y', 'yes']:
        try:
            # Conectar al servidor SMTP
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, password)
            
            # Crear mensaje
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = sender_email  # Enviar a ti mismo
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            # Enviar correo
            server.send_message(msg)
            print("✅ Correo de prueba enviado exitosamente!")
            print("Revisa tu bandeja de entrada para ver el correo.")
            
            server.quit()
            
        except Exception as e:
            print(f"❌ Error al enviar correo de prueba: {e}")
    else:
        print("No se envió correo de prueba.")

if __name__ == "__main__":
    preview_email() 