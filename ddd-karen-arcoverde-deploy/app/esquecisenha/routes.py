from flask import Blueprint
from app.esquecisenha.controller import SenhaMail, SenhaNova
esquecisenha_api = Blueprint('esquecisenha_api',__name__)


esquecisenha_api.add_url_rule(
         '/send_mail/reset', view_func = SenhaMail.as_view('mail_reset'), methods = ['POST'])

esquecisenha_api.add_url_rule(
         '/reset/<string:token>', view_func = SenhaNova.as_view('reset'), methods = ['PATCH'])