from flask import Flask
from app.config import Config
from app.extensions import db, migrate,jwt,ma

# routes
from app.usuario.routes import usuario_api
from app.carrinho.routes import carrinho_api
from app.cupons.routes import cupons_api
from app.carros.routes import carros_api
from app.motos.routes import motos_api
from app.carrosCarrinho.routes import carroscarrinho_api
from app.motosCarrinho.routes import motoscarrinho_api

from app.storages.routes import storage_api

from app.esquecisenha.routes import esquecisenha_api
from app.extensions import mail as mail


# cria o app
def create_app():
    # instanciacao do aplicativo
    app = Flask(__name__)

    # configuracao do app
    app.config.from_object(Config)

    # inicializacao da database
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    # rotas implementadas
    app.register_blueprint(usuario_api)
    app.register_blueprint(carrinho_api)
    app.register_blueprint(cupons_api)
    app.register_blueprint(carros_api)
    app.register_blueprint(motos_api)
    app.register_blueprint(carroscarrinho_api)
    app.register_blueprint(motoscarrinho_api)
    app.register_blueprint(storage_api)
    app.register_blueprint(esquecisenha_api)

    return app