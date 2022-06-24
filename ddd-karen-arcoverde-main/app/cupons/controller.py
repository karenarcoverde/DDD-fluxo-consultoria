from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.cupons.model import Cupons

class CuponsDetalhes(MethodView): 
    def get(self):
        cupons = Cupons.query.all()
        return jsonify([cupom.json() for cupom in cupons]),200

    def post(self):
        dados = request.json        
        codigo_cupom = dados.get('codigo_cupom')
        valor_desconto = dados.get('valor_desconto')
        quantidade = dados.get('quantidade')
        categoria = dados.get('categoria')


        if isinstance (codigo_cupom,int) and isinstance (valor_desconto,str) and isinstance (quantidade,int) and isinstance (categoria,str):
            cupom = Cupons(codigo_cupom= codigo_cupom, valor_desconto = valor_desconto, quantidade = quantidade, categoria = categoria)
            db.session.add(cupom)
            db.session.commit()
            return cupom.json(),200
        return {"code_status":"invalid data in request"},400

class CuponsId(MethodView):
    def get (self,id):
        cupom = Cupons.query.get_or_404(id)
        return cupom.json()

    def put (self,id):
        dados = request.json
        codigo_cupom = dados.get('codigo_cupom')
        valor_desconto = dados.get('valor_desconto')
        quantidade = dados.get('quantidade')
        categoria = dados.get('categoria')

        cupom = Cupons.query.get_or_404(id)
        cupom.codigo_cupom = codigo_cupom
        cupom.valor_desconto = valor_desconto
        cupom.quantidade = quantidade
        cupom.categoria = categoria
        db.session.commit()
        return cupom.json(),200
      

    def patch (self,id):
        dados = request.json
        cupom = Cupons.query.get_or_404 (id)
  
        codigo_cupom = dados.get('codigo_cupom',Cupons.codigo_cupom)
        valor_desconto = dados.get('valor_desconto', Cupons.valor_desconto)
        quantidade = dados.get('quantidade',Cupons.quantidade)
        categoria = dados.get('categoria',Cupons.categoria)

        cupom.codigo_cupom = codigo_cupom
        cupom.valor_desconto = valor_desconto
        cupom.quantidade = quantidade
        cupom.categoria = categoria
        db.session.commit()
        return cupom.json(),200
    

    def delete(self,id):
        cupom = Cupons.query.get_or_404(id)
        db.session.delete (cupom)
        db.session.commit ()
        return {"code_status":"deletado"},200

