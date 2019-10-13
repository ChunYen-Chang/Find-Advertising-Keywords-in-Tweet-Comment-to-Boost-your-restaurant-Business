# import packages
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.apps import custom_app_context as pwd_context
from model import BaseModel, Tweet, User


# connect to Mysql database
engine = create_engine("mysql+mysqlconnector://<MySql_account>:<MySql_password>@<MySql_IP>:<MySql_port>/<MySql_db>")
DBSession = sessionmaker(bind=engine)
session = DBSession()


# declare a auth instance and Flask instance
auth = HTTPBasicAuth()
app = Flask(__name__)


@auth.verify_password
def verify_password(username, password):
	'''
	Description: This function allow flask server to check the username and userpassword 
				If the username does not exist in the Mysql database or the userpassword
				is not correct, the flask server won't allow this user to extract information.
				
	Parameters: -username: the username a user gives
				-password: the password a user gives
	
	Returns: -True: The username can be found in the Mysql database and the password is correct
			 -False: The username cannot be found in the Mysql database and the password isn't correct
	'''
	# extract a user's information based on the "username" that a user gives
	user = session.query(User).filter_by(account = username).first()
	
	# if username cannot be found in the database, return False
	if not user:
		return False

	# save this user's username and hashed password from in account and hash_passowrd variable
	account = user.account
	hash_passowrd = user.password
	
	# if userpassword is not correct, return False
	if not pwd_context.verify(password, hash_passowrd):
		return False

	return True


@app.route('/user', methods = ['POST'])
def user_register():
	'''
	Description: This function allow users to register their account in Mysql database
				
	Parameters: None
	
	Returns: None
	'''
	# extract username and userpassword information from request.form
	user_name = request.form['username']
	user_password= request.form['userpassword']
	
	# use pwd_context.hash function to convert password into hashed_password 
	user_password_hash = pwd_context.hash(user_password)
	
	# connect to Mysql and check whether this user_name exists or not.
	user = session.query(User).filter_by(account = user_name).first()
	if user:
		return 'The user exists'

	# save this new username and userpassword into the Mysql database
	new_user = User(account=user_name,
			password=user_password_hash)
	session.add(new_user)
	session.commit()

	return 'Already registered a new user'


@app.route('/RestaurantTweetInf', methods = ['GET'])
@auth.login_required
def get_tweet_inf():
	'''
	Description: This function allow users to get all Tweet text information
				
	Parameters: None
	
	Returns: None
	
	Note: This function is protected by auth.login_required, users need to pass the verification in the
			beginning
	'''
	if request.method == 'GET':
        all_tweet = session.query(Tweet).all()
        all_tweet_dict = {}
        for i in all_tweet:
                all_tweet_dict[i.tweet_id] = {'tweet_user':i.tweet_user, \
												'tweet_text':i.tweet_text, \
												'tweet_text_time':i.tweet_text_time, \
												'tweet_text_polarity':i.tweet_text_polarity, \
												'tweet_text_subjectivity':i.tweet_text_subjectivity}
        return jsonify(all_tweet_dict)


if __name__ == '__main__':
	app.run(host="0.0.0.0", port=80)
