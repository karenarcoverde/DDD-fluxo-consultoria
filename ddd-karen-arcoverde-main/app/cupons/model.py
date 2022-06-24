from app.extensions import db

# Cupons
# tabela com as informações dos cupons de desconto
# id => chave primária
# codigo_cupom => os cupons possuem codigos para poder inserir no carrinho de compras
# valor_desconto => se o desconto é de 5%, 10% etc.
# quantidade => quantidade de cupons disponíveis
# categoria => se o cupom só é disponível em datas comemorativas, por exemplo, natal etc.

class Cupons(db.Model):
        __tablename__ = 'cupons'
        id = db.Column(db.Integer, primary_key = True)
        codigo_cupom = db.Column(db.Integer, nullable = False)
        valor_desconto = db.Column(db.Integer, nullable = False)
        quantidade = db.Column(db.Integer, nullable = False)
        categoria = db.Column(db.String(20), nullable = False)

        # cupons(many) <-> usuario(one)
        usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

        # carrinho(one) <-> cupons(one)
        carrinho = db.relationship("Carrinho", backref='Cupons', uselist=False)

         
        def json(self):
                return{
                'id':self.id,
                'codigo_cupom':self.codigo_cupom,
                'valor_desconto':self.valor_desconto,
                'quantidade':self.quantidade,
                'categoria':self.categoria
                }
