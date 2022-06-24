from flask.views import MethodView
from flask import request, jsonify, abort,make_response
from app.extensions import db
from app.usuario.model import Usuario
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import bcrypt
from sqlalchemy import exc
from app.usuario.schema import UsuarioSchema, LoginSchema
from app.utils.filters import filter

class UsuarioDetalhes(MethodView): 
    def get(self):
        schema = UsuarioSchema(many = True)
        return jsonify(schema.dump(Usuario.query.all())),200

    def post(self):
        dados = request.json    
        schema = UsuarioSchema() 
        usuario = schema.load(dados)
        db.session.add(usuario)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        
        return schema.dump(usuario),200
     
class UsuarioId(MethodView): #/usuarios/<int:id>
    decorators = [jwt_required()]
    def get(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400       

        schema = filter.getSchema(
            qs=request.args,schema_cls=UsuarioSchema)
        
        usuario = Usuario.query.get_or_404(id)
        return schema.dump(usuario),200

    def put(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400

        usuario = Usuario.query.get_or_404(id)
        schema = UsuarioSchema()
        usuario = schema.load(request.json,instance=usuario)

        db.session.add(usuario)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(usuario),200

    def patch(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        usuario = Usuario.query.get_or_404(id)
        schema = UsuarioSchema()
        usuario = schema.load(request.json, instance=usuario, partial = True)

        db.session.add(usuario)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        return schema.dump(usuario),200



    def delete(self, id):
        if (get_jwt_identity() != id):
            return {'error':'Usuario não permitido'}, 400
        usuario= Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return {}, 200

class UsuarioLogin(MethodView):  #/login
    def post(self):
        schema = LoginSchema()
        dados = schema.load(request.json)
        usuario = Usuario.query.filter_by(email=dados['email']).first()

        if (not usuario) or not usuario.verify_senha(dados['senha']):
            return {'error':'Email ou senha inválida'}, 400
        
        token = create_access_token(identity=usuario.id)

        return {"token": token},200