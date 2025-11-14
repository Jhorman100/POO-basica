from __future__ import annotations
from typing import Callable, Dict

InputFn = Callable[[str], str]
DBType = Dict[str, list]

MENU = """
[1] listar usuario
[2] Crear usuario
[3] Listar tickets
[4] Crear ticket
[5] Cambiar estado de ticket
[6] Listar tickets por estado
[0] Salir
"""

def emit(msg: str, printer=print) -> None:
    printer(msg)

def format_title(title: str) -> str:
    return f"\n{title} \n {'-' * len(title)}"

def list_usuarios(db: DBType) -> None:
    usuarios = db["usuarios"]
    if not usuarios:
        raise ValueError("no hay usuarios registrados")
    return list(usuarios.values())

def list_tickets(db: DBType) -> None:
    tickets = db["tickets"]
    if not tickets:
        raise ValueError("usuario no tiene tickets")
    return list(tickets.values())

def format_usuario(usuario: dict) -> str:
    return f"{usuario['id']: 3d} | {usuario['nombre']:<20s} | {usuario['email']:<30s} | {usuario['telefono']}"

def format_ticket(ticket: dict) -> str:
    return f"{ticket['id']: 3d} | {ticket['titulo']:<30s} | {ticket['estado']:<12s} | {ticket['prioridad']}"

def input_format(prompt: str, validator: Callable[[str], bool], error_msg: str, input_func: callable) -> str:
    value = input_func(prompt).strip()
    if validator(value):
        return value
    else:
        print(f"\nError: {error_msg}")
        return None

def run(db: DBType, input_func: InputFn = input, printer=print) -> None:
    emit(format_title("Taller POO básica - Menú"), printer)
    while True:
        emit(MENU.strip(), printer)
        opcion = input_format(
            "Opción: ",
            lambda x: x.isdigit(),
            "Debes ingresar un número del menú",
            input_func
        ).strip()
        if opcion == "0":
            emit("Hasta luego.", printer)
            break
        handle_option(opcion, db, input_func, printer)

def handle_option(opcion: str, db: DBType, input_func: InputFn, printer=print) -> None:
    if opcion == "1":
        usuarios = list_usuarios(db)
        if not usuarios:
            ("No hay usuarios registrados", printer)
            return
        emit("\nUsuarios registrados:", printer)
        emit("ID  | Nombre               | Email                          | Teléfono", printer)
        emit("-" * 75, printer)
        for u in usuarios:
            emit(format_usuario(u), printer)

    elif opcion == "2":
        try:
            nombre = input_format(
                "Nombre: ",
                lambda x: len(x.strip()) >= 2,
                "El nombre debe tener al menos 2 caracteres",
                input_func
            )
            
            email = input_format(
                "Email: ",
                lambda x: "@" in x and "." in x,
                "El email debe ser válido (ejemplo: jhorman@gmail.com)",
                input_func
            )

            telefono = input_func("Teléfono (opcional): ").strip()
            if telefono:
                if len("".join(c for c in telefono if c.isdigit())) < 7:
                    telefono = input_format(
                        "Teléfono (debe tener al menos 7 dígitos): ",
                        lambda x: len("".join(c for c in x if c.isdigit())) >= 7,
                        "El teléfono debe tener al menos 7 dígitos",
                        input_func
                    )
            else:
                telefono = None
            
            id = len(db["usuarios"]) + 1
            usuario = {
                "id": id,
                "nombre": nombre,
                "email": email,
                "telefono": telefono
            }
            db["usuarios"][id] = usuario
            emit("Usuario creado exitosamente", printer)
        except ValueError as e:
            raise ValueError(f"Error al crear usuario: {str(e)}")

    elif opcion == "3":
        tickets = list_tickets(db)
        if not tickets:
            emit("No hay tickets registrados", printer)
            return
        emit("\nTiTickets registrados:", printer)
        emit("ID  | Titulo               | Estado                          | Prioridad", printer)
        emit("-" * 65, printer)
        for t in tickets:
            emit(format_ticket(t), printer)

    elif opcion == "4":
        try:
            titulo = input_format(
                "Titulo: ",
                lambda x: len(x.strip()) >= 5,
                "El titulo debe tener al menos 5 caracteres",
                input_func
            )

            descripcion = input_format(
                "Descripcion: ",
                lambda x: len(x.strip()) >= 10,
                "La descripcion debe tener al menos 10 caracteres",
                input_func
            )

            prioridad = input_format(
                "Prioridad (alta/media/baja): ",
                lambda x: x.lower() in {"alta", "media", "baja"},
                "La prioridad debe ser alta, media o baja",
                input_func
            ).lower()

            id = len(db["tickets"]) + 1
            ticket = {
                "id": id,
                "titulo": titulo,
                "prioridad": prioridad,
                "estado": "abierto"
            }

            db["tickets"][id] = ticket
            emit("se ha creado un ticket exitosamente", printer)
        except ValueError as e:
            raise ValueError(f"Error al crear el ticket: {str(e)}")

    elif opcion == "5":
        try:
            id_str = input_format(
                "ID del ticket: ",
                lambda x: x.isdigit() and int(x) in db["tickets"],
                "ID del ticket no es valido",
                input_func
            )
            id = int(id_str)
            
            nuevo_estado = input_format(
                "Nuevo estado (abierto / en progreso / cerrado): ",
                lambda x: x.lower() in {"abierto", "en progreso", "cerrado"},
                "El estado debe ser abierto, en progreso o cerrado",
                input_func
            ).lower()
            
            db["tickets"][id]["estado"] = nuevo_estado
            emit("Estado actualizado exitosamente", printer)
        except ValueError as e:
            raise ValueError(f"Error al actualizar estado: {str(e)}")

    elif opcion == "6":
        estado = input_format(
            "Estado a filtrar (abierto / en progreso / cerrado): ",
            lambda x: x.lower() in {"abierto", "en progreso", "cerrado"},
            "Estado debe ser abierto, en progreso o cerrado",
            input_func
        ).lower()
        
        tickets = [t for t in db["tickets"].values() if t["estado"] == estado]
        if not tickets:
            emit(f"No hay tickets en estado '{estado}'", printer)
            return
        
        emit(f"\nTickets en estado '{estado}':", printer)
        emit("ID  | Título                         | Estado       | Prioridad", printer)
        emit("-" * 65, printer)
        for t in tickets:
            emit(format_ticket(t), printer)

    else:
        raise ValueError(f"Opción inválida: {opcion}")
        
        
      

    