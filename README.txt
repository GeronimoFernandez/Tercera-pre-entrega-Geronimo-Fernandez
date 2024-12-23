# Tercera Pre-Entrega - Geronimo Fernadnez

## Descripción del Proyecto

Este proyecto es una aplicación de Django donde se gestionan funcionalidades relacionadas con el tema de "lobby" de un sistema. La aplicación permite interactuar con diferentes vistas y funcionalidades como la página principal y las vistas relacionadas con el lobby.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/Tercera-pre-entregaApellido.git
    ```

2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

4. Corre el servidor local:
    ```bash
    python manage.py runserver
    ```

5. Accede a la aplicación en el navegador:
    - Abre tu navegador y ve a `http://127.0.0.1:8000/`.

## Funcionalidades

**Lobby**: La primera pantalla que verás al ingresar a la URL principal (`http://127.0.0.1:8000/`) es el "Lobby".
- **Vista de "Lobby"**: Aquí puedes encontrar las funcionalidades iniciales y las interacciones del sistema. La página de lobby sirve como punto de entrada para probar otras partes del proyecto.
- **Autenticación de usuario**: Si implementaste autenticación (inicio de sesión o registro), indícalo aquí y proporciona detalles sobre cómo probar esas funcionalidades.
- **Formularios**: Si tienes formularios en el proyecto (por ejemplo, formularios de contacto o creación de usuarios), menciona en qué URL se encuentran y cómo probarlos.
## Orden de pruebas

A continuación se indica el orden en el que se recomienda probar las funcionalidades de la aplicación:

1. **Prueba el "Lobby"**:
   - Accede a la URL principal (`http://127.0.0.1:8000/`) para ver cómo se carga la página del lobby.
   
2. **Prueba las funcionalidades adicionales**:
   - Accede a `http://127.0.0.1:8000/lobby/` para ver otras vistas relacionadas con el lobby.
   
3. **Verifica los formularios y el comportamiento en la vista**:
   - Si tienes formularios u otros elementos interactivos, indícalos aquí.


