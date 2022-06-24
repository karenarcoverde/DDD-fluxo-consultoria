from flask import Blueprint

from app.motosCarrinho.controller import MotosCarrinhoDetalhes, MotosCarrinhoId

motoscarrinho_api = Blueprint('motoscarrinho_api', __name__)

motoscarrinho_api.add_url_rule(
    '/motoscarrinho', view_func= MotosCarrinhoDetalhes.as_view('motoscarrinho_detalhes'), methods=['GET','POST']
)

motoscarrinho_api.add_url_rule(
    '/motoscarrinho/<int:id>', view_func= MotosCarrinhoId.as_view('motoscarrinho_id'), methods=['GET','PUT', 'PATCH','DELETE']
)