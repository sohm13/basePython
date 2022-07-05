from os import getenv

SQLALCHEMY_DATABASE_URI = getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://user:passw@localhost:5432/postgres",
)



class Config:
    DEBUG = False
    TESTING = False
    ENV = "development"

    SECRET_KEY = "qwsgdfgertytrewsupersecret"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    # DATABASE_URI = 'mysql://user@localhost/foo'
    pass

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True