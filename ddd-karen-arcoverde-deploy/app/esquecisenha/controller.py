from flask import request,render_template, jsonify, abort, make_response
from flask.views import MethodView
from flask_jwt_extended import create_access_token,create_refresh_token
from flask_jwt_extended.utils import decode_token
from flask_mail import Message
from app.extensions import mail, db
from app.models import BaseModel
from app.esquecisenha.schema import EmailSchema,SenhaSchema
from app.usuario.model import Usuario
from sqlalchemy import exc


class SenhaMail(MethodView):#/send_mail/reset
    def post(self):
        schema = EmailSchema()
        dados = schema.load(request.json)
        usuario = Usuario.query.filter_by(email=dados['email']).first()
        if usuario:
            token = create_access_token(identity=usuario.id,additional_claims={'user_type' : "usuario"})
            refresh_token = create_refresh_token(identity=usuario.id, additional_claims={'user_type': "usuario"})
    
        else:
            return {"Error":"Esse email não está cadastrado cadastrado"}, 400
        msg = Message(sender = 'karenarcoverde@poli.ufrj.br',
        recipients=[usuario.email],
        subject = 'Mudança de senha',
        html = render_template('recupera.html', nome = usuario.nome, link=token))
        mail.send(msg)
        return {"Resultado":"envio feito"},200

class SenhaNova(MethodView): #/reset/<token>
    def patch(self,token):
        schema = SenhaSchema()
        dados = schema.load(request.json)

        token = decode_token(token)
        
        if token['user_type']=="usuario":
            usuario = Usuario.query.filter_by(id = token["sub"]).first()
        
        if not usuario: return {"Error":"Token Inválido ou expirado"},404
        usuario.senha = dados["senha"]
        db.session.add(usuario)
        try:
            db.session.commit()
        except exc.IntegrityError as err:
            db.session.rollback()
            abort(
                make_response(jsonify({'errors':str(err.orig)},400)))
        msg = Message(sender = 'karenarcoverde@poli.ufrj.br',
        recipients=[usuario.email],
        subject = 'Senha Alterada',
        html = render_template('altera.html', nome = usuario.nome))
        mail.send(msg)
        mail.send(msg)
        return {},200