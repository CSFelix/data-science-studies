import os

from deta import Deta # pip install deta
from dotenv import load_dotenv # pip install python-dotenv

# ---- LOADING ENV ----
load_dotenv('.env')
DETA_KEY = os.getenv('DETA_KEY')

# ---- CONNECTION ----
deta = Deta(DETA_KEY)
db = deta.Base('monthly_reports')

# ---- FUNCTIONS ----
def insert_period(period, incomes, expenses, comment):
	"""Returns the report on a successful creation, otherwise raises an error"""
	return db.put({'key': period, 'incomes': incomes, 'expenses': expenses, 'comment': comment})

def fetch_all_periods():
	"""Returns a dict of all periods"""
	res = db.fetch()
	return res.items

def get_period(period):
	"""If not found, the function will return None"""
	return db.get(period)