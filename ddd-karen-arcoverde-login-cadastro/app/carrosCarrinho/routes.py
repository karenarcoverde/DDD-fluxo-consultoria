from flask import Blueprint

from app.carrosCarrinho.controller import CarrosCarrinhoDetalhes, CarrosCarrinhoId

carroscarrinho_api = Blueprint('carroscarrinho_api', __name__)

carroscarrinho_api.add_url_rule(
    '/carroscarrinho', view_func= CarrosCarrinhoDetalhes.as_view('carroscarrinho_detalhes'), methods=['GET','POST']
)

carroscarrinho_api.add_url_rule(
    '/carroscarrinho/<int:id>', view_func= CarrosCarrinhoId.as_view('carroscarrinho_id'), methods=['GET','PUT', 'PATCH','DELETE']
)