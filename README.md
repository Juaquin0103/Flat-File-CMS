# Flat-File CMS (Generación de Software) 🚀

Este proyecto es un sistema de gestión de contenidos de "archivo plano" desarrollado para la materia de **Generación de Software**. A diferencia de los CMS tradicionales, este sistema no utiliza bases de datos relacionales, optando por la persistencia de datos en archivos locales.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.11
* **Framework Web:** Flask (Micro-framework)
* **Formato de Contenido:** Markdown (.md)
* **Motor de Plantillas:** Jinja2

## 📁 Estructura del Proyecto

La arquitectura sigue una separación clara entre la lógica de negocio y el almacenamiento de contenido:

- `/content`: Directorio raíz para los archivos de datos (Markdown).
- `/static`: Recursos estáticos (CSS, Imágenes, JS).
- `/templates`: Plantillas HTML dinámicas.
- `app.py`: Núcleo del CMS y manejo de rutas.
- `requirements.txt`: Dependencias necesarias para la ejecución.

## 🚀 Instalación y Ejecución

Para ejecutar este proyecto localmente, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Juaquin0103/Flat-File-CMS.git]
   cd [GeneracionSW]
2. **Crear un entorno virtual:**
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
3. **Instalar dependencias:**
    pip install -r requirements.txt
4. **Correr la aplicacion:**
    python app.py
