from ..extensions import db
from app.models import BaseModel
import bcrypt
from flask_jwt_extended import create_access_token
from sqlalchemy.orm import backref
from app.utils import storage

# Usuario
# tabela que contem as configurações do usuário
# id => chave primária
# nome => nome completo do usuário
# cpf => CPF do usuário
# email => email do usuário
# telefone => telefone residencial ou celular do usuário
# endereco => endereço completo do usuário: rua, número, complemento etc.
# senha => senha do usuário para fazer o login
# avatar => Foto de identificação do usuário relacionado ao digital ocean

class Usuario(BaseModel):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    cpf = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    telefone = db.Column(db.String(15), nullable = False)
    endereco = db.Column(db.String(150), nullable = False)
    senha_hash = db.Column(db.LargeBinary(128),nullable = False) 
    avatar = db.Column(db.String(64), unique = True, default = None )

    # carrinho(one) <-> usuario(one)
    carrinho = db.relationship('Carrinho', backref='Usuario', uselist=False)

    # cupons(many) <-> usuario(one)
    cupons = db.relationship('Cupons', backref='usuario')

    @property
    def avatar_url(self):
        if self.avatar:
            return storage.get_url(self.avatar)
        return None

    @avatar_url.setter
    def avatar_url(self,name):
        if self.avatar:
            storage.delete_object(self.avatar)
        self.avatar = name

    @property
    def senha(self):
        raise AttributeError('password is not a readable attribute')

    @senha.setter
    def senha(self, senha) -> None:
        self.senha_hash = bcrypt.hashpw(
            senha.encode(), bcrypt.gensalt())

    def verify_senha(self, senha) -> bool:
        return bcrypt.checkpw(senha.encode(), self.senha_hash)

    def token(self) -> str:
        return create_access_token(
            identity=self.id)