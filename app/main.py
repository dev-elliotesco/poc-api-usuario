from fastapi import FastAPI, HTTPException, Depends

from app.infrastructure.database import create_tables
from app.infrastructure.database import UsuarioRepositorySQLAlchemy
from app.application.services import UsuarioService
from app.domain.models import Usuario

from typing import List


app = FastAPI()

# Crear las tablas en la base de datos
create_tables()

# Inyectar el repositorio y el servicio de usuarios en la aplicación
usuario_repository = UsuarioRepositorySQLAlchemy()
usuario_service = UsuarioService(usuario_repository)

@app.get("/usuarios/{user_id}", response_model=Usuario)
def read_usuario(user_id: int):
    usuario = usuario_service.get_usuario(user_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/usuarios/", response_model=List[Usuario])
def read_usuarios():
    return usuario_service.get_usuarios()

@app.post("/usuarios/", response_model=Usuario)
def create_usuario(usuario: Usuario):
    return usuario_service.create_usuario(usuario)

@app.put("/usuarios/{user_id}", response_model=Usuario)
def update_usuario(user_id: int, usuario: Usuario):
    updated_usuario = usuario_service.update_usuario(user_id, usuario)
    if updated_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated_usuario

@app.delete("/usuarios/{user_id}", response_model=bool)
def delete_usuario(user_id: int):
    return usuario_service.delete_usuario(user_id)
