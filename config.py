import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = 'smtp.qq.com'
    #MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'mei0fei@qq.com'
    #MAIL_USERNAME = 'mei9fei@gmail.com'
    MAIL_DEFAULT_SENDER = 'mei0fei@qq.com'
    #MAIL_DEFAULT_SENDER = 'mei9fei@gmail.com'
    MAIL_PASSWORD = 'xxxx'
    MAIL_USE_TLS = 0

    ADMINS = ['mei0fei@qq.com']

    POSTS_PER_PAGE = 2
