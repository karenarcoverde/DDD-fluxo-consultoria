from ..extensions import ma
from .model import Carros


class CarrosSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Carros
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    descricao = ma.String(required=True)
    cor = ma.String(required=True)
    modelo = ma.String(required=True)
    marca = ma.String(required=True)
    ano_fabricacao = ma.Integer(required=True)
    motor = ma.String(required=True)
    estoque = ma.Integer(required=True)
    preco = ma.Integer(required=True)
    nacional = ma.Boolean(required=True)
    importada = ma.Boolean(required=True)