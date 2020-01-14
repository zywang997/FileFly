import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'H7XyGqdqghcoCH7T4cf!'     # Flask Session 需要使用密钥
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    WTF_CSRF_SECRET_KEY = 'H7XyGqdqghcoCH7T4cf!'    # Flask-WTF的CSRF保护需要使用密钥
    WTF_CSRF_CHECK_DEFAULT = True
	# 最大上传限制，默认1024M
    MAX_CONTENT_LENGTH = 1024 * 1024 * 128
	# Cookie 过期时间
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    FONT=basedir+'/app/static/font/Arial.ttf'
	# HDFS回收站文件路径
    HDFS_TRASH = '/user/username/.Trash/Current/'
	# HDFS namenode
    #HDFS_IP = "http://127.0.0.1:50070"
    HDFS_IP = "http://114.116.5.3:9870"
    SESSION_COOKIE_HTTPONLY=True

    @staticmethod
    def init__app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    BASE_HOST='http://0.0.0.0:8082/'
    SHARE_BASE_HOST='http://114.115.167.187:8082/'
    #BASE_HOST='http://127.0.0.1:5000/'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'web_db.sqlite')



class TestingConfig(Config):
    pass


class Production(Config):
    DEBUG = False
    BASE_HOST='http://0.0.0.0:8082/'
    SHARE_BASE_HOST='http://114.115.167.187:8082/'
    #BASE_HOST = 'http://127.0.0.1:5000/'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'web_db.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': Production,
    'default': DevelopmentConfig
}
