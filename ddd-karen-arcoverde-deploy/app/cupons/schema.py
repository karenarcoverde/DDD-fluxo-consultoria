from ..extensions import ma
from .model import Cupons


class CuponsSchema(ma.SQLAlchemySchema):

    class Meta:
        model = Cupons
        load_instance = True
        ordered = True

    id = ma.Integer(dump_only=True)
    codigo_cupom = ma.Integer(required=True)
    valor_desconto = ma.Integer(required=True)
    quantidade = ma.Integer(required=True)
    categoria = ma.String(required=True)
    
    usuario_id = ma.Integer(load_only = True,required=True)
    
    # mostrar os cupons que cada usuario tem
    usuario = ma.Nested("UsuarioSchema", many=False)
