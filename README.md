# Sistema de Envío de Correos para Servicios de Metales

## Descripción
Este proyecto es un sistema automatizado para enviar correos electrónicos masivos a partir de datos almacenados en un archivo Excel. Está diseñado para facilitar campañas de marketing,
notificaciones o comunicaciones empresariales de forma personalizada y eficiente.

## Características
- Envío de correos electrónicos personalizados a múltiples destinatarios
- Soporte para correos en formato texto plano y HTML
- Verificación de la estructura del archivo Excel
- Herramientas de prueba y depuración
- Vista previa de correos antes de enviarlos

## Requisitos
- Python 3.6 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Clona o descarga este repositorio
2. Instala las dependencias:

```
pip install -r requirements.txt
```

3. Configura tus credenciales en el archivo `config.env`

## Uso

### Configuración
Edita el archivo `config.env` con tus credenciales de correo electrónico:

```
EMAIL_USER=tu_correo@gmail.com
EMAIL_PASSWORD=tu_contraseña_o_clave_de_app
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Preparación de datos
1. Asegúrate de tener un archivo Excel en la carpeta `Data/Base de datos.xlsx` con las columnas `Correo` y `Nombre`
2. Puedes crear un archivo de ejemplo con `crear_excel_ejemplo.py`
3. Verifica la estructura del archivo con `verificar_excel.py`

### Envío de correos

#### Correos en formato texto plano
Ejecuta el script principal:

```
python Main.py
```

#### Correos en formato HTML (Nuevo)
Ejecuta el script para envío de correos HTML:

```
python enviar_email_html.py
```

Selecciona la opción 1 para enviar correos o la opción 2 para ver una vista previa.

### Pruebas

#### Prueba de conexión SMTP
```
python test_email.py
```

#### Prueba de correo HTML
```
python test_email_html.py
```

## Personalización

### Plantilla HTML
Puedes modificar el diseño del correo HTML editando el archivo `email_template.html`. La plantilla utiliza la variable `{nombre}` que será reemplazada por el nombre del destinatario.

## Solución de problemas

Si encuentras problemas al enviar correos, verifica:

1. Que las credenciales en `config.env` sean correctas
2. Si usas Gmail, asegúrate de:
   - Tener habilitado el acceso a aplicaciones menos seguras, o
   - Usar una contraseña de aplicación
3. Que el archivo Excel tenga la estructura correcta

## Archivos del proyecto

- `Main.py`: Script principal para envío de correos en texto plano
- `enviar_email_html.py`: Script para envío de correos en formato HTML
- `email_template.html`: Plantilla HTML para los correos
- `test_email.py`: Prueba de conexión SMTP y envío de correo de texto
- `test_email_html.py`: Prueba de envío de correo HTML
- `verificar_excel.py`: Verifica la estructura del archivo Excel
- `crear_excel_ejemplo.py`: Crea un archivo Excel de ejemplo
- `config.env`: Archivo de configuración con credenciales

## By EyelessEngine
