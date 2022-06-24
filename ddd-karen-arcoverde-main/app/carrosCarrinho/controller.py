from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.carrosCarrinho.model import CarrosCarrinho

class CarrosCarrinhoDetalhes(MethodView): 
    def get(self):
        carroscarrinho = CarrosCarrinho.query.all()
        return jsonify([carrocarrinho.json() for carrocarrinho in carroscarrinho]),200

    def post(self):
        dados = request.json        
        modelo = dados.get('modelo')
        marca = dados.get('marca')
        quantidade = dados.get('quantidade')
        preco_unitario = dados.get('preco_unitario')
       
        preco_total = quantidade * preco_unitario
       
        if isinstance (modelo,str) and isinstance (marca,str) and isinstance (quantidade,int) and isinstance (preco_unitario,int) and isinstance (preco_total,int):
            novidadecarrinho = CarrosCarrinho(modelo= modelo, marca = marca, quantidade = quantidade, preco_unitario = preco_unitario, preco_total = preco_total)
            db.session.add(novidadecarrinho)
            db.session.commit()
            return novidadecarrinho.json(),200
        return {"code_status":"invalid data in request"},400

class CarrosCarrinhoId(MethodView):
    def get (self,id):
        carrocarrinho = CarrosCarrinho.query.get_or_404(id)
        return carrocarrinho.json()

    def put (self,id):
        dados = request.json
        modelo = dados.get('modelo')
        marca = dados.get('marca')
        quantidade = dados.get('quantidade')
        preco_unitario = dados.get('preco_unitario')

        carrocarrinho = CarrosCarrinho.query.get_or_404(id)
        carrocarrinho.modelo = modelo
        carrocarrinho.marca = marca

        carrocarrinho.quantidade = quantidade
        carrocarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return carrocarrinho.json(),200
      

    def patch (self,id):
        dados = request.json
        carrocarrinho= CarrosCarrinho.query.get_or_404 (id)
  
        modelo= dados.get('modelo',CarrosCarrinho.modelo)
        marca= dados.get('marca',CarrosCarrinho.marca)
        quantidade = dados.get('quantidade', CarrosCarrinho.quantidade)
        preco_unitario = dados.get('preco_unitario',CarrosCarrinho.preco_unitario)
     

        carrocarrinho.modelo = modelo
        carrocarrinho.marca = marca
        carrocarrinho.quantidade = quantidade
        carrocarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return carrocarrinho.json(),200
    

    def delete(self,id):
        carrocarrinho = CarrosCarrinho.query.get_or_404(id)
        db.session.delete (carrocarrinho)
        db.session.commit ()
        return {"code_status":"deletado"},200

