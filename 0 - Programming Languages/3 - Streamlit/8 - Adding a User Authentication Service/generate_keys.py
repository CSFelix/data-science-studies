import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ['Peter Parker', 'Rebecca Miller']
usernames = ['pparker', 'rmiller']
# passwords = ['abc123', 'def456']
passwords = ['XXX', 'XXX'] # after hasing the passwords, replace them by XXX for security

# hashing passwords with bcrypt
hashed_passwords = stauth.Hasher(passwords).generate()

# storing the hased passwords
file_path = Path(__file__).parent / 'hashed_pw.pkl'

with file_path.open('wb') as file:
	pickle.dump(hashed_passwords, file)