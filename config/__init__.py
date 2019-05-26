import os


class Base:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    DB_USER = os.getenv('RDS_USERNAME', 'postgres')
    DB_PWD = os.getenv('RDS_PASSWORD', 'root')
    DB_HOST = os.getenv('RDS_HOST', 'localhost') + ':' + os.getenv('RDS_PORT', '5432')
    DB_NAME = os.getenv('RDS_DB_NAME', 'postgres')
    DB_SCHEMA_NAME = os.getenv('DB_SCHEMA_NAME', 'config')

    SQLALCHEMY_DATABASE_URI = 'postgres://' + DB_USER + ':' + DB_PWD \
                              + '@' + DB_HOST + '/' + DB_NAME

    SQLALCHEMY_TRACK_MODIFICATIONS = False