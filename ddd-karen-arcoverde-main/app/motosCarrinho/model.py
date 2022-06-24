from app.extensions import db


# MotosCarrinho
# tabela que contem as motos colocadas no carrinho pelo usuário
# id => chave primária
# modelo => por exemplo Fiat Uno, modelo: Uno
# marca => por exemplo Fiat uno, marca: Fiat
# quantidade => quantidade de motos colocadas no carrinho 
# preco_unitario => preço de somente uma moto
# preco_total => preço total de todos as motos colocadas 

class MotosCarrinho(db.Model):
        __tablename__ = 'MotosCarrinho'
        id = db.Column(db.Integer, primary_key = True)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # motos carrinho (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # motos(one) <-> carros carrinho(many)
        motos_id = db.Column(db.Integer, db.ForeignKey('motos.id'))

        def json(self):
                return{
                'id':self.id,
                'modelo':self.modelo,
                'marca':self.marca,
                'quantidade':self.quantidade,
                'preco_unitario':self.preco_unitario,
                'preco_total':self.preco_total
                }