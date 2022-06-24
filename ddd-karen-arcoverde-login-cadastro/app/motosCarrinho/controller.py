from flask.views import MethodView
from flask import request, jsonify, abort,make_response
from app.extensions import db
from app.motosCarrinho.model import MotosCarrinho
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from sqlalchemy import exc
from app.motosCarrinho.schema import MotosCarrinhoSchema

class MotosCarrinhoDetalhes(MethodView): 
    def get(self):
        schema = MotosCarrinhoSchema(many = True)
        return jsonify(schema.dump(MotosCarrinho.query.all())),200

    def post(self):
        dados = request.json      
        schema = MotosCarrinhoSchema()  
        quantidade = dados["quantidade"]
        preco_unitario = dados["preco_unitario"]
        preco_total = quantidade * preco_unitario
        dados["preco_total"] = preco_total

        motoscarrinho = schema.load(dados)

        db.session.add(motoscarrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        
        return schema.dump(motoscarrinho),200

class MotosCarrinhoId(MethodView):
    def get(self, id):
        schema = MotosCarrinhoSchema(many = True)
        
        motos = MotosCarrinho.query.get_or_404(id)
        return schema.dump(motos),200

    def put(self, id):
        motoscarrinho = MotosCarrinho.query.get_or_404(id)
        schema = MotosCarrinhoSchema()
        motoscarrinho = schema.load(request.json,instance=motoscarrinho)

        db.session.add(motoscarrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(motoscarrinho),200

    def patch(self, id):
        motoscarrinho = MotosCarrinho.query.get_or_404(id)
        schema = MotosCarrinhoSchema()
        motoscarrinho = schema.load(request.json, instance=motoscarrinho, partial = True)

        db.session.add(motoscarrinho)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(motoscarrinho),200

    def delete(self, id):
        motoscarrinho = MotosCarrinho.query.get_or_404(id)
        db.session.delete(motoscarrinho)
        db.session.commit()
        return {}, 200

