from flask import Flask
from app.config import Config
from app.extensions import db, migrate, mail, jwt

# models
from app.usuario.model import Usuario
from app.motos.model import Motos
from app.carrinho.model import Carrinho
from app.carrosCarrinho.model import CarrosCarrinho
from app.cupons.model import Cupons
from app.carros.model import Carros
from app.motosCarrinho.model import MotosCarrinho

# routes
from app.usuario.routes import usuario_api
from app.carrinho.routes import carrinho_api
from app.cupons.routes import cupons_api
from app.carros.routes import carros_api
from app.motos.routes import motos_api
from app.carrosCarrinho.routes import carroscarrinho_api
from app.motosCarrinho.routes import motoscarrinho_api

# cria o app
def create_app():
    # instanciacao do aplicativo
    app = Flask(__name__)

    # configuracao do app
    app.config.from_object(Config)

    # inicializacao da database
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    jwt.init_app(app)

    # rotas implementadas
    app.register_blueprint(usuario_api)
    app.register_blueprint(carrinho_api)
    app.register_blueprint(cupons_api)
    app.register_blueprint(carros_api)
    app.register_blueprint(motos_api)
    app.register_blueprint(carroscarrinho_api)
    app.register_blueprint(motoscarrinho_api)

    return app