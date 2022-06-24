from flask.views import MethodView
from flask import request, jsonify, abort,make_response
from app.extensions import db
from app.carros.model import Carros
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from sqlalchemy import exc
from app.carros.schema import CarrosSchema

class CarrosDetalhes(MethodView): 
    def get(self):
        schema = CarrosSchema(many = True)
        return jsonify(schema.dump(Carros.query.all())),200

    def post(self):
        dados = request.json      
        schema = CarrosSchema()  
        carros = schema.load(dados)

        db.session.add(carros)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        
        return schema.dump(carros),200

class CarrosId(MethodView):
    def get(self, id):
        schema = CarrosSchema(many = True)
        
        carros = Carros.query.get_or_404(id)
        return schema.dump(carros),200

    def put(self, id):
        carros = Carros.query.get_or_404(id)
        schema = CarrosSchema()
        carros = schema.load(request.json,instance=carros)

        db.session.add(carros)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(carros),200

    def patch(self, id):
        carros = Carros.query.get_or_404(id)
        schema = CarrosSchema()
        carros = schema.load(request.json, instance=carros, partial = True)

        db.session.add(carros)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(carros),200

    def delete(self, id):
        carros= Carros.query.get_or_404(id)
        db.session.delete(carros)
        db.session.commit()
        return {}, 200
