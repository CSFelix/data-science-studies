import streamlit_authenticator as stauth # pip install streamlit-authenticator
import streamlit as st

import database as db

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title='Authenticator'
    , page_icon=':lock:'
    , layout='wide'
)

# ---- USER AUTHENTICATION ----


# loading hashed passwords
users = db.fetch_all_users()
users_dict = { 
    'usernames': { 
        user['key']: { 'name': user['name'], 'password': user['password'] } for user in users 
    } 
}

authenticator = stauth.Authenticate(
    users_dict
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