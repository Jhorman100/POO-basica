from typing import Dict, List
from modelos.ticket import Ticket

DBType = Dict[str, List[Ticket]]

def add_ticket(db: DBType, id_: int, usuario_id: int, titulo: int, prioridad: str = "media", estado: str = "abierto") -> Ticket:
    if any(t.id == id_ for t in db.setdefault("tickets", [])):
        raise ValueError(f"Ya existe un ticket con id={id_}")
    tick = Ticket(id_, usuario_id, titulo, prioridad, estado)
    db["tickets"].append(tick)
    return tick

def list_tickets(db: DBType) -> list[Ticket]:
    return list(db.get("tickets",[]))

    