from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie # pip install streamlit-lottie 

# ---- PAGE CONFIG ----
st.set_page_config(
	page_title='My Webpage'
	, page_icon=':tada:'
	, layout='wide'
)

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code != 200: return None
	return r.json()

def local_css(file_name):
	with open(file_name) as f:
		st.markdown(
			f'<style>{f.read()}</style>'
			, unsafe_allow_html=True
		)

# ---- LOAD ASSETS ----
local_css('./style/style.css')
lottie_coding = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_3rwasyjy.json')
img_tanjiro = Image.open('./images/tanjiro.jpg')
img_tomioka = Image.open('./images/tomioka.jpg')

# ---- HEADER SECTION ----
with st.container():
	st.subheader('Hi, I am Felix :wave:')
	st.title('A Data Scientist from Brazil')
	st.write('Come with me to learn about Data Science, Dashboards and Machine Learning.')
	st.write('[Learn More >](https://csfelix.github.io)')

# ---- WHAT I DO ----
with st.container():
	st.write('----')
	left_column, right_column = st.columns(2)

	with left_column:
		st.header('What I do')
		st.write('##') # adds spacing between elements
		st.write(
			"""
			On my blog you will find tutorials about:
			- Data Science with Python;
			- Data Analysis with Python;
			- SQL;
			- NoSQL with Neo4J and Cipher;
			- Streamlit and Dashboards;
			- Machine Learning;
			- Deep Learning;
			"""
		)
		st.write('[Blog >](https://csfelix.vercel.app)')

		with right_column:
			st_lottie(lottie_coding, height=300, key='Coding')

# ---- PROJECTS ----
with st.container():
	st.write('----')
	st.header('My Projects')
	st.write('##')
	image_column, text_column = st.columns(2)

	with image_column:
		st.image(img_tanjiro)

	with text_column:
		st.subheader('Integrate Lottie Animations with Streamlit Apps')
		st.write(
			"""
			Here you will learn a lot!
			"""
		)
		st.markdown('[Watch Video...](https://youtu.be/TXSOitGoINE)')

with st.container():
	image_column, text_column = st.columns(2)

	with image_column: 
		st.image(img_tomioka)

	with text_column:
		st.subheader('Integrate Lottie Animations with Streamlit Apps')
		st.write(
			"""
			Here you will learn a lot!
			"""
		)
		st.markdown('[Watch Video...](https://youtu.be/TXSOitGoINE)')

# ---- CONTACT ----
with st.container():
	st.write('----')
	st.header('Reach Me!')
	st.write('##')

	contact_form = """
	<form action="https://formsubmit.co/csfelix@gmail.com" method="POST">
		<input type="hidden" name="_captcha" value="false">
     	<input type="text" name="name" placeholder='Your Name' required>
     	<input type="email" name="email" placeholder='Your Email' required>
     	<textarea name='message' placeholder='Your Message' required></textarea>
    	<button type="submit">Send</button>
	</form>
	"""

	left_column, right_column = st.columns(2)
	with left_column:
		st.markdown(contact_form, unsafe_allow_html=True)
	with right_column:
		st.empty()