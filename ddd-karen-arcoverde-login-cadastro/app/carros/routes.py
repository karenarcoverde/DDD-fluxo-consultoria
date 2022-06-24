from flask import Blueprint

from app.carros.controller import CarrosDetalhes, CarrosId

carros_api = Blueprint('carros_api', __name__)

carros_api.add_url_rule(
    '/carros', view_func= CarrosDetalhes.as_view('carros_detalhes'), methods=['GET','POST']
)

carros_api.add_url_rule(
    '/carros/<int:id>', view_func= CarrosId.as_view('carros_id'), methods=['GET','PUT', 'PATCH','DELETE']
)