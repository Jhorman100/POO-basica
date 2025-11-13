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
def emit (msg: str, printer = print) -> None:
    printer(msg)

def format_title (title: str) -> str:
    return f"\n{title} \n {'-' * len (title)}"

def list_usuarios(db: DBType) -> None:
    usuarios = db ["usuarios"]
    if not usuarios:
        raise ValueError ("no hay gullosos registrados")
    return list (usuarios.values())

def list_tickets(db :DBType) -> None:
    tickets = db ["tickets"]
    if not tickets:
        raise ValueError ("gulloso no tiene tickets")
    return list (tickets.values())







def run(db: DBType, input_func: InputFn = input, printer = print) -> None:
    emit(format_title("Taller POO basica - Menu"), printer)
    while True:
        emit(MENU.strip(), printer)
        try:
           opcion = input_func("opcion: ").strip()
        if opcion == 0:
            emit("Hasta luego.", printer)
            break
        try:
            handle_option(opcion, db, input_func, printer)
        except Exception as ex:
            emit(format_error(str(ex)), printer)

def handle_option(opcion: str, db: DBType, input_func: InputFn, printer=print) -> None:
    if opcion == "1":
        usuarios = list_usuarios(db)
        headers = ["id", "nombre", "email", "telefono"]
        rows = [(u.id, u.nombre, u.email, u.telefono or "") for u in usuarios]
        emit(format_table(headers, rows), printer)

    elif opcion == "2":
        id_ = int(input_func("id: "))
        nombre = input_func("nombre: ")
        email = input_func("email: ")
        telefono = input_func("telefono (opcional): ").strip() or None
        us = add_usuario(db, id_, nombre, email, telefono)
        emit(format_success(f"Usuario creado: {us}"), printer)

    elif opcion == "3":
        tickets = list_tickets(db)
        headers = ["id", "usuario_id", "titulo", "prioridad", "estado"]
        rows = [(t.id, t.usuario_id, t.titulo, t.prioridad, t.estado) for t in tickets]
        emit(format_table(headers, rows), printer)

    elif opcion == "4":
        id_ = int(input_func("id: "))
        usuario_id = int(input_func("usuario_id: "))
        titulo = input_func("titulo: ")
        prioridad = input_func("prioridad: ")
        estado = input_func("estado: ")
        tick = add_ticket(db, id_, usuario_id, prioridad, estado)
        emit(format_success(f"Ticket creado: {tick}"), printer)