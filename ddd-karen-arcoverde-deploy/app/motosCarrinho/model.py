from app.extensions import db
from app.models import BaseModel

# MotosCarrinho
# tabela que contem as motos colocadas no carrinho pelo usuário
# id => chave primária
# modelo => por exemplo Fiat Uno, modelo: Uno
# marca => por exemplo Fiat uno, marca: Fiat
# quantidade => quantidade de motos colocadas no carrinho 
# preco_unitario => preço de somente uma moto
# preco_total => preço total de todos as motos colocadas 

class MotosCarrinho(BaseModel):
        __tablename__ = 'MotosCarrinho'
        id = db.Column(db.Integer, primary_key = True)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # motos carrinho(many) <-> carrinho(one)
        carrinho = db.relationship('Carrinho', backref = 'MotosCarrinho')

        # motos(one) <-> carros carrinho(many)
        motos_id = db.Column(db.Integer, db.ForeignKey('motos.id'))