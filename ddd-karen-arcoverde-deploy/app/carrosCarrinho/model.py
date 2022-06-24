from app.extensions import db
from app.models import BaseModel

# CarrosCarrinho
# tabela que contem os carros colocados no carrinho pelo usuário
# id => chave primária
# modelo => por exemplo Fiat Uno, modelo: Uno
# marca => por exemplo Fiat uno, marca: Fiat
# quantidade => quantidade de carros colocados no carrinho 
# preco_unitario => preço de somente um carro colocado no carrinho
# preco_total => preço total de todas os carros colocados no carrinho

class CarrosCarrinho(BaseModel):
        __tablename__ = 'CarrosCarrinho'
        id = db.Column(db.Integer, primary_key = True)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # carros carrinho(many) <-> carrinho(one)
        carrinho = db.relationship('Carrinho', backref = 'CarrosCarrinho')

        # carros(one) <-> carros carrinho(many)
        carros_id = db.Column(db.Integer, db.ForeignKey('carros.id'))