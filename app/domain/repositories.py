from abc import ABC, abstractmethod
from typing import List, Optional

from .models import Usuario

class UsuarioRepository(ABC):
    @abstractmethod
    def get_usuario(self, user_id: int) -> Optional[Usuario]:
        pass

    @abstractmethod
    def get_usuarios(self) -> List[Usuario]:
        pass

    @abstractmethod
    def create_usuario(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def update_usuario(self, user_id: int, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def delete_usuario(self, user_id: int) -> bool:
        pass
