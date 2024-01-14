# gitignore.io
import os
from deta import Deta # pip install deta
from dotenv import load_dotenv # pip install python-dotenv

# Load the environment variables
load_dotenv('.env')
DETA_KEY = os.getenv('DETA_KEY')

# Initialize with a project key
deta = Deta(DETA_KEY)

# Connecting to the database
db = deta.Base('users_db')

# Function to inser a user
def insert_user(username, name, password):
	"""Returns the use on a successful user creation, otherwise raises an error"""
	return db.put({
		'key': username
		, 'name': name
		, 'password': password
	})
# adding two defualt users (just run this two lines bellow once)
# insert_user('pparker', 'Peter Parker', 'abc123')
# insert_user('rmiller', 'Rebecca Miller', 'def456')

def fetch_all_users():
	"""Returns a dict of all users"""
	res = db.fetch()
	return res.items # count, last, items

# print(fetch_all_users())

def get_user(username):
	"""If not found, the function will return None"""
	return db.get(username)

# print(get_user('pparker'))

def update_user(username, updates):
	"""If the item is updated, returns None. Otherwise, an exception is raised"""
	return db.update(updates, username)

# update_user('pparker', { 'name': 'Spider-Man' })

def delete_user(username):
	"""Always returns None, even if the does not exist"""
	return db.delete(username)

# delete_user('pparker')
# delete_user('rmiller')