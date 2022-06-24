from ..extensions import ma
from .model import Usuario


class UsuarioSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Usuario
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    nome=ma.String(required=True)
    cpf=ma.String(required=True)
    email=ma.Email(required=True)
    telefone=ma.Integer(required=True)
    endereco=ma.String(required=True)
    senha = ma.String(Load_only=True, required=True)

    
class LoginSchema(ma.Schema):
    email = ma.Email(required=True)
    senha = ma.String(load_only=True, required=True)
