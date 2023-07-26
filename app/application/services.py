from typing import List, Optional

from app.domain.models import Usuario
from app.domain.repositories import UsuarioRepository

class UsuarioService:
    def __init__(self, usuario_repository: UsuarioRepository):
        self.usuario_repository = usuario_repository

    def get_usuario(self, user_id: int) -> Optional[Usuario]:
        return self.usuario_repository.get_usuario(user_id)

    def get_usuarios(self) -> List[Usuario]:
        return self.usuario_repository.get_usuarios()

    def create_usuario(self, usuario: Usuario) -> Usuario:
        return self.usuario_repository.create_usuario(usuario)

    def update_usuario(self, user_id: int, usuario: Usuario) -> Usuario:
        return self.usuario_repository.update_usuario(user_id, usuario)

    def delete_usuario(self, user_id: int) -> bool:
        return self.usuario_repository.delete_usuario(user_id)
