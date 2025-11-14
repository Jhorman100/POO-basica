# Tickets de Soporte

mesa de ayuda interna para registrar y consultar tickets de soporte asociados a usuarios, permite gestionar Usuarios y Tickets

# Estructura del proyecto

taller POO_basica/
├── main.py
├── src/
│   ├── controladores/
│   │   ├── tickets.py
│   │   └── usuarios.py
│   ├── modelos/
│   │   ├── ticket.py
│   │   └── usuario.py
│   └── views/
│       └── menu.py


# Funciones

# Gestión de Usuarios
Listar usuarios
Crear usuario (nombre, email, teléfono opcional)
Validación de datos

# Gestión de Tickets
Listar tickets
Crear ticket (título, descripción, prioridad)
Cambiar estado de ticket (abierto/en progreso/cerrado)
Filtrar tickets por estado



# se va a mostar en el menu principal las siguientes opciones


[1] Listar usuarios
[2] Crear usuario
[3] Listar tickets
[4] Crear ticket
[5] Cambiar estado de ticket
[6] Listar tickets por estado
[0] Salir

# Validaciones

# Usuarios
Nombre
Email
Teléfono

# Tickets
Título
Descripción
Prioridad
Estado

# Requisitos
Python 3.10