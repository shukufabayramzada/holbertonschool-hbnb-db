import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    USE_DATABASE = os.getenv('USE_DATABASE', 'True').lower() == 'true'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///development.db')

class ProductionConfig(Config):
    DEBUG = False
    USE_DATABASE = os.getenv('USE_DATABASE', 'True').lower() == 'true'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')

def get_config():
    env = os.getenv('ENV', 'development')
    if env == 'development':
        return DevelopmentConfig
    elif env == 'production':
        return ProductionConfig
    else:
        return Config
