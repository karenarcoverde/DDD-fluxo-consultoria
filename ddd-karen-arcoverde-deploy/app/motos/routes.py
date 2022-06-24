from flask import Blueprint

from app.motos.controller import MotosDetalhes, MotosId

motos_api = Blueprint('motos_api', __name__)

motos_api.add_url_rule(
    '/produtos', view_func= MotosDetalhes.as_view('Motos_detalhes'), methods=['GET','POST']
)

motos_api.add_url_rule(
    '/motos/<int:id>', view_func= MotosId.as_view('motos_id'), methods=['GET','PUT', 'PATCH','DELETE']
)