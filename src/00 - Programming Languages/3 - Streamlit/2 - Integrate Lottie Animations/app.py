import json
import requests # pip instal requests
import streamlit as st # pip install streamlit
from streamlit_lottie import st_lottie # pip install streamlit-lottie

# ---- FUNCTIONS ----
def load_lottiefile(filepath: str):
	with open(filepath, 'r') as f:
		return json.load(f)

def load_lottieurl(url: str):
	r = requests.get(url)
	if r.status_code != 200: return None
	return r.json()

# ---- HEADER ----
# webfx.com/tools/emoji-cheat-sheet
st.header(':package: Adding Lottie Animations')

# ---- LOTTIE FILES ----
lottie_laptop = load_lottiefile('./assets/laptop.json')
lottie_robot = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_SI8fvW.json')

# laptop
st_lottie(
	lottie_laptop
	, speed=1
	, reverse=False
	, loop=True
	, quality='low' # low, medium or high
	, height=500
	, width=500
	, key='laptop'
)

# robot
st_lottie(
	lottie_robot
	, height=500
	, width=500
	, key='robot')