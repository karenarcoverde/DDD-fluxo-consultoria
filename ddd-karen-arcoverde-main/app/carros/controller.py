from flask.views import MethodView
from flask import request, jsonify
from app.extensions import db
from app.carros.model import Carros

class CarrosDetalhes(MethodView): 
    def get(self):
        carros = Carros.query.all()
        return jsonify([carro.json() for carro in carros]),200

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
            carro = Carros(cor= cor, descricao = descricao, modelo = modelo, marca = marca, ano_fabricacao = ano_fabricacao, motor = motor, estoque = estoque, preco = preco, nacional = nacional, importada = importada)
            db.session.add(carro)
            db.session.commit()
            return carro.json(),200
        return {"code_status":"invalid data in request"},400

class CarrosId(MethodView):
    def get (self,id):
        carro = Carros.query.get_or_404(id)
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


        carro = Carros.query.get_or_404(id)
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
        carro = Carros.query.get_or_404 (id)
  
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

        carro = Carros.query.get_or_404(id)
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
    

    def delete(self,id):
        carro = Carros.query.get_or_404(id)
        db.session.delete (carro)
        db.session.commit ()
        return {"code_status":"deletado"},200

