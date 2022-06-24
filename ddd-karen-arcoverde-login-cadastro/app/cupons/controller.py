from flask.views import MethodView
from flask import request, jsonify, abort,make_response
from app.extensions import db
from app.cupons.model import Cupons
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from sqlalchemy import exc
from app.cupons.schema import CuponsSchema

class CuponsDetalhes(MethodView): 
    def get(self):
        schema = CuponsSchema(many = True)
        return jsonify(schema.dump(Cupons.query.all())),200

    def post(self):
        dados = request.json      
        schema = CuponsSchema()  
        cupons = schema.load(dados)

        db.session.add(cupons)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))   

        return schema.dump(cupons),200

class CuponsId(MethodView):
    def get(self, id):
        schema = CuponsSchema(many = True)
        
        cupons = Cupons.query.get_or_404(id)
        return schema.dump(cupons),200

    def put(self, id):
        cupons = Cupons.query.get_or_404(id)
        schema = CuponsSchema()
        cupons = schema.load(request.json,instance=cupons)

        db.session.add(cupons)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(cupons),200

    def patch(self, id):
        cupons = Cupons.query.get_or_404(id)
        schema = CuponsSchema()
        cupons = schema.load(request.json, instance=cupons, partial = True)

        db.session.add(cupons)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(cupons),200

    def delete(self, id):
        cupons = Cupons.query.get_or_404(id)
        db.session.delete(cupons)
        db.session.commit()
        return {}, 200

