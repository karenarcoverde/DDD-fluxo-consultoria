from flask import Blueprint

from app.usuario.controller import UsuarioDetalhes,UsuarioId, UsuarioLogin

usuario_api = Blueprint('usuario_api', __name__)

usuario_api.add_url_rule(
    '/usuarios', view_func= UsuarioDetalhes.as_view('usuario_detalhes'), methods=['GET','POST']
)

usuario_api.add_url_rule(
    '/usuarios/<int:id>', view_func= UsuarioId.as_view('usuario_id'), methods=['GET','PUT', 'PATCH','DELETE']
)

usuario_api.add_url_rule(
    '/login', view_func= UsuarioLogin.as_view('usuario_login'), methods=['POST']
)