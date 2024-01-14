import pickle
from pathlib import Path
import streamlit_authenticator as stauth # pip install streamlit-authenticator
import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title='Authenticator'
    , page_icon=':lock:'
    , layout='wide'
)

# ---- USER AUTHENTICATION ----


# loading hashed passwords
file_path = Path(__file__).parent / 'hashed_pw.pkl'

with file_path.open('rb') as file:
    hashed_passwords = pickle.load(file)

credentials = {
    "usernames":{
        "pparker":{ "name":"Peter Parker", "password": hashed_passwords[0] }
        , "rmiller":{ "name":"Rebecca Miller", "password": hashed_passwords[1] }            
    }
}

authenticator = stauth.Authenticate(
    credentials
    , 'authenticate_service' # cookie file name in the browser
    , 'abcdef' # key to encode the cookies
    , cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status == False:
    st.error('Username/Password is incorrect')
elif authentication_status == None:
    st.warning('Please, enter your username and password')
elif authentication_status:
    st.success('Yeah, you got it!! :tada:')
    authenticator.logout('Logout', 'sidebar')
    st.sidebar.title(f'Welcome {name}')