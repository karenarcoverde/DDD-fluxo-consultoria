from flask.views import MethodView
from flask import request, jsonify, render_template
from app.extensions import db
from app.usuario.model import Usuario
from flask_mail import Message
from app.extensions import mail, jwt
from flask_jwt_extended import create_access_token, jwt_required 
import bcrypt

class UsuarioDetalhes(MethodView): 
    def get(self):
        usuarios = Usuario.query.all()
        return jsonify([usuario.json() for usuario in usuarios]),200

    def post(self):
        dados = request.json        
        nome = dados.get('nome')
        cpf = dados.get('cpf')
        email = dados.get('email')
        telefone = dados.get('telefone')
        endereco = dados.get('endereco')
        senha = dados.get('senha')

        if Usuario.query.filter_by(cpf = cpf).first():
            return{"error":"CPF já cadastrado"}
        if Usuario.query.filter_by(email = email).first():
            return{"error":"E-mail já cadastrado"}  

        if isinstance (nome,str) and isinstance (cpf,str) and isinstance (telefone,str) and isinstance (endereco,str):
            senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
            usuario = Usuario(nome = nome, cpf = cpf, email = email, telefone = telefone, endereco = endereco, senha_hash=senha_hash)
            db.session.add(usuario)
            db.session.commit()

            msg = Message (
                sender = 'karenarcoverde@poli.ufrj.br',
                recipients = [email],
                subject = 'Bem-vindo!',
                html = render_template('email.html', nome=nome)
            )

            mail.send(msg)

            return usuario.json(),200

        return {"code_status":"invalid data in request"},400

class UsuarioId(MethodView): #/usuarios/<int:id>
    decorators = [jwt_required()]
    def get (self,id):
        usuario = Usuario.query.get_or_404(id)
        return usuario.json()

    def put (self,id):
        dados = request.json
        nome = dados.get('nome')
        cpf = dados.get('cpf')
        email = dados.get('email')
        telefone = dados.get('telefone')
        endereco = dados.get('endereco')

        usuario = Usuario.query.get_or_404(id)
        usuario.nome = nome
        usuario.cpf = cpf
        usuario.email = email
        usuario.telefone = telefone
        usuario.endereco = endereco
        db.session.commit()
        return usuario.json(),200
      

    def patch (self,id):
        dados = request.json
        usuario = Usuario.query.get_or_404 (id)
  
        nome = dados.get('nome',Usuario.nome)
        cpf = dados.get('cpf', Usuario.cpf)
        email = dados.get('email',Usuario.email)
        telefone = dados.get('telefone',Usuario.telefone)
        endereco = dados.get('endereco',Usuario.endereco)

        usuario.nome = nome
        usuario.cpf = cpf
        usuario.email = email
        usuario.telefone = telefone
        usuario.endereco = endereco
        db.session.commit()
        return usuario.json(),200
    

    def delete(self,id):
        usuario = Usuario.query.get_or_404(id)
        db.session.delete (usuario)
        db.session.commit ()
        return {"code_status":"deletado"},200

class UsuarioLogin(MethodView):  #/login
    def post(self):
        dados = request.json        
       
        email = dados.get('email')
        senha = dados.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario or not bcrypt.hashpw(senha.encode(), bcrypt.gensalt()):
            return {'error': 'Usuário ou senha inválidos'}

        token = create_access_token(identity=usuario.id)

        return {"token": token},200