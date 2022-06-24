from ..extensions import ma
from .model import MotosCarrinho


class MotosCarrinhoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = MotosCarrinho
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    modelo = ma.String(required=True)
    marca = ma.String(required=True)
    quantidade = ma.Integer(required=True)
    preco_unitario = ma.Integer(required=True)
    preco_total = ma.Integer(required=True)
