from typing import Dict, List, Optional
from modelos.usuario import Usuario

DBType = Dict[str, List[Usuario]]

def add_usuario(db: DBType, id_: int, nombre: str, email: str, telefono: "Optional" [str] = None) -> Usuario:
    if any(u.id == id_ for u in db.setdefault("usuarios", [])):
        raise ValueError(f"Ya existe un usuario con id = {id_}")
    us = Usuario(id_, nombre, email, telefono)
    db["usuarios"].append(us)
    return us

def list_usuarios(db: DBType) -> List[Usuario]:
    return List(db.get("usuarios", []))
