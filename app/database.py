from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Init engine and db_session
#engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'], convert_unicode=True)
#db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

#Base = declarative_base()
#Base.query = db_session.query_property()
db = SQLAlchemy()
