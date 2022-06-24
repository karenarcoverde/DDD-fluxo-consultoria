from flask.views import MethodView
from flask import request, jsonify, abort,make_response
from app.extensions import db
from app.carrosCarrinho.model import CarrosCarrinho
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from sqlalchemy import exc
from app.carrosCarrinho.schema import CarrosCarrinhoSchema

class CarrosCarrinhoDetalhes(MethodView): 
    def get(self):
        schema = CarrosCarrinhoSchema(many = True)
        return jsonify(schema.dump(CarrosCarrinho.query.all())),200

    def post(self):
        dados = request.json        
    
        schema = CarrosCarrinhoSchema()    
        quantidade = dados["quantidade"]
        preco_unitario = dados["preco_unitario"]
        preco_total = quantidade * preco_unitario
        dados["preco_total"] = preco_total

        carroscarrinho = schema.load(dados)

        db.session.add(carroscarrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        
        return schema.dump(carroscarrinho),200

class CarrosCarrinhoId(MethodView):
    def get(self, id):
        schema = CarrosCarrinhoSchema(many = True)
        
        carros = CarrosCarrinho.query.get_or_404(id)
        return schema.dump(carros),200

    def put(self, id):
        carroscarrinho = CarrosCarrinho.query.get_or_404(id)
        schema = CarrosCarrinhoSchema()
        carroscarrinho = schema.load(request.json,instance=carroscarrinho)

        db.session.add(carroscarrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(carroscarrinho),200

    def patch(self, id):
        carroscarrinho = CarrosCarrinho.query.get_or_404(id)
        schema = CarrosCarrinhoSchema()
        carroscarrinho = schema.load(request.json, instance=carroscarrinho, partial = True)

        db.session.add(carroscarrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(carroscarrinho),200

    def delete(self, id):
        carroscarrinho = CarrosCarrinho.query.get_or_404(id)
        db.session.delete(carroscarrinho)
        db.session.commit()
        return {}, 200
