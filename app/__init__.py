from flask import Flask
from flask_cors import CORS
from app.config.database import db, migrate, FULL_URL_DB
from app.models import *
from flask_marshmallow import Marshmallow
from flask_caching import Cache

ma = Marshmallow()
cache = Cache()

def create_app():
    app=Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.debug = True
    
    ma.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app, config={'CACHE_TYPE': 'RedisCache', 'CACHE_DEFAULT_TIMEOUT': 300, 
                   'CACHE_REDIS_HOST': 'redis', 'CACHE_REDIS_PORT': 6379, 'CACHE_REDIS_DB': '0', 'CACHE_REDIS_PASSWORD': '9697', 'CACHE_KEY_PREFIX': 'order_'})
    
    from app.resources import order
    app.register_blueprint(order, url_prefix="/api/v1")

    return app