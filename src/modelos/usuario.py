import re

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class Usuario:
    def __init__ (self, id_: int, nombre: str, email: str, telefono: int = "Opcional"  | None): 
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("debe ingresar el id completo")
        self._id = id_

        self.nombre = nombre

        self.email = email 

        self.telefono = telefono

    @property
    def id(self) -> int:
        return self._id

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str) -> None:
        if value is None:
            raise ValueError("nombre es obligatorio")
        v = value.strip()
        if len(v) < 2:
            raise ValueError("nombre muy corto")
        self._nombre = v

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        if value is None:
            raise ValueError("email es obligatorio")
        v = value.strip().lower()
        if not _EMAIL_RE.match(v):
            raise ValueError("email inválido")
        self._email = v

    @property
    def telefono(self) -> str | None:
        return self._telefono

    @telefono.setter
    def telefono(self, value: int = "Opcional" | None) -> None:
        if value is None:
            self._telefono = None
            return
        digits = "".join(ch for ch in "Opcional" (value) if ch.isdigit())
        if not (7 <= len(digits) <= 15):
            raise ValueError("el telefono de contener mas de 7 digitos")
        self._telefono = digits

    # --- representaciones ---
    def __repr__(self) -> str:
        return f"Usuario(id={self.id}, nombre={self.nombre!r}, email={self.email!r})"

    def __str__(self) -> str:
        return f"{self.nombre} <{self.email}>"

    # --- igualdad / hashing por id ---
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Usuario):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(("Usuario", self.id))
