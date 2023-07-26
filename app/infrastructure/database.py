from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.domain.repositories import UsuarioRepository
from typing import List, Optional


from app.domain.models import Usuario

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:12345678@localhost/gestion_usuarios")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class UsuarioORM(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo = Column(String, index=True)
    organizacion = Column(String, index=True)

def create_tables():
    Base.metadata.create_all(bind=engine)

def map_orm_user_to_model(usuario_orm: UsuarioORM) -> Usuario:
    return Usuario(id=usuario_orm.id,
                   nombre=usuario_orm.nombre,
                   correo=usuario_orm.correo,
                   organizacion=usuario_orm.organizacion)

def map_model_to_orm_user(usuario: Usuario) -> UsuarioORM:
    return UsuarioORM(id=usuario.id,
                      nombre=usuario.nombre,
                      correo=usuario.correo,
                      organizacion=usuario.organizacion)

class UsuarioRepositorySQLAlchemy(UsuarioRepository):
    def get_usuario(self, user_id: int) -> Optional[Usuario]:
        with SessionLocal() as session:
            usuario_orm = session.query(UsuarioORM).filter(UsuarioORM.id == user_id).first()
            return map_orm_user_to_model(usuario_orm) if usuario_orm else None

    def get_usuarios(self) -> List[Usuario]:
        with SessionLocal() as session:
            usuarios_orm = session.query(UsuarioORM).all()
            return [map_orm_user_to_model(usuario) for usuario in usuarios_orm]

    def create_usuario(self, usuario: Usuario) -> Usuario:
        usuario_orm = map_model_to_orm_user(usuario)
        with SessionLocal() as session:
            session.add(usuario_orm)
            session.commit()
            session.refresh(usuario_orm)
            return map_orm_user_to_model(usuario_orm)

    def update_usuario(self, user_id: int, usuario: Usuario) -> Usuario:
        with SessionLocal() as session:
            usuario_orm = session.query(UsuarioORM).filter(UsuarioORM.id == user_id).first()
            if usuario_orm:
                for key, value in usuario.dict(exclude_unset=True).items():
                    setattr(usuario_orm, key, value)
                session.commit()
                session.refresh(usuario_orm)
                return map_orm_user_to_model(usuario_orm)
            return None

    def delete_usuario(self, user_id: int) -> bool:
        with SessionLocal() as session:
            usuario_orm = session.query(UsuarioORM).filter(UsuarioORM.id == user_id).first()
            if usuario_orm:
                session.delete(usuario_orm)
                session.commit()
                return True
            return False
