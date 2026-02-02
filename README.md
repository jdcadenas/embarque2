# Sistema de Gestión de Importaciones

Este es un sistema de gestión de importaciones desarrollado con Django. Permite a los usuarios administrar productos, categorías y embarques de importación.

## Características

*   **Gestión de Productos:** Crear, leer, actualizar y eliminar productos.
*   **Gestión de Categorías:** Organizar productos en categorías.
*   **Gestión de Embarques:** Rastrear y administrar los embarques de importación.
*   **Interfaz de Administración:** Interfaz de administración de Django para una fácil gestión de datos.
*   **Interfaz de Grappelli:** Una interfaz de administración más moderna y amigable.

## Requisitos

*   Python 3.x
*   Django
*   django-grappelli
*   Pillow

## Instalación

1.  Clona este repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```
2.  Crea y activa un entorno virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows usa `.venv\Scripts\activate`
    ```
3.  Instala las dependencias:
    ```bash
    pip install -r requeriments.txt
    ```
4.  Aplica las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```
5.  Crea un superusuario para acceder al admin:
    ```bash
    python manage.py createsuperuser
    ```
6.  Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

1.  Accede a la interfaz de administración en `http://127.0.0.1:8000/admin/`.
2.  Inicia sesión con las credenciales de superusuario.
3.  Administra tus productos, categorías y embarques.
