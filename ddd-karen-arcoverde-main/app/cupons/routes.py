from flask import Blueprint

from app.cupons.controller import CuponsDetalhes, CuponsId

cupons_api = Blueprint('cupons_api', __name__)

cupons_api.add_url_rule(
    '/cupons', view_func= CuponsDetalhes.as_view('cupons_detalhes'), methods=['GET','POST']
)

cupons_api.add_url_rule(
    '/cupons/<int:id>', view_func= CuponsId.as_view('cupons_id'), methods=['GET','PUT', 'PATCH','DELETE']
)