import os


class BaseConfig:
    SECRET_KEY = 'very secret key'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    mysql_pwd = os.environ.get('MYSQL_PWD') or ''
    uri = 'mysql://root:{}@localhost:3306/jobplus?charset=utf8'
    SQLALCHEMY_DATABASE_URI = uri.format(mysql_pwd)
    print('=======================================================')
    print('SQLALCHEMY_DATABASE_URI:', SQLALCHEMY_DATABASE_URI)
    print('=======================================================')


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
