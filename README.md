# Proyecto de Prueba con PostgreSQL y Python

## Requisitos

- **PostgreSQL**: Versión 16
- **Python**: Versión 3.10.10

## Configuración del Entorno

1. **Crear un entorno virtual**:

   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual**:

   - En **Windows**:
     ```bash
     venv\Scripts\activate
     ```

   - En **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar los paquetes necesarios**:

   Ejecuta el siguiente comando para instalar las dependencias desde el archivo `requirements.txt`:

   ```bash
   python manage.py -r requirements.txt
   ```

## Configuración de la Base de Datos

1. **Crear la base de datos**:

   Conéctate a PostgreSQL y ejecuta el siguiente comando para crear la base de datos:

   ```sql
   CREATE DATABASE ikbo_prueba;
   ```

2. **Ejecutar las migraciones**:

   Asegúrate de que el entorno virtual esté activado y luego ejecuta:

   ```bash
   python manage.py migrate
   ```

3. **Ejecutar el script SQL**:

   Ejecuta el archivo `tipo_ordenes.sql` en la base de datos `ikbo_prueba`:

## Notas

- Ajusta la ruta del script SQL según la estructura de tu proyecto.
- Para salir del entorno virtual, simplemente ejecuta el comando `deactivate`.