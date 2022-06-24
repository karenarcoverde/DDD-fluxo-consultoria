from os import environ

#Configuracoes gerais, o SQLALCHEMY_DATABASE_URI  é trocado ao reiniciar o banco de dados
class Config:

    # DATABASE - configuracao da database (modo web-dev)
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    #SQLALCHEMY_DATABASE_URI = 'postgresql://sryfuothqoncnv:76144c9960f62577452899ddbd425fc015286148846e3b0ec06b1075a1f77ef4@ec2-3-222-204-187.compute-1.amazonaws.com:5432/dde5jjmk6js05n'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application - configuracao da comunicacao com o front-end
    SECRET_KEY = environ.get('SECRET_KEY')
    JSON_SORT_KEYS = False
    DEBUG = True

    ## MAIL ## 
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = environ.get('MAIL_PORT')
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_USE_TLS = True
    MAIL_USE_SSH = False
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')

    ### JWT EXTENDED ##
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')

    