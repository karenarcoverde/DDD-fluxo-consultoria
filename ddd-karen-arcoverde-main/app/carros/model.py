from app.extensions import db

# Carros
# tabela que contem as informações sobre todos os carros
# id => chave primária
# cor => cor do carro: vermelho, branco, preto etc.
# descricao => uma breve descricao sobre o carro, história do carro etc.
# modelo => por exemplo Fiat Uno, modelo: Uno
# marca => por exemplo Fiat uno, marca: Fiat
# ano_fabricacao => ano em que foi fabricado o carro
# motor => motor 1.0, 2.0 etc.
# estoque => quantidade de um determinado carro que tem em estoque 
# preco => preço do carro
# nacional => se o carro é nacional (true) ou não (false)
# importada => se o carro é importado (true) ou não (false)

class Carros(db.Model):
        __tablename__ = 'carros'
        id = db.Column(db.Integer, primary_key = True)
        cor = db.Column(db.String(10), nullable = False)
        descricao = db.Column(db.String(50), nullable = False)
        modelo = db.Column(db.String(20), nullable = False)
        marca = db.Column(db.String(20), nullable = False)
        ano_fabricacao = db.Column(db.Integer, nullable = False)
        motor = db.Column(db.String(10), nullable = False)
        estoque = db.Column(db.Integer, nullable = False)
        preco = db.Column(db.Integer, nullable = False)
        nacional = db.Column(db.Boolean, nullable = False)
        importada = db.Column(db.Boolean, nullable = False)

        # carros(one) <-> carros carrinho(many)
        carros_carrinho = db.relationship('CarrosCarrinho', backref = 'carrosCarrinho')

        def json(self):
                return{
                'id':self.id,
                'cor':self.cor,
                'descricao':self.descricao,
                'modelo':self.modelo,
                'marca':self.marca,
                'ano_fabricacao':self.ano_fabricacao,
                'motor':self.motor,
                'estoque':self.estoque,
                'preco':self.preco,
                'nacional':self.nacional,
                'importada':self.importada
                }