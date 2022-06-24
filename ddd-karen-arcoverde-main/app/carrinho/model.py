from app.extensions import db

# Carrinho
# tabela com as informações necessárias para poder pagar o que contem no carrinho
# id => chave primária
# forma_pagamento => pode ser PIX, boleto bancario, cartao de crédito etc.
# preco_frete => preço diferente para cada regiao e para cada transporte
# quantidade => quantidade de itens no carrinho
# preco_total => preço total, incluindo tudo que foi colocado no carrinho

class Carrinho(db.Model):
        __tablename__ = 'carrinho'
        id = db.Column(db.Integer, primary_key = True)
        forma_pagamento = db.Column(db.String(40), nullable = False)
        preco_frete = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        preco_total = db.Column(db.Integer, nullable = False)

        # carrinho(one) <-> cupons(one)
        cupons_id = db.Column(db.Integer, db.ForeignKey('cupons.id'))

        # novidades carrinho(many) <-> carrinho(one)
        novidades_carrinho = db.relationship('NovidadesCarrinho', backref = 'novidadesCarrinho_carrinho')

        # produtos carrinho(many) <-> carrinho(one)
        produtos_carrinho = db.relationship('ProdutosCarrinho', backref = 'produtosCarrinho_carrinho')

        # carrinho(one) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
       
        def json(self):
                return{
                'id':self.id,
                'forma_pagamento':self.forma_pagamento,
                'preco_frete':self.preco_frete,
                'quantidade':self.quantidade,
                'preco_total':self.preco_total
                }
