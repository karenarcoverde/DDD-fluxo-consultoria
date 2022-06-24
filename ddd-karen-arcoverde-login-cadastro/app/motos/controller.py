from flask.views import MethodView
from flask import request, jsonify, abort,make_response
from app.extensions import db
from app.motos.model import Motos
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from sqlalchemy import exc
from app.motos.schema import MotosSchema

class MotosDetalhes(MethodView): 
    def get(self):
        schema = MotosSchema(many = True)
        return jsonify(schema.dump(Motos.query.all())),200

    def post(self):
        dados = request.json      
        schema = MotosSchema()  
        motos = schema.load(dados)

        db.session.add(motos)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))

        return schema.dump(motos),200

class MotosId(MethodView):
    def get(self, id):
        schema = MotosSchema(many = True)
        
        motos = Motos.query.get_or_404(id)
        return schema.dump(motos),200

    def put(self, id):
        motos = Motos.query.get_or_404(id)
        schema = MotosSchema()
        motos = schema.load(request.json,instance=motos)

        db.session.add(motos)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(motos),200

    def patch(self, id):
        motos = Motos.query.get_or_404(id)
        schema = MotosSchema()
        motos = schema.load(request.json, instance=Motos, partial = True)

        db.session.add(motos)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(motos),200

    def delete(self, id):
        motos= Motos.query.get_or_404(id)
        db.session.delete(motos)
        db.session.commit()
        return {}, 200
