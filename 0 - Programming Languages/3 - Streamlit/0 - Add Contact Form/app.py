import streamlit as st

# ---- HEADER ----
st.header(':mailbox: Get in Touch With Me!')

# ---- FORM ----
# documentation: https://formsubmit.co
contact_form = """
<form action="https://formsubmit.co/csfelix08@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Details of your message" required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# ---- FORM STYLE ----
def local_css(file_name):
	with open(file_name) as f:
		st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('./style/style.css')