from flask.views import MethodView
from flask import request, jsonify, abort,make_response
from app.extensions import db
from app.carrinho.model import Carrinho
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from sqlalchemy import exc
from app.carrinho.schema import CarrinhoSchema

class CarrinhoDetalhes(MethodView): 
    def get(self):
        schema = CarrinhoSchema(many = True)
        return jsonify(schema.dump(Carrinho.query.all())),200

    def post(self):
        dados = request.json      
        schema = CarrinhoSchema()  

        carrinho = schema.load(dados)

        db.session.add(carrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
    
        return schema.dump(carrinho),200

class CarrinhoId(MethodView):
    def get(self, id):
        schema = CarrinhoSchema(many = True)
        
        carrinho = Carrinho.query.get_or_404(id)
        return schema.dump(carrinho),200

    def put(self, id):
        carrinho = Carrinho.query.get_or_404(id)
        schema = CarrinhoSchema()
        carrinho = schema.load(request.json,instance=carrinho)

        db.session.add(carrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(carrinho),200

    def patch(self, id):
        carrinho = Carrinho.query.get_or_404(id)
        schema = CarrinhoSchema()
        carrinho = schema.load(request.json, instance=carrinho, partial = True)

        db.session.add(carrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(carrinho),200

    def delete(self, id):
        carrinho= Carrinho.query.get_or_404(id)
        db.session.delete(carrinho)
        db.session.commit()
        return {}, 200
