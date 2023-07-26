from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str
    organizacion: str
