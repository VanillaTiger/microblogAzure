import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://azure:6#vWHD_$@127.0.0.1:56080/localdb"
    #Database=localdb;Data Source=127.0.0.1:56080;User Id=azure;Password=6#vWHD_$

    #SQLALCHEMY_DATABASE_URI = os.environ.get('blalbals') or\
                              #'sqlite:///' +  os.path.join(basedir, 'app.db')

    print('ADAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA= '+basedir)
    #'sqlite:///' + os.path.join(basedir, 'app.db')

    #SQLALCHEMY_DATABASE_URI = "jdbc:sqlserver://microblogazuresql.database.windows.net:1433;database=myDB;user=adam@microblogazuresql;password={your_password_here};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
    POSTS_PER_PAGE = 25
