from typing import Opcional
from enum import Enum

class Prioridad(Enum):
    BAJA = "baja"
    MEDIA = "media"
    ALTA = "alta"


class Estado(Enum):
    ABIERTO = "abierto"
    EN_PROCESO = "en_proceso"
    CERRADO = "cerrado"


class Ticket:
    
    __slots__ = ("_id", "_usuario_id", "_descripcion", "_prioridad", "_estado")

# mirar bien si en prioridad y estado va primero con el guion bajo al principio _

    def __init__(self, id_: int, usuario_id: int, titulo: int, descripcion: str = "opcional", prioridad: str = "media", estado: str = "abierto"):
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("debe ingresar el id completo")
        if not isinstance(usuario_id, int) or usuario_id <= 0:
            raise ValueError("el usuario_id debe ser ingresado completo")
        
        self._id = id_
        self._usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion    
        self.prioridad = prioridad
        self.estado = estado

    @property
    def id(self) -> int:
        return self._id

    @property
    def usuario_id(self) -> int:
        return self._usuario_id

    @property
    def titulo(self) -> titulo:
        return self._titulo

    @titulo.setter
    def titulo(self, value: titulo) -> None:
        if value is None:
                raise ValueError("titulo no puede quedar vacio")
        v = value.strip()
     
    @property
    def descripcion(self) -> Opcional[str]:
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value: Opcional[str]) -> None:
        if value is None:
            self._descripcion = None
        else:
            texto = value.strip()
            if not texto:
                raise ValueError("La descripción no puede estar vacía.")
            self._descripcion = texto
    
    @property
    def prioridad(self) -> Prioridad:
        return self._prioridad

    @prioridad.setter
    def prioridad(self, value: Prioridad) -> None:
        if not isinstance(value, Prioridad):
            raise ValueError("La prioridad debe ser una instancia de Prioridad.")
        self._prioridad = value

    @property
    def estado(self) -> Estado:
        return self._estado

    @estado.setter
    def estado(self, value: Estado) -> None:
        if not isinstance(value, Estado):
            raise ValueError("El estado debe ser una instancia de Estado.")
        self._estado = value
    
    def cambiar_prioridad(self, nueva_prioridad: Prioridad) -> None:
        if not isinstance(nueva_prioridad, Prioridad):
            raise ValueError("El nuevo prioridad debe ser una instancia de Prioridad.")
        if nueva_prioridad == self._prioridad:
            print(f"el ticket ya está en prioridad '{nueva_prioridad.value}'.")
            return
        print(f"cambiando prioridad de '{self._prioridad.value}' a '{nueva_prioridad.value}'...")
        self.prioridad = nueva_prioridad
        print("La prioridad se actualizo correctamente")
    
    def cambiar_estado(self, nuevo_estado: Estado) -> None:
        if not isinstance(nuevo_estado, Estado):
            raise ValueError("El nuevo estado debe ser una instancia de Estado.")
        if nuevo_estado == self._estado:
            print(f"el ticket ya está en estado '{nuevo_estado.value}'.")
            return
        print(f"cambiando estado de '{self._estado.value}' a '{nuevo_estado.value}'...")
        self.estado = nuevo_estado
        print("El estado se actualizo correctamente")
    

    # este es el nuevo