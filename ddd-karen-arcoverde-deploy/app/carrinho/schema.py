from ..extensions import ma
from .model import Carrinho


class CarrinhoSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Carrinho
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    forma_pagamento=ma.String(required=True)
    preco_frete=ma.Integer(required=True)
    quantidade=ma.Integer(required=True)
    preco_total = ma.Integer(required=True)

    CarrosCarrinho_id = ma.Integer(load_only = True,required=True)
    MotosCarrinho_id = ma.Integer(load_only = True,required=True)
    
    # mostrar os carros que estão no carrinho no carrinho final
    CarrosCarrinho = ma.Nested("CarrosCarrinhoSchema", many=False)

    # mostrar as motos que estão no carrinho no carrinho final
    MotosCarrinho = ma.Nested("MotosCarrinhoSchema", many=False)

    
      