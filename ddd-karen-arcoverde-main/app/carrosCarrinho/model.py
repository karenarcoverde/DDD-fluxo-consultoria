from app.extensions import db


# CarrosCarrinho
# tabela que contem os carros colocados no carrinho pelo usuário
# id => chave primária
# modelo => por exemplo Fiat Uno, modelo: Uno
# marca => por exemplo Fiat uno, marca: Fiat
# quantidade => quantidade de carros colocados no carrinho 
# preco_unitario => preço de somente um carro colocado no carrinho
# preco_total => preço total de todas os carros colocados no carrinho

class CarrosCarrinho(db.Model):
        __tablename__ = 'CarrosCarrinho'
        id = db.Column(db.Integer, primary_key = True)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_unitario = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # carros carrinho (many) <-> carrinho(one)
        carrinho_id = db.Column(db.Integer, db.ForeignKey('carrinho.id'))

        # carros(one) <-> carros carrinho(many)
        carros_id = db.Column(db.Integer, db.ForeignKey('carros.id'))

        def json(self):
                return{
                'id':self.id,
                'modelo':self.modelo,
                'marca':self.marca,
                'quantidade':self.quantidade,
                'preco_unitario':self.preco_unitario,
                'preco_total':self.preco_total
                }