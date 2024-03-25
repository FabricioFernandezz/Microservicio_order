from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from .env import USER_DB, PASS_DB, URL_DB, NAME_DB

db = SQLAlchemy()
migrate= Migrate()

# FULL_URL_DB=f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}"