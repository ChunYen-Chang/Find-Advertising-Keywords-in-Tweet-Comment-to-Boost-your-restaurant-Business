# import packages
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import *


# declare the basemodel
BaseModel = declarative_base()


# define the User and Tweet class
class User(BaseModel):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    account = Column(String(512))    
    password = Column(String(20))


class Tweet(BaseModel):
    __tablename__ = 'Tweet'
    tweet_id = Column(Integer, autoincrement=True, primary_key=True)
    tweet_user = Column(String(512))
    tweet_text = Column(String(512))
    tweet_text_time = Column(String(512))
	tweet_text_polarity = Column(String(512))
	tweet_text_subjectivity = Column(String(512))


if __name__ == '__main__': 
	# create user and Restaurant table in Mysql database    
	engine = create_engine("mysql+mysqlconnector://<MySql_account>:<MySql_password>@<MySql_IP>:<MySql_port>/<MySql_db>")
	BaseModel.metadata.create_all(engine)
    
