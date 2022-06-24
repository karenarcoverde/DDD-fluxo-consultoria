from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.motos.model import Motos

class MotosDetalhes(MethodView): 
    def get(self):
        motos = Motos.query.all()
        return jsonify([moto.json() for moto in motos]),200

    def post(self):
        dados = request.json        
        cor = dados.get('cor')
        descricao = dados.get('descricao')
        modelo = dados.get('modelo')
        marca = dados.get('marca')
        ano_fabricacao = dados.get('ano_fabricacao')
        motor = dados.get('motor')
        estoque = dados.get('estoque')
        preco = preco.get('preco')
        nacional = nacional.get('nacional')
        importada = importada.get ('importada')


        if isinstance (cor,str) and isinstance (descricao,str) and isinstance (modelo,str) and isinstance (marca,str) and isinstance (ano_fabricacao,int) and isinstance (motor,str) and isinstance (estoque,int) and isinstance (preco,int) and isinstance (nacional,bool) and isinstance (importada,bool):
            moto = Motos(cor= cor, descricao = descricao, modelo = modelo, marca = marca, ano_fabricacao = ano_fabricacao, motor = motor, estoque = estoque, preco = preco, nacional = nacional, importada = importada)
            db.session.add(moto)
            db.session.commit()
            return moto.json(),200
        return {"code_status":"invalid data in request"},400

class MotosId(MethodView):
    def get (self,id):
        carro = Motos.query.get_or_404(id)
        return carro.json()

    def put (self,id):
        dados = request.json
        cor = dados.get('cor')
        descricao = dados.get('descricao')
        modelo = dados.get('modelo')
        marca = dados.get('marca')
        ano_fabricacao = dados.get('ano_fabricacao')
        motor = dados.get('motor')
        estoque = dados.get('estoque')
        preco = preco.get('preco')
        nacional = nacional.get('nacional')
        importada = importada.get ('importada')


        carro = Motos.query.get_or_404(id)
        carro.cor = cor
        carro.descricao = descricao
        carro.modelo = modelo
        carro.marca = marca
        carro.ano_fabricacao = ano_fabricacao
        carro.motor = motor
        carro.estoque = estoque
        carro.preco = preco
        nacional = nacional.get ('nacional')
        importada = importada.get ('importada')
        db.session.commit()
        return carro.json(),200
      

    def patch (self,id):
        dados = request.json
        moto = Motos.query.get_or_404 (id)
  
        cor = dados.get('cor')
        descricao = dados.get('descricao')
        modelo = dados.get('modelo')
        marca = dados.get('marca')
        ano_fabricacao = dados.get('ano_fabricacao')
        motor = dados.get('motor')
        estoque = dados.get('estoque')
        preco = preco.get('preco')
        nacional = nacional.get('nacional')
        importada = importada.get ('importada')

        moto = Motos.query.get_or_404(id)
        moto.cor = cor
        moto.descricao = descricao
        moto.modelo = modelo
        moto.marca = marca
        moto.ano_fabricacao = ano_fabricacao
        moto.motor = motor
        moto.estoque = estoque
        moto.preco = preco
        nacional = nacional.get ('nacional')
        importada = importada.get ('importada')
        db.session.commit()
        return moto.json(),200
    

    def delete(self,id):
        carro = Motos.query.get_or_404(id)
        db.session.delete (carro)
        db.session.commit ()
        return {"code_status":"deletado"},200

