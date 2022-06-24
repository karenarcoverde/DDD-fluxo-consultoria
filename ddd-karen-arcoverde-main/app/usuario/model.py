from ..extensions import db

# Usuario
# tabela que contem as configurações do usuário
# id => chave primária
# nome => nome completo do usuário
# cpf => CPF do usuário
# email => email do usuário
# telefone => telefone residencial ou celular do usuário
# endereco => endereço completo do usuário: rua, número, complemento etc.

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(30), nullable = False)
    cpf = db.Column(db.String(15), unique = True, nullable = False)
    email = db.Column(db.String(50), unique = True, nullable = False)
    telefone = db.Column(db.String(15), nullable = False)
    endereco = db.Column(db.String(150), nullable = False)
    senha_hash = db.Column(db.String(200),nullable = False) 

    # carrinho(one) <-> usuario(one)
    carrinho = db.relationship('Carrinho', backref='Usuario', uselist=False)

    # cupons(many) <-> usuario(one)
    cupom = db.relationship('Cupons', backref='cupons_usuario')

    def json(self):
            return{
                'id':self.id,
                'nome':self.nome,
                'cpf':self.cpf,
                'email':self.email,
                'telefone':self.telefone,
                'endereco':self.endereco
            }
            