from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.motosCarrinho.model import MotosCarrinho

class MotosCarrinhoDetalhes(MethodView): 
    def get(self):
        motoscarrinho = MotosCarrinho.query.all()
        return jsonify([motocarrinho.json() for motocarrinho in motoscarrinho]),200

    def post(self):
        dados = request.json        
        modelo = dados.get('modelo')
        marca = dados.get('marca')
        quantidade = dados.get('quantidade')
        preco_unitario = dados.get('preco_unitario')
       
        preco_total = quantidade * preco_unitario
       
        if isinstance (modelo,str) and isinstance (marca,str) and isinstance (quantidade,int) and isinstance (preco_unitario,int) and isinstance (preco_total,int):
            motocarrinho = MotosCarrinho(modelo= modelo, marca = marca, quantidade = quantidade, preco_unitario = preco_unitario, preco_total = preco_total)
            db.session.add(motocarrinho)
            db.session.commit()
            return motocarrinho.json(),200
        return {"code_status":"invalid data in request"},400

class MotosCarrinhoId(MethodView):
    def get (self,id):
        motocarrinho = MotosCarrinho.query.get_or_404(id)
        return motocarrinho.json()

    def put (self,id):
        dados = request.json
        modelo = dados.get('modelo')
        marca = dados.get('marca')
        quantidade = dados.get('quantidade')
        preco_unitario = dados.get('preco_unitario')

        motocarrinho = MotosCarrinho.query.get_or_404(id)
        motocarrinho.modelo = modelo
        motocarrinho.marca = marca

        motocarrinho.quantidade = quantidade
        motocarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return motocarrinho.json(),200
      

    def patch (self,id):
        dados = request.json
        motocarrinho= MotosCarrinho.query.get_or_404 (id)
  
        modelo= dados.get('modelo',MotosCarrinho.modelo)
        marca= dados.get('marca',MotosCarrinho.marca)
        quantidade = dados.get('quantidade', MotosCarrinho.quantidade)
        preco_unitario = dados.get('preco_unitario',MotosCarrinho.preco_unitario)
     

        motocarrinho.modelo = modelo
        motocarrinho.marca = marca
        motocarrinho.quantidade = quantidade
        motocarrinho.preco_unitario = preco_unitario
        db.session.commit()
        return motocarrinho.json(),200
    

    def delete(self,id):
        motocarrinho = MotosCarrinho.query.get_or_404(id)
        db.session.delete (motocarrinho)
        db.session.commit ()
        return {"code_status":"deletado"},200

